from app.plugins import ma
from .models import (Ingredient,
                     Size,
                     Order,
                     IngredientDetail,
                     BeveragesDetail,
                     Beverage)


class IngredientSerializer(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Ingredient
        load_instance = True
        fields = ('_id',
                  'name',
                  'price')


class BeverageSerializer(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Beverage
        load_instance = True
        fields = ('_id',
                  'name',
                  'price'
                  )


class SizeSerializer(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Size
        load_instance = True
        fields = ('_id',
                  'name',
                  'price'
                  )


class OrderIngredientsSerializer(ma.SQLAlchemyAutoSchema):

    ingredient = ma.Nested(IngredientSerializer)

    class Meta:
        model = IngredientDetail
        load_instance = True
        fields = (
            'ingredient',
            'ingredient_price',
            'ingredient_id',
        )


class OrderBeveragesSerializer(ma.SQLAlchemyAutoSchema):

    beverage = ma.Nested(BeverageSerializer)

    class Meta:
        model = BeveragesDetail
        load_instance = True
        fields = (
            'beverage',
            'beverage_price',
            'beverage_id',
            'beverage_quantity',
        )


class OrderSerializer(ma.SQLAlchemyAutoSchema):
    size = ma.Nested(SizeSerializer)
    ingredientsDetail = ma.Nested(OrderIngredientsSerializer, many=True)
    beveragesDetail = ma.Nested(OrderBeveragesSerializer, many=True)

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
            'ingredientsDetail',
            'beveragesDetail'
        )
