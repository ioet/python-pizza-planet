import pytest

from app.test.utils.helpers import generate_order
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
def create_order(client, order_uri, create_ingredients, create_sizes, create_beverages, client_data) -> dict:
    order = generate_order(create_ingredients, create_sizes, create_beverages, client_data)
    response = client.post(order_uri, json=order)
    return response


@pytest.fixture
def create_orders(client, order_uri, create_ingredients, create_sizes, create_beverages) -> list:
    orders = []
    for _ in range(10):
        new_order = client.post(order_uri, json=generate_order(create_ingredients, create_sizes, create_beverages, client_data_mock()))
        orders.append(new_order)
    return orders
