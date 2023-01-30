from sqlalchemy.exc import SQLAlchemyError

from ..common.utils import check_required_keys
from ..repositories.managers import (IngredientManager, OrderManager,
                                     SizeManager)
from .base import BaseController

from ..builders.order_builder import OrderBuilder
from ..models import Client, Product

class OrderController(BaseController):
    manager = OrderManager
    __required_info = ('client_name', 'client_dni', 'client_address', 'client_phone', 'size_id')

    @staticmethod
    def calculate_order_price(size_price: float, ingredients: list):
        price = sum(ingredient.price for ingredient in ingredients)
        return round(price, 2)

    @classmethod
    def create(cls, order: dict):
        current_order = order.copy()
        if not check_required_keys(cls.__required_info, current_order):
            return 'Invalid order payload', None 
        
        client = Client(current_order.get('client_name'), current_order.get('client_dni'), current_order.get('client_address'), current_order.get('client_phone'))
        size_id = current_order.get('size_id')
        size = SizeManager.get_by_id(size_id)   
        ingredient_ids = current_order.pop('ingredients', [])
        pizza = Product('pizza', {'size_id': current_order.get('size_id'), 'ingredients': ingredient_ids})

        if not size:
            return 'Invalid size for Order', None

        try:
            ingredients = IngredientManager.get_by_id_list(ingredient_ids)
            price = cls.calculate_order_price(size.get('price'), ingredients)
            order_with_price = OrderBuilder().item().standardOrder(client, pizza, price).orderDict()
            return cls.manager.create(order_with_price, ingredients), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)
