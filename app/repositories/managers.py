from itertools import groupby
from multiprocessing.connection import Client
from typing import Any, List, Optional, Sequence
from sqlalchemy.sql import text, column, func, desc
from .models import Ingredient, Beverage, Order, OrderDetail, Size, db
from .serializers import (IngredientSerializer, BeverageSerializer, OrderSerializer,
                          SizeSerializer, ma)



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
    def get_by_id_list(cls, ids: Sequence):
        _objects = cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []
        return _objects

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


class BeverageManager(BaseManager):
    model = Beverage
    serializer = BeverageSerializer


class OrderManager(BaseManager):
    model = Order
    serializer = OrderSerializer

    @classmethod
    def create(cls, order_data: dict, ingredients: List[Ingredient], beverages: List[Beverage]):
        new_order = cls.model(**order_data)
        cls.session.add(new_order)
        cls.session.flush()
        cls.session.refresh(new_order)
        ingredient_details = (
            OrderDetail(
                order_id=new_order._id, ingredient_id=ingredient._id, ingredient_price=ingredient.price
            )
            for ingredient in ingredients
        )
        beverage_details = (
            OrderDetail(
                order_id=new_order._id, beverage_id=beverage._id, beverage_price=beverage.price
            )
            for beverage in beverages
        )
        cls.session.add_all([*ingredient_details, *beverage_details])
        cls.session.commit()
        return cls.serializer().dump(new_order)

    @classmethod
    def get_best_ingredients(cls):
        serializer = cls.serializer(many=True)
        _objects = cls.session.query(
            Ingredient._id,
            func.count(OrderDetail.ingredient_id).label('ingredient')
            )\
            .join(Ingredient)\
            .filter(OrderDetail.ingredient_id != None)\
            .group_by(OrderDetail.ingredient_id)\
            .order_by(desc('ingredient')).limit(3)
        result = serializer.dump(_objects)
        return result

    @classmethod
    def get_best_customers(cls):
        serializer = cls.serializer(many=True)
        _objects = cls.session.query(Order.client_name, func.count(Order._id).label('qty')
        ).group_by(Order.client_name
        ).order_by(desc('qty')
        ).limit(3)
        result = serializer.dump(_objects)
        return result
    
    @classmethod
    def get_best_months(cls):
        serializer = cls.serializer(many=True)
        _objects = cls.session.query(Order.date, func.count(Order._id).label('qty')
        # Here we group by month to prevent fetch same month with different days
        ).group_by(func.strftime("%Y-%m", Order.date)
        ).order_by(desc('qty')
        ).limit(3)
        result = serializer.dump(_objects)
        return result


    @classmethod
    def update(cls):
        raise NotImplementedError(f'Method not supported for {cls.__name__}')


class IndexManager(BaseManager):

    @classmethod
    def test_connection(cls):
        cls.session.query(column('1')).from_statement(text('SELECT 1')).all()
