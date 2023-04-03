import json
import pytest
from app.common.utils import response_to_dict

from app.test.utils.functions import get_random_price, get_random_string


def test_create_size_service(create_size):
    size = create_size.json
    response_has_status_200 = create_size.status.startswith('200')

    pytest.assume(response_has_status_200)
    pytest.assume(size["_id"])
    pytest.assume(size["name"])
    pytest.assume(size["price"])


def test_update_size_service(client, create_size, size_uri):
    size_object_to_update = create_size.json
    updated_size_json_input = {**size_object_to_update,
                               "name": get_random_string(), "price": get_random_price(1, 5)}

    response = client.put(size_uri, json=updated_size_json_input)
    response_has_status_200 = response.status.startswith('200')
    response_size_json_data = json.loads(response.data.decode())

    pytest.assume(response_has_status_200)
    pytest.assume(response_size_json_data == updated_size_json_input)


def test_get_size_by_id_service(client, create_size, size_uri):
    size_object_json = create_size.json

    response = client.get(f'{size_uri}id/{size_object_json["_id"]}')
    response_has_status_200 = response.status.startswith('200')
    response_size_json_data = json.loads(response.data.decode())

    pytest.assume(response_has_status_200)
    pytest.assume(response_size_json_data == size_object_json)


def test_get_sizes_service(client, create_sizes, size_uri):
    response = client.get(size_uri)
    response_has_status_200 = response.status.startswith('200')

    pytest.assume(response_has_status_200)
    response_sizes = response_to_dict(response, "_id")
    for created_size in create_sizes:
        size_id = created_size["_id"]
        size_found = size_id in response_sizes
        pytest.assume(size_found)
