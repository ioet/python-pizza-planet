from sqlalchemy.exc import SQLAlchemyError

from ..common.utils import check_required_keys
from ..repositories.managers import (IngredientManager, OrderManager,
                                     SizeManager)
from .base import BaseController


class OrderController(BaseController):
    manager = OrderManager
    __required_info = ('client_name', 'client_dni', 'client_address', 'client_phone', 'size_id')

    @staticmethod
    def calculate_order_price(size_price: float, ingredients: list):
        price = size_price + sum(ingredient.price for ingredient in ingredients)
        return round(price, 2)

    @classmethod
    def create(cls, order: dict):
        if not check_required_keys(cls.__required_info, order):
            return 'Invalid order payload', None

        size_id = order.get('size_id')
        size = SizeManager.get_by_id(size_id)

        if not size:
            return 'Invalid size for Order', None

        ingredient_ids = order.pop('ingredients', [])
        try:
            ingredients = IngredientManager.get_by_id_list(ingredient_ids)
            price = cls.calculate_order_price(size.get('price'), ingredients)
            order_with_price = {**order, 'total_price': price}
            return cls.manager.create(order_with_price, ingredients), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)
