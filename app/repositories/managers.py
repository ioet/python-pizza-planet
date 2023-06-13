from typing import Any, List, Optional, Sequence

from sqlalchemy.sql import text, column

from .models import Ingredient, Order, Size, db, Beverage
from .serializers import (IngredientSerializer, OrderSerializer,SizeSerializer, BeverageSerializer, ma)
from ..common.builders.order_builder import OrderBuilder

class BaseManager:
    model: Optional[db.Model] = None
    serializer: Optional[ma.SQLAlchemyAutoSchema] = None
    session = db.session

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

    @classmethod
    def create(cls, entry: dict):
        serializer = cls.serializer()
        new_entry = serializer.load(entry)
        cls.session.add(new_entry)
        cls.session.commit()
        return serializer.dump(new_entry)

    @classmethod
    def update(cls, _id: Any, new_values: dict):
        cls.session.query(cls.model).filter_by(_id=_id).update(new_values)
        cls.session.commit()
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
    

class BeverageManager(BaseManager):
    model = Beverage
    serializer = BeverageSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []




class OrderManager(BaseManager):
    model = Order
    serializer = OrderSerializer

    @classmethod
    def create(cls, order_data: dict, ingredients: List[Ingredient], beverages: List[Beverage]):
        order_builder = OrderBuilder()
        order_builder.with_client_name(order_data['client_name'])
        order_builder.with_client_dni(order_data['client_dni'])
        order_builder.with_client_address(order_data['client_address'])
        order_builder.with_client_phone(order_data['client_phone'])
        order_builder.with_size(order_data['size_id'])
        order_builder.with_total_price(order_data['total_price'])
        order_builder.with_ingredients(ingredients)
        order_builder.with_beverages(beverages)
        new_order = order_builder.build()
        cls.session.add(new_order)
        cls.session.commit()
        return cls.serializer().dump(new_order)



    @classmethod
    def update(cls):
        raise NotImplementedError(f'Method not suported for {cls.__name__}')


class IndexManager(BaseManager):

    @classmethod
    def test_connection(cls):
        cls.session.query(column('1')).from_statement(text('SELECT 1')).all()
