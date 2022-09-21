from typing import Any, Optional, Sequence

from sqlalchemy.sql import text, column

from app.plugins import db
from app.plugins import ma
from .models import Beverage, Ingredient, Order, OrderDetail, Pizza, PizzaIngredient, Size
from .serializers import (BeverageSerializer, IngredientSerializer, OrderSerializer, PizzaIngredientSerializer, PizzaSerializer,
                          SizeSerializer)

class BaseManager:

    def __init__(self, session=None):
        self.session = session

    model: Optional[db.Model] = None
    serializer: Optional[ma.SQLAlchemyAutoSchema] = None
    session = None

    @classmethod
    def get_all(cls):
        serializer = cls.serializer(many=True)
        _objects = cls.model.query.all()
        result = serializer.dump(_objects)
        return result

    @classmethod
    def get_by_id(cls, _id: Any):
        entry = cls.model.query.get(_id)
        return cls.serializer().dump(entry)

    def create(cls, entry: dict):
        serializer = cls.serializer()
        new_entry = serializer.load(entry)
        cls.session.add(new_entry)
        cls.session.flush()
        cls.session.refresh(new_entry)
        return serializer.dump(new_entry)

    def update(cls, _id: Any, new_values: dict):
        cls.session.query(cls.model).filter_by(_id=_id).update(new_values)
        return cls.get_by_id(_id)


class SizeManager(BaseManager):
    model = Size
    serializer = SizeSerializer


class IngredientManager(BaseManager):
    model = Ingredient
    serializer = IngredientSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []


class OrderManager(BaseManager):
    model = Order
    serializer = OrderSerializer

    product_map = {
        'pizza': Pizza,
        'beverage': Beverage
    }

    @classmethod
    def get_product_model(cls, product: dict):
        return cls.product_map.get(product.get('product_type', None))

    def create(self, order_data: dict):
        details = order_data.pop('details')
        new_order = self.model(**order_data)
        self.session.add(new_order)
        self.session.flush()
        self.session.refresh(new_order)
        for detail in details:
            product_data = detail.pop('product')
            product_type = product_data.get('product_type')
            product_manager = ProductManager(product_type, session=self.session)
            new_product = product_manager.get_or_create(product_data)
            new_product_id = new_product.get('_id')
            self.session.add(OrderDetail(**detail, order_id=new_order._id, product_id=new_product_id))
        self.session.refresh(new_order)
        return self.serializer().dump(new_order)

    def update(cls):
        raise NotImplementedError(f'Method not suported for {cls.__name__}')


class IndexManager(BaseManager):

    @classmethod
    def test_connection(cls):
        cls.session.query(column('1')).from_statement(text('SELECT 1')).all()


class PizzaIngredientManager(BaseManager):
    model = PizzaIngredient
    serializer = PizzaIngredientSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        entries = cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []
        return [cls.serializer().dump(entry) for entry in entries]


class PizzaManager(BaseManager):
    model = Pizza
    serializer = PizzaSerializer

    @classmethod
    def calculate_price(cls, data):
        size_id = data.get('size_id')
        size_price = SizeManager.get_by_id(size_id).get('price')

        ingredients_data = data.get('ingredients', [])
        ingredients_with_quantity = [{**IngredientManager.get_by_id(i.get('_id')), 'quantity': i.get('quantity')} for i in ingredients_data]

        return size_price + sum(i.get('price')*i.get('quantity') for i in ingredients_with_quantity)

    def get_or_create(self, data):
        id = data.get('_id')
        if id is None:
            ingredients = data.pop('ingredients', [])
            new_product = self.model(**data)
            self.session.add(new_product)
            self.session.flush()
            self.session.refresh(new_product)
            product_id = new_product._id
            pizza_ingredients_data = [{'ingredient_id': i.get('_id'), 'pizza_id': product_id, 'quantity': i.get('quantity')} for i in ingredients]
            self.session.add_all(PizzaIngredient(**i) for i in pizza_ingredients_data)
            return {**self.serializer().dump(new_product), '_id': product_id}
        return self.get_by_id(id)
    

class BeverageManager(BaseManager):
    model = Beverage
    serializer = BeverageSerializer
    
    @classmethod
    def calculate_price(cls, data):
        beverage_id = data.get('_id', None)
        return BeverageManager.get_by_id(beverage_id).get('price')

    
    def create(self, data):
        data['product_type'] = 'beverage'
        return super().create(data)


    def get_or_create(self, data):
        id = data.get('_id')
        if id is None:
            return self.create(data)
        return self.get_by_id(id)


class ProductManager(BaseManager):

    product_map = {
        'pizza': PizzaManager,
        'beverage': BeverageManager
    }

    def __new__(self, product_type, *args, **kwargs):
        return self.product_map.get(product_type)(*args, **kwargs)

    @classmethod
    def calculate_price():
        return 0

    def get_or_create(self, data):
        return {}