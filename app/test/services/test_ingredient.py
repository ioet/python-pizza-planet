import json
import pytest
from app.common.utils import response_to_dict

from app.test.utils.functions import get_random_string, get_random_price


def test_create_ingredient_service(create_ingredient):
    ingredient = create_ingredient.json
    response_has_status_200 = create_ingredient.status.startswith('200')

    pytest.assume(response_has_status_200)
    pytest.assume(ingredient['_id'])
    pytest.assume(ingredient['name'])
    pytest.assume(ingredient['price'])


def test_update_ingredient_service(client, create_ingredient, ingredient_uri):
    ingredient_object_to_update = create_ingredient.json
    updated_ingredient_json_input = {**ingredient_object_to_update,
                                     'name': get_random_string(), 'price': get_random_price(1, 5)}

    response = client.put(ingredient_uri, json=updated_ingredient_json_input)
    response_has_status_200 = response.status.startswith('200')
    response_ingredient_json_data = json.loads(response.data.decode())

    pytest.assume(response_has_status_200)
    pytest.assume(response_ingredient_json_data ==
                  updated_ingredient_json_input)


def test_get_ingredient_by_id_service(client, create_ingredient, ingredient_uri):
    ingredient_object_json = create_ingredient.json

    response = client.get(
        f'{ingredient_uri}id/{ingredient_object_json["_id"]}')
    response_has_status_200 = response.status.startswith('200')
    response_ingredient_json_data = json.loads(response.data.decode())

    pytest.assume(response_has_status_200)
    pytest.assume(response_ingredient_json_data == ingredient_object_json)


def test_get_ingredients_service(client, create_ingredients, ingredient_uri):
    response = client.get(ingredient_uri)
    response_has_status_200 = response.status.startswith('200')

    pytest.assume(response_has_status_200)
    response_ingredients = response_to_dict(response, "_id")
    for created_ingredient in create_ingredients:
        ingredient_id = created_ingredient["_id"]
        ingredient_found = ingredient_id in response_ingredients
        pytest.assume(ingredient_found)