from typing import Any, List, Optional, Sequence

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

        
class ReportManager:
    order_model = Order
    ingredient_model = Ingredient
    session = db.session
    order_detail_model = OrderDetail

    @classmethod
    def get_report(cls):
        response = {
            'ingredient':cls.get_most_requested_ingredient(),
            'client_data':cls.get_best_3_clients()
        }
        return response
    
    @classmethod
    def get_most_requested_ingredient(cls):
        ingredient_details = cls.order_detail_model.query.all()
        ingredients = [ingredient_detail.ingredient_id
        for ingredient_detail in ingredient_details if ingredient_detail.ingredient_id != None]

        count=Counter(ingredients)
        max_quantity, max_ingredient_id = 0,0
        for id, quantity in count.items():
            if quantity>max_quantity:
                max_quantity = quantity
                max_ingredient_id = id
        #max_ingredient = cls.order_model.query.get(max_ingredient_id)
        max_ingredient = cls.ingredient_model.query.get(max_ingredient_id)
        return [max_ingredient]
    
    @classmethod
    def get_best_3_clients(cls):
        client_details = cls.order_model.query.all()
        clients_dni = []
        client_id_info = {}
        data = []
        for client_detail in client_details:
            clients_dni.append(client_detail.client_dni)
            client_id_info[client_detail.client_dni] = client_detail._id
        count=Counter(clients_dni)
        
        top_clients = sorted(
        dict(count).items(), key=lambda x: x[1], reverse=True)
        for client in top_clients:
            if len(data) == 3:
                break
            data.append(cls.order_model.query.get(client_id_info[client[0]]))
        return data