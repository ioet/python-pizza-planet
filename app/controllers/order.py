from typing import Optional
from sqlalchemy.exc import SQLAlchemyError

from ..common.utils import check_required_keys
from ..repositories.managers import (BeverageManager, IngredientManager, OrderManager,
                                     SizeManager)
from .base import BaseController

from ..builders.order_builder import OrderBuilder
from ..models import Client, Product

class OrderController(BaseController):
    manager = OrderManager
    __required_info = ('client_name', 'client_dni', 'client_address', 'client_phone', 'size_id')

    @staticmethod
    def calculate_order_price(size_price: float, ingredients: list, beverages: Optional[list]):
        price = 0
        ingredients_price = sum(ingredient.price for ingredient in ingredients)
        if not beverages:
            price = size_price + ingredients_price
        else:
            beverages_price = sum(beverage.price for beverage in beverages)
            price = size_price + ingredients_price + beverages_price        
        return round(price, 2)

    @classmethod
    def create(cls, order: dict):
        current_order = order.copy()
        if not check_required_keys(cls.__required_info, current_order):
            return 'Invalid order payload', None 
        if current_order.get('beverages'):
            return cls.build_order_with_multiple_products(cls, current_order)
        return cls.build_standard_order(cls, current_order)

    def build_client(order_data: dict):
        return Client(order_data.get('client_name'), order_data.get('client_dni'), order_data.get('client_address'), order_data.get('client_phone'))
    
    def build_standard_order(cls, order_data: dict):
        client = cls.build_client(order_data)
        pizza = Product('pizza', {'size_id': order_data.get('size_id'), 'ingredients': order_data.pop('ingredients', [])})
        size = SizeManager.get_by_id(pizza.getData('size_id')) 
        if not size:
            return 'Invalid size for Order', None
        
        try:
            ingredients = IngredientManager.get_by_id_list(pizza.getData('ingredients'))
            price = cls.calculate_order_price(size.get('price'), ingredients, [])
            order_with_price = OrderBuilder().item().standardOrder(client, pizza, price).orderDict()
            return cls.manager.create(order_with_price, ingredients, None), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)

    def build_order_with_multiple_products(cls, order_data: dict):
        client = cls.build_client(order_data)
        pizza = Product('pizza', {'size_id': order_data.get('size_id'), 'ingredients': order_data.pop('ingredients', [])})
        size = SizeManager.get_by_id(pizza.getData('size_id')) 
        if not size:
            return 'Invalid size for Order', None
        
        beverages_ids = order_data.pop('beverages', [])

        try:
            ingredients = IngredientManager.get_by_id_list(pizza.getData('ingredients'))
            beverages = BeverageManager.get_by_id_list(beverages_ids)
            products_beverage = [Product(beverage.name, {'volume': beverage.volume, 'price': beverage.price}) for beverage in beverages]
            price = cls.calculate_order_price(size.get('price'), ingredients, beverages)
            order_with_multiple_products = OrderBuilder().item().standardOrder(client, pizza, price).withMultipleProducts(products_beverage).orderDict()
            return cls.manager.create(order_with_multiple_products, ingredients, beverages), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)