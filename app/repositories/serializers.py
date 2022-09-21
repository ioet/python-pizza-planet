import typing

from marshmallow import types
from marshmallow import post_dump
from marshmallow.schema import Schema
from marshmallow.exceptions import ValidationError

from app.plugins import ma
from .models import Beverage, Ingredient, Pizza, PizzaIngredient, Size, Order, OrderDetail


class IngredientSerializer(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Ingredient
        load_instance = True
        fields = ('_id', 'name', 'price')


class SizeSerializer(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Size
        load_instance = True
        fields = ('_id', 'name', 'price')


class PizzaIngredientSerializer(ma.SQLAlchemyAutoSchema):

    ingredient = ma.Nested(IngredientSerializer)

    class Meta:
        model = PizzaIngredient
        load_instance = True
        fields = ('ingredient', 'quantity')

    # To flatten data when serializing
    @post_dump
    def flatten_data(self, in_data, **kwargs):
        data = in_data.pop('ingredient')
        in_data.update(data)
        return in_data


class PizzaSerializer(ma.SQLAlchemyAutoSchema):

    size = ma.Nested(SizeSerializer)
    ingredients = ma.Nested(PizzaIngredientSerializer, many=True)

    class Meta:
        model = Pizza
        load_instance = True
        fields = (
            'product_type',
            'size',
            'ingredients'
        )


class BeverageSerializer(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Beverage
        load_instance = True
        fields = (
            'product_type',
            '_id',
            'name',
            'price'
        )
        

class ProductSerializer(Schema):
    type_map = {
        'pizza': PizzaSerializer,
        'beverage': BeverageSerializer
    }

    # To serialize polymorphic product
    def dump(self, obj: typing.Any, *, many: bool = None):
        result = []
        errors = {}
        many = self.many if many is None else bool(many)

        if not many:
            return self._dump(obj)

        for idx, value in enumerate(obj):
            try:
                res = self._dump(value)
                result.append(res)

            except ValidationError as error:
                errors[idx] = error.normalized_messages()
                result.append(error.valid_data)

        if errors:
            raise ValidationError(errors, data=obj, valid_data=result)

        return result

    def _dump(self, obj: typing.Any):
        product_type = getattr(obj, 'product_type')
        inner_schema = ProductSerializer.type_map.get(product_type)

        if inner_schema is None:
            raise ValidationError(f'Missing schema for "{product_type}"')

        return inner_schema().dump(obj)

    # To deserialize polymorphic product
    def load(
        self,
        data: (
            typing.Mapping[str, typing.Any]
            | typing.Iterable[typing.Mapping[str, typing.Any]]
        ),
        *,
        many: bool | None = None,
        partial: bool | types.StrSequenceOrSet | None = None,
        unknown: str | None = None,
    ):

        product_type = data.get('product_type')
        inner_schema = ProductSerializer.type_map.get(product_type)

        if inner_schema is None:
            raise ValidationError(f'Missing schema for "{product_type}"')

        return inner_schema().load(data, many=many, partial=partial, unknown=unknown)


class OrderDetailSerializer(ma.SQLAlchemyAutoSchema):

    product = ma.Nested(ProductSerializer)

    class Meta:
        model = OrderDetail
        load_instance = True
        fields = (
            'product',
            'quantity',
            'price'
        )


class OrderSerializer(ma.SQLAlchemyAutoSchema):

    details = ma.Nested(OrderDetailSerializer, many=True)

    class Meta:
        model = Order
        load_instance = True
        fields = (
            '_id',
            'client_name',
            'client_dni',
            'client_address',
            'client_phone',
            'date',
            'total_price',
            'details'
        )
