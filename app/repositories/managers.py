from typing import Any, List, Optional, Sequence

from sqlalchemy import func
from sqlalchemy.sql import text, column

from .models import Ingredient, Order, OrderBeverage, OrderDetail, Size, Beverage, db
from .serializers import (IngredientSerializer, OrderSerializer,
                          SizeSerializer, BeverageSerializer, ma)
from collections import Counter
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

class BeverageManager(BaseManager):
    model = Beverage
    serializer = BeverageSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []

class IngredientManager(BaseManager):
    model = Ingredient
    serializer = IngredientSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []


class OrderManager(BaseManager):
    model = Order
    serializer = OrderSerializer

    @classmethod
    def create(cls, order_data: dict, ingredients: List[Ingredient], beverages: List[Beverage]):
        new_order = cls.model(**order_data)
        cls.session.add(new_order)
        cls.session.flush()
        cls.session.refresh(new_order)
        cls.session.add_all(
            (OrderDetail(
                order_id=new_order._id, 
                ingredient_id=ingredient._id, 
                ingredient_price=ingredient.price)
                for ingredient in ingredients))
        cls.session.add_all(
            (OrderBeverage(
                order_id=new_order._id,
                beverage_id=beverage._id,
                beverage_price=beverage.price)
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
    model: None
    serializer: None

    @classmethod
    def get_report(cls):
        ingredient = cls.most_request_ingredient()
        month = cls.month_with_more_revenue()
        best_three_customers = cls.best_customers(3)
        result = {
            "most_request_ingredient": ingredient,
            "month_with_more_revenue": month,
            "top_3_customers": best_three_customers,
        }
        return result

    @classmethod
    def most_request_ingredient(cls):
        id = cls.session.query(OrderDetail.ingredient_id)\
            .group_by(OrderDetail.ingredient_id)\
            .order_by(func.count(OrderDetail.ingredient_id)\
            .desc()).limit(1).scalar()
        ingredient = Ingredient.query.get(id)

        return IngredientSerializer().dump(ingredient)


    @classmethod
    def month_with_more_revenue(cls):
        v1 = func.strftime('%m-%Y', Order.date).label('month')
        v2 = func.sum(Order.total_price).label('revenue')
        result = cls.session.query(v1, v2)\
            .group_by('month')\
            .order_by(text('revenue DESC'))\
            .first()

        return {"month": result[0], "revenue": round(result[1], 2)}


    @classmethod
    def best_customers(cls, quantity):
        v1 = Order.client_name.label('client_name')
        v2 = func.sum(Order.total_price).label('total_spent')
        query_result = cls.session.query(v1, v2)\
            .group_by('client_name')\
            .order_by(text('total_spent DESC'))\
            .limit(quantity).all()
        result = [{"client_name": cust[0], "total_spent": cust[1]} for cust in query_result]

        return result