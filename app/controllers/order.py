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
        price = sum(ingredient.price for ingredient in ingredients) + size_price
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
        try:
            ingredients = IngredientManager.get_by_id_list(ingredient_ids)
            price = cls.calculate_order_price(size.get('price'), ingredients)
            order_with_price = {**current_order, 'total_price': price}
            return cls.manager.create(order_with_price, ingredients), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)

    @classmethod
    def get_report_data(cls):
        try:
            all_orders = cls.manager.get_all()
            names = []
            customers_frequency = {}
            top_customers = []

            for order in all_orders:
                names.append(order['client_name'])
            
            for name in names:
                if name in customers_frequency:
                    customers_frequency[name] += 1
                else:
                    customers_frequency[name] = 1

            for round in range(3):
                if len(customers_frequency) > 0:
                   top_customers.append({'name': max(customers_frequency), 'number_of_orders': customers_frequency[max(customers_frequency)]})
                   customers_frequency.pop(max(customers_frequency))


            ingredients = []
            ingredients_frequency = {}
            top_ingredients = {}

            for order in all_orders:
                for detail in order['detail']:
                    ingredients.append(detail['ingredient']['name'])

            for ingredient in ingredients:
                if ingredient in ingredients_frequency:
                    ingredients_frequency[ingredient] += 1
                else:
                    ingredients_frequency[ingredient] = 1

            top_ingredients.update({'name': max(ingredients_frequency), 'number_of_orders': ingredients_frequency[max(ingredients_frequency)]})


            months = []
            months_revenue = {}

            for order in all_orders:
                months.append(order['date'][5:7] + ' ' + str(order['total_price']))

            for month in months:
                if month in months_revenue:
                    months_revenue[month] += month[3:]
                else:
                    months_revenue[month[:2]] = month[3:]
            
            greatest_revenue_month = {'month': max(months_revenue), 'Revenue': months_revenue[max(months_revenue)]}


            return [top_customers, top_ingredients, greatest_revenue_month], None

        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)
