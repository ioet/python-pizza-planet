from app.plugins import ma
from .models import Ingredient, Size, Order, IngredientDetail, BeveragesDetail, Beverage


class IngredientSerializer(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Ingredient
        load_instance = True
        fields = ('_id', 'name', 'price')


class BeverageSerializer(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Beverage
        load_instance = True
        fields = ('_id', 'name', 'price')


class SizeSerializer(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Size
        load_instance = True
        fields = ('_id', 'name', 'price')


class OrderIngredientsSerializer(ma.SQLAlchemyAutoSchema):

    ingredient = ma.Nested(IngredientSerializer)

    class Meta:
        model = IngredientDetail
        load_instance = True
        fields = (
            'ingredient_price',
            'ingredient'
        )

class OrderBeveragesSerializer(ma.SQLAlchemyAutoSchema):

    ingredient = ma.Nested(IngredientSerializer)

    class Meta:
        model = BeveragesDetail
        load_instance = True
        fields = (
            'beverage_price',
            'beverage_quantity',
            'beverage'
        )


class OrderSerializer(ma.SQLAlchemyAutoSchema):
    size = ma.Nested(SizeSerializer)
    ingredientsDetails = ma.Nested(OrderIngredientsSerializer, many=True)
    beveragesDetails = ma.Nested(OrderBeveragesSerializer, many=True)

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
            'size',
            'ingredientsDetails',
            'beveragesDetails'
        )
