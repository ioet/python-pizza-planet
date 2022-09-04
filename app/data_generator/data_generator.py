from abc import ABC, abstractmethod
from asyncio.windows_events import NULL
from datetime import datetime
from random import randint

class DataGenerator(ABC):
    
    @abstractmethod
    def create_dummy_data(**kwargs):
        pass


    def generate_orders(customer, ingredients, size, date):
        pass


class CustomerGenerator(DataGenerator):

    def create_dummy_data(customer_address, customer_dni, customer_name, customer_phone):
        new_customer = {
            'customer_address': customer_address,
            'customer_dni': customer_dni,
            'customer_name': customer_name,
            'customer_phone': customer_phone
        }
        return new_customer
    
class IngredientGenerator(DataGenerator):

    def create_dummy_data(name, price):
        new_ingredient = {
            'name': name,
            'price': price
        }
        return new_ingredient


class SizeGenerator(DataGenerator):

    def create_dummy_data(name, price):        
        new_size = {
            'name': name,
            'price': price
        }
        return new_size

class OrderGenerator(DataGenerator):

    def create_dummy_data(customer, ingredients, size):
        new_order = {
            'client_name': customer['customer_name'],
            'client_dni': customer['customer_dni'],
            'client_phone': customer['customer_phone'],
            'client_address': customer['customer_address'],
            'date': datetime(2022, randint(1,8), randint(0,30)),
            'total_price': NULL,
            'size_id': size
        }
        return new_order