from app.plugins import ma
from .models import (Ingredient,
                     Size,
                     Order,
                     IngredientDetail,
                     BeveragesDetail,
                     Beverage)

class SerializerFactory:
    def __init__(self, model, load_instance=True, fields=None):
        self.model = model
        self.load_instance = load_instance
        self.fields = fields

    def create(self, class_name, nested_serializers=None):
        class Meta:
            model=self.model
            load_instance=self.load_instance
            fields=self.fields

        class_attrs = {'Meta': Meta}

        if nested_serializers:
            for field_name, (serializer, many) in nested_serializers.items():
                class_attrs[field_name] = ma.Nested(serializer, many=many)

        serializer_class = type(class_name, (ma.SQLAlchemyAutoSchema, ), class_attrs)
        
        return serializer_class              

IngredientSerializer = SerializerFactory(
    Ingredient, 
    fields=('_id', 'name', 'price')).create('IngredientSerializer')

BeverageSerializer = SerializerFactory(
    Beverage, 
    fields=('_id', 'name', 'price')).create('BeverageSerializer')

SizeSerializer = SerializerFactory(
    Size, 
    fields=('_id', 'name', 'price')).create('SizeSerializer')

OrderIngredientsSerializer = SerializerFactory(
    IngredientDetail, 
    fields=('ingredient', )).create('OrderIngredientsSerializer',
                                   nested_serializers={'ingredient': (IngredientSerializer, False)})

OrderBeveragesSerializer = SerializerFactory(
    BeveragesDetail, 
    fields=('beverage', 'beverage_quantity')).create('OrderBeveragesSerializer',
                                                    nested_serializers={'beverage': (BeverageSerializer, False)})

OrderSerializer = SerializerFactory(
    Order, 
    fields=('_id', 
            'client_name', 
            'client_dni', 
            'client_address', 
            'client_phone', 
            'date', 
            'total_price', 
            'size', 
            'ingredientsDetail', 
            'beveragesDetail')).create('OrderSerializer', 
                                       nested_serializers={'size': (SizeSerializer, False), 
                                                           'ingredientsDetail': (OrderIngredientsSerializer, True),
                                                           'beveragesDetail': (OrderBeveragesSerializer, True)})
