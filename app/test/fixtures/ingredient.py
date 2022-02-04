import pytest

from ..utils.functions import get_random_price, get_random_string


@pytest.fixture
def ingredient_uri():
    return '/ingredient'


@pytest.fixture
def ingredient() -> dict:
    return {
        'name': get_random_string(),
        'price': get_random_price(10, 20)
    }


@pytest.fixture
def create_ingredient(client, ingredient_uri) -> dict:
    response = client.post(ingredient_uri, json=ingredient())
    return response.json


@pytest.fixture
def create_ingredients(client, ingredient_uri) -> list:
    ingredients = []
    for _ in range(10):
        new_ingredient = client.post(ingredient_uri, json=ingredient())
        ingredients.append(new_ingredient.json)
    return ingredients
