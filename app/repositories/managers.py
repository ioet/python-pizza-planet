from hashlib import new
import json
from traceback import print_tb
from typing import Any, List, Optional, Sequence
from datetime import datetime
from sqlalchemy import func, desc

from sqlalchemy.sql import text, column

from .models import Ingredient, Beverage, Order, OrderDetail, OrderBeverage, Size, db
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
        new_order = cls.model(**order_data)
        if(new_order.date is None):
            new_order.date = datetime.now()
        else:
            new_order.date = datetime.strptime(
                new_order.date, '%Y-%m-%d %H:%M:%S')
        cls.session.add(new_order)
        cls.session.flush()
        cls.session.refresh(new_order)
        cls.session.add_all((OrderDetail(order_id=new_order._id, ingredient_id=ingredient._id, ingredient_price=ingredient.price)
                             for ingredient in ingredients))
        cls.session.add_all((OrderBeverage(order_id=new_order._id, beverage_id=beverage._id, beverage_price=beverage.price)
                             for beverage in beverages))
        cls.session.commit()
        return cls.serializer().dump(new_order)

    @classmethod
    def update(cls):
        raise NotImplementedError(f'Method not suported for {cls.__name__}')


class IndexManager(BaseManager):

    @classmethod
    def test_connection(cls):
        cls.session.query(column('1')).from_statement(text('SELECT 1')).all()


class ReportManager(BaseManager):
    order = Order
    order_detail = OrderDetail
    ingredient = Ingredient

    
    @classmethod
    def get_customer_report(cls):
        return {
            'best_customers': cls.get_best_customers_list(),
        }

    @classmethod
    def get_all_report(cls):
        return {
            'best_customers': cls.get_best_customers_list(),
            'most_requested_ingredient': cls.get_most_requested_ingredients(),
            'date_with_most_revenue': cls.get_date_with_most_revenue()
        }

    @classmethod
    def get_report(cls,func):
        report = func()
        return report

    @classmethod
    def get_best_customers_list(cls):
        best_customers = []
        customers = cls.session.query(cls.order.client_name, func.count(cls.order.client_dni).label(
            'times')).group_by(cls.order.client_dni).order_by(desc('times')).limit(3).all()
        for customer in customers:
            best_customers.append(
                {'client_name': customer.client_name, 'times': customer.times})
        return best_customers
        
    @classmethod
    def get_most_requested_ingredients(cls):
        most_requested_ingredients = []
        ingredients = cls.session.query(cls.ingredient.name, func.count(cls.order_detail.ingredient_id).label('times')).join(
            cls.ingredient, cls.order_detail.ingredient_id == cls.ingredient._id).group_by(cls.order_detail.ingredient_id).order_by(desc('times')).limit(1).all()
        for ingredient in ingredients:
            most_requested_ingredients.append(
                {'name': ingredient.name, 'times': ingredient.times})
        return most_requested_ingredients
    
    @classmethod
    def get_date_with_most_revenue(cls):
        date_with_most_revenue = []
        revenues = cls.session.query(func.strftime('%Y', cls.order.date).label('year'), func.strftime('%m', cls.order.date).label(
            'month'), func.sum(cls.order.total_price).label('total_sales')).group_by('year', 'month').order_by(desc('total_sales')).limit(1).all()
        for revenue in revenues:
            date_with_most_revenue.append(
                {'year': revenue.year, 'month': revenue.month, 'total_sales': revenue.total_sales})
        return date_with_most_revenue
