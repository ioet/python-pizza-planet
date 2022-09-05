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
def order(client_data, create_ingredients, create_size, create_beverages) -> dict:
    ingredients = [ingredient.get('_id') for ingredient in create_ingredients]
    beverage = [beverage.get('_id') for beverage in create_beverages]
    size_id = create_size.json.get('_id')
    return {
        **client_data,
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


@pytest.fixture
def create_repeted_clients_and_ingredients_order(client, create_size, 
                    ingredient_uri, create_beverages, client_data, ingredient, repeted_ingredients) -> dict:
    most_repeated_client = client_data
    orders = []
    #most_repeated_ingredient_id = ingredient.get('_id')
    ingredients_to_create, most_repeated_ingredient = repeted_ingredients
    created_ingredients = [client.post(ingredient_uri, json=ingredient) for ingredient in ingredients_to_create]
    ingredients = [ingredient.json.get('_id') for ingredient in created_ingredients]
    beverage = [beverage.get('_id') for beverage in create_beverages]
    size_id = create_size.json.get('_id')
    for _ in range(4):
        new_order = {
            **most_repeated_client,
            'ingredients': ingredients,
            'size_id': size_id,
            'beverages': beverage
        }
        orders.append(new_order)
        new_order = {
            **client_data_mock(),
            'ingredients': ingredients,
            'size_id': size_id,
            'beverages': beverage
        }
        orders.append(new_order)

    return orders, most_repeated_client, most_repeated_ingredient
