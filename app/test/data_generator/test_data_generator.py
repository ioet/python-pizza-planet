import imp
import pytest
from app.data_generator import create_data 

from ..utils.functions import (shuffle_list, get_random_sequence,
                               get_random_string, get_random_price)

from app.test.fixtures.ingredient import create_ingredients
from app.test.fixtures.size import create_size, create_sizes

def client_data_mock() -> dict:
    return {
        'client_address': get_random_string(),
        'client_dni': get_random_sequence(),
        'client_name': get_random_string(),
        'client_phone': get_random_sequence()
    }

def ingredient_mock() -> dict:
    return {
        'name': get_random_string(),
        'price': get_random_price(10, 20)
    }

def size_mock() -> dict:
    return {
        'name': get_random_string(),
        'price': get_random_price(10, 20)
    }


@pytest.fixture
def order_uri():
    return '/order/'


@pytest.fixture
def client_data():
    return client_data_mock()

@pytest.fixture
def ingredientes():
    return ingredient_mock()

@pytest.fixture
def size():
    return size_mock()

def test_dummy_orders_created(create_ingredients, create_size):
    ingredients = [ingredient.get('_id') for ingredient in create_ingredients]
    size_id = create_size
    order = create_data.main()

    pytest.assume(order[0]['total_price'])