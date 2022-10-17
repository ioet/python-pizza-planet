from datetime import date
import datetime
import json
from typing import Any, Optional, List, Sequence

from ..models import Ingredient, OrderDetail, Beverage, Order
from ..serializers import IngredientSerializer, OrderSerializer, ma, db

from sqlalchemy.sql import text, column, func, desc, extract

class BaseManager:

    def __init__(self, model: Optional[db.Model], serializer: Optional[ma.SQLAlchemyAutoSchema]):
        self.model = model
        self.serializer = serializer
        self.session = db.session

    def get_report(self):
        order_serializer = OrderSerializer(many=True)
        ingredient_serializer = IngredientSerializer(many=False)

        orders = self.session.query(
                Order.client_name,
                func.count(Order.client_name).label('orders')).group_by('client_name').order_by(desc('orders')).all()     
        customers = order_serializer.dump(orders)[0:4]

        ingredients_by_id = self.session.query(
            OrderDetail.ingredient_id,
            func.count(OrderDetail.ingredient_id).label('ingredient')).group_by('ingredient_id').order_by(desc("ingredient")).all()
        ingredient_most_requeted = Ingredient.query.get(ingredients_by_id[0][0])
        result_ingredient = ingredient_serializer.dump(ingredient_most_requeted)["name"]

        month_most_revenue = self.session.query(
            Order.date,
            func.sum(Order.total_price).label('income')).group_by('date').order_by(desc('income')).all()

        report = {
            "most_popular_ingredient": result_ingredient,
            "month_more_revenue": {"month": month_most_revenue[0][0], "income": month_most_revenue[0][1]},
            "best_costumers": customers,
        }

        return report

    def get_all(self):
        serializer = self.serializer(many=True)
        _objects = self.model.query.all()
        result = serializer.dump(_objects)
        return result

    def get_by_id(self, _id: Any):
        entry = self.model.query.get(_id)
        return self.serializer().dump(entry)

    def create(self, entry: dict):
        serializer = self.serializer()
        new_entry = serializer.load(entry)
        self.session.add(new_entry)
        self.session.commit()
        return serializer.dump(new_entry)

    def update(self, _id: Any, new_values: dict):
        self.session.query(self.model).filter_by(_id=_id).update(new_values)
        self.session.commit()
        return self.get_by_id(_id)

    def get_by_id_list(self, ids: Sequence):
        return self.session.query(self.model).filter(
            self.model._id.in_(set(ids))).all() or []

    def create_order(self, order_data: dict,  ingredients: List[Ingredient], beverages: List[Beverage], from_seeder: bool):
        new_order = self.model(**order_data)
        self.session.add(new_order)
        self.session.flush()
        self.session.refresh(new_order)
        if from_seeder:
            self.session.add_all((
                OrderDetail(
                    order_id=new_order._id,
                    ingredient_id=ingredient["_id"],
                    ingredient_price=ingredient["price"],
                ) for ingredient in ingredients
            )
            )
            self.session.add_all((
                OrderDetail(
                    order_id=new_order._id,
                    beverage_id=beverage["_id"],
                    beverage_price=beverage["price"],
                ) for beverage in beverages
            )
            )
        else: 
            self.session.add_all((
                OrderDetail(
                    order_id=new_order._id,
                    ingredient_id=ingredient._id,
                    ingredient_price=ingredient.price,
                ) for ingredient in ingredients
            )
            )
            self.session.add_all((
                OrderDetail(
                    order_id=new_order._id,
                    beverage_id=beverage._id,
                    beverage_price=beverage.price,
                ) for beverage in beverages
            )
            )
        self.session.commit()
        return self.serializer().dump(new_order)

    def test_connection(self):
        self.session.query(column('1')).from_statement(text('SELECT 1')).all()
