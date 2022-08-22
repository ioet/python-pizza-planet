from sqlalchemy.exc import SQLAlchemyError

from ..common.utils import check_required_keys
from ..repositories.managers import (BeverageManager, IngredientManager, OrderManager,
                                     SizeManager)

from .base import BaseController


class OrderController(BaseController):
    manager = OrderManager
    __required_info = ('client_name', 'client_dni', 'client_address', 'client_phone', 'size_id')

    @staticmethod
    def calculate_order_price(size_price: float, ingredients: list, beverages: list):
        price = sum(_order_detail.price for _order_detail in [*ingredients, *beverages]) + size_price
        return round(price, 2)

    @classmethod
    def create(cls, order: dict):
        current_order = order.copy()
        if not check_required_keys(cls.__required_info, current_order):
            return 'Invalid order payload', None

        size_id = current_order.get('size_id')
        size = SizeManager.get_by_id(size_id)

        if not size:
            return 'Invalid size for Order', None

        ingredient_ids = current_order.pop('ingredients', [])
        beverage_ids = current_order.pop('beverages', [])
        try:
            ingredients = IngredientManager.get_by_id_list(ingredient_ids)
            beverages = BeverageManager.get_by_id_list(beverage_ids)
            price = cls.calculate_order_price(size.get("price"), ingredients, beverages)
            order_with_price = {**current_order, 'total_price': price}
            return cls.manager.create(order_with_price, ingredients, beverages), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)

    @classmethod
    def get_best_ingredients(cls):
        return cls.manager.get_best_ingredients()
    
    @classmethod
    def get_best_customers(cls):
        return cls.manager.get_best_customers()

    @classmethod
    def get_best_months(cls):
        return cls.manager.get_best_months()
