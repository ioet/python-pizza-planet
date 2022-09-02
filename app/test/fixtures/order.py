import pytest

from ..utils.functions import (shuffle_list, get_random_sequence,
                               get_random_string)


def client_data_mock() -> dict:
    return {
        'client_address': get_random_string(),
        'client_dni': get_random_sequence(),
        'client_name': get_random_string(),
        'client_phone': get_random_sequence()
    }


@pytest.fixture
def order_uri():
    return '/order/'


@pytest.fixture
def client_data():
    return client_data_mock()


@pytest.fixture
def order(create_ingredients, create_size, create_beverages) -> dict:
    ingredients = [ingredient.get('_id') for ingredient in create_ingredients]
    beverage = [beverage.get('_id') for beverage in create_beverages]
    size_id = create_size.json.get('_id')
    return {
        **client_data_mock(),
        'ingredients': ingredients,
        'size_id': size_id,
        'beverages': beverage
    }


@pytest.fixture
def create_orders(create_order) -> list:
    orders = []
    for _ in range(10):
        new_order = create_order
        orders.append(new_order)
    return orders

@pytest.fixture
def create_order(client, order, order_uri):
    response = client.post(order_uri, json=order)
    return response
