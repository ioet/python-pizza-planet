from ast import Tuple
from collections import Counter
from typing import Any, List, Optional, Sequence

from sqlalchemy.sql import text, column

from .models import (
    Ingredient,
    Order,
    OrderDetail,
    Size,
    Beverage,
    BeverageOrderDetail,
    db,
)
from .serializers import (
    IngredientSerializer,
    OrderSerializer,
    SizeSerializer,
    BeverageSerializer,
    ma,
)

from sqlalchemy import func, desc

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
        return (
            cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []
        )


class BeverageManager(BaseManager):
    model = Beverage
    serializer = BeverageSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return (
            cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []
        )


class OrderManager(BaseManager):
    model = Order
    serializer = OrderSerializer

    @classmethod
    def create(
        cls, order_data: dict, ingredients: List[Ingredient], beverages: List[Beverage]
    ):
        new_order = cls.model(**order_data)
        cls.session.add(new_order)
        cls.session.flush()
        cls.session.refresh(new_order)
        cls.session.add_all(
            (
                OrderDetail(
                    order_id=new_order._id,
                    ingredient_id=ingredient._id,
                    ingredient_price=ingredient.price,
                )
                for ingredient in ingredients
            )
        )
        cls.session.add_all(
            (
                BeverageOrderDetail(
                    order_id=new_order._id,
                    beverage_id=beverage._id,
                    beverage_price=beverage.price,
                )
                for beverage in beverages
            )
        )
        cls.session.commit()
        return cls.serializer().dump(new_order)

    @classmethod
    def update(cls):
        raise NotImplementedError(f"Method not suported for {cls.__name__}")


class IndexManager(BaseManager):
    @classmethod
    def test_connection(cls):
        cls.session.query(column("1")).from_statement(text("SELECT 1")).all()

class ReportManager(BaseManager):
    order_model = Order
    ingredient_model = OrderDetail
    session = db.session

    @classmethod
    def get_most_requested_ingredient(cls) -> dict:
        ingredients = cls.session.query(
            cls.ingredient_model).all()
        ingredients_ids = [ingredient.ingredient_id
                               for ingredient
                               in ingredients]
                               
        ingredients_with_times = Counter(ingredients_ids)
        ingredient_id = 0
        for id, times in ingredients_with_times.most_common(1):
            ingredient_id = id
            ingredient_count = times

        most_requested_ingredient = Ingredient.query.get(ingredient_id)
        if most_requested_ingredient:
            return {
                'name': most_requested_ingredient.name,
                'times': ingredient_count
            }

    @classmethod
    def get_month_with_more_revenue(cls) -> dict:
        orders = cls.session.query(cls.order_model).all()

        dates_price_of_orders = [(order.date.month, order.total_price)
                     for order in orders]

        new_month_revenue = cls.update_values(dates_price_of_orders)

        max_price_in_month= 0
        month_name = ""
        for month, price in new_month_revenue.items():
            if price > max_price_in_month :
                max_price_in_month = price
                month_name = month

        if dates_price_of_orders:
            return {
                'month': month_name,
                'revenue': round(max_price_in_month, 2)
            }

    @classmethod
    def get_best_customers(cls) -> list:
        orders = cls.session.query(cls.order_model).all()
        clients_with_price = [(client.client_dni, client.total_price) for client in orders]

        new_clients = cls.update_values(clients_with_price)
        
        clients_count= Counter(new_clients)
        best_customers = clients_count.most_common(3) 
        if best_customers:
            return [
                {
                    'dni': dni,
                    'name': cls.get_client_name(dni, orders),
                    'total_purchase': total_purchase
                } for dni, total_purchase in best_customers
            ]

    @staticmethod
    def update_values(list_tuples) -> dict:        
        dictionary = {} 
        for key, value in list_tuples:
            dictionary.update({key: value}) 

        new_dictionary = {} 
        for key, value in list_tuples: 
            new_dictionary.update(
                {key: value + dictionary.get(key)})

        return new_dictionary 

    @staticmethod
    def get_client_name(dni: str, orders: list) -> str:
        for order in orders:
            if order.client_dni == dni:
                return order.client_name

