import json
import pytest
from app.common.utils import response_to_dict

from app.test.utils.functions import get_random_string, get_random_price


def test_create_beverage_service(create_beverage):
    beverage = create_beverage.json
    response_has_status_200 = create_beverage.status.startswith('200')

    pytest.assume(response_has_status_200)
    pytest.assume(beverage['_id'])
    pytest.assume(beverage['name'])
    pytest.assume(beverage['price'])


def test_update_beverage_service(client, create_beverage, beverage_uri):
    beverage_object_to_update = create_beverage.json
    updated_beverage_json_input = {**beverage_object_to_update,
                                   'name': get_random_string(), 'price': get_random_price(1, 5)}

    response = client.put(beverage_uri, json=updated_beverage_json_input)
    response_has_status_200 = response.status.startswith('200')
    response_beverage_json_data = json.loads(response.data.decode())

    pytest.assume(response_has_status_200)
    pytest.assume(response_beverage_json_data ==
                  updated_beverage_json_input)


def test_get_beverage_by_id_service(client, create_beverage, beverage_uri):
    beverage_object_json = create_beverage.json

    response = client.get(
        f'{beverage_uri}id/{beverage_object_json["_id"]}')
    response_has_status_200 = response.status.startswith('200')
    response_beverage_json_data = json.loads(response.data.decode())

    pytest.assume(response_has_status_200)
    pytest.assume(response_beverage_json_data == beverage_object_json)


def test_get_beverages_service(client, create_beverages, beverage_uri):
    response = client.get(beverage_uri)
    response_has_status_200 = response.status.startswith('200')

    pytest.assume(response_has_status_200)
    response_beverages = response_to_dict(response, "_id")
    for created_beverage in create_beverages:
        beverage_id = created_beverage["_id"]
        beverage_found = beverage_id in response_beverages
        pytest.assume(beverage_found)