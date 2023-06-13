from app.plugins import ma
from .models import Ingredient, Size, Order, Beverage


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


class BeverageSerializer(ma.SQLAlchemyAutoSchema):
    
        class Meta:
            model = Beverage
            load_instance = True
            fields = ('_id', 'name', 'price')






class OrderSerializer(ma.SQLAlchemyAutoSchema):
    size = ma.Nested(SizeSerializer)
    ingredients = ma.Nested(IngredientSerializer, many=True)
    beverages = ma.Nested(BeverageSerializer, many=True)

    class Meta:
        model = Order
        load_instance = True
        fields = (
            '_id',
            'client_dni',
            'client_address',
            'client_name',
            'client_phone',
            'date',
            'size',
            'total_price',
            'ingredients',
            'beverages'
        )
