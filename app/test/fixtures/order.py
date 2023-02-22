import json

import pytest
from datetime import datetime
from faker import Faker
from faker.generator import random
from app.repositories.models import Ingredient, Size, Beverage
from ..utils.functions import (shuffle_list, get_random_sequence,
                               get_random_string, get_random_phone, get_random_choice, create_random_date,
                               )
from ...controllers import IngredientController, SizeController


def client_data_mock() -> dict:
    fake = Faker()
    return {
        'client_address': fake.address(),
        'client_dni': fake.random_number(digits=8),
        'client_name': fake.name(),
        'client_phone': fake.phone_number()
    }


@pytest.fixture
def order_uri():
    return '/order/'


@pytest.fixture
def client_data():
    return client_data_mock()


@pytest.fixture
def clients_data():
    return [client_data_mock() for _ in range(3)]

@pytest.fixture
def order(create_beverages, create_ingredients, create_size, client_data) -> dict:
    ingredients = [ingredient.get('_id') for ingredient in create_ingredients]
    beverages = [beverage.get('_id') for beverage in create_beverages]
    size_id = create_size.json['_id']
    return {
        **client_data,
        'ingredients': ingredients,
        'beverages': beverages,
        'size_id': size_id
    }
    
@pytest.fixture
def create_order(client, order_uri, create_ingredients, create_beverages, create_size, client_data):
    ingredients = [ingredient.get('_id') for ingredient in create_ingredients]
    beverages = [beverage.get('_id') for beverage in create_beverages]
    size_id = create_size.json['_id']
    order_data = {
        **client_data,
        'ingredients': ingredients,
        'beverages': beverages,
        'size_id': size_id,
        'date': create_random_date()
    }
    return order_data

@pytest.fixture
def get_order_by_id():
    fake = Faker()
    order = {
        '_id': fake.uuid4(),
        'client_name': fake.name(),
        'client_dni': fake.random_number(digits=8),
        'client_address': fake.address(),
        'client_phone': fake.phone_number(),
        'date': fake.date_time_this_decade(),
        'total_price': fake.random_number(),
        'size': {'_id': fake.random_number()}
    }
    return order
