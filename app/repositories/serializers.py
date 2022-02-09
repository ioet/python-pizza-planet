from app.plugins import ma
from .models import Ingredient, Size, Order, OrderDetail


class IngredientSerializer(ma.ModelSchema):

    class Meta:
        model = Ingredient
        fields = ('_id', 'name', 'price')


class SizeSerializer(ma.ModelSchema):

    class Meta:
        model = Size
        fields = ('_id', 'name', 'price')


class OrderDetailSerializer(ma.ModelSchema):

    ingredient = ma.Nested(IngredientSerializer)

    class Meta:
        model = OrderDetail
        fields = (
            'ingredient_price',
            'ingredient'
        )


class OrderSerializer(ma.ModelSchema):
    size = ma.Nested(SizeSerializer)
    detail = ma.Nested(OrderDetailSerializer, many=True)

    class Meta:
        model = Order
        fields = (
            '_id',
            'client_name',
            'client_dni',
            'client_address',
            'client_phone',
            'date',
            'total_price',
            'size',
            'detail'
        )
