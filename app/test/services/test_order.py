import json
import pytest

from app.common.utils import response_to_dict


def test_create_order_service(create_order_dict):
    order = create_order_dict.json
    response_has_status_200 = create_order_dict.status.startswith('200')

    pytest.assume(response_has_status_200)
    pytest.assume(order['_id'])
    pytest.assume(order['client_address'])
    pytest.assume(order['client_dni'])
    pytest.assume(order['client_name'])
    pytest.assume(order['client_phone'])
    pytest.assume(order['date'])
    pytest.assume(order['detail'])
    pytest.assume(order['size'])


def test_get_order_by_id_service(client, create_order_dict, order_uri):
    order_object_json = create_order_dict.json

    response = client.get(f'{order_uri}id/{order_object_json["_id"]}')
    response_has_status_200 = response.status.startswith('200')
    response_order_json_data = json.loads(response.data.decode())

    pytest.assume(response_has_status_200)
    pytest.assume(response_order_json_data == order_object_json)


def test_get_orders_service(client, create_orders_list, order_uri):
    response = client.get(order_uri)
    response_has_status_200 = response.status.startswith('200')

    pytest.assume(response_has_status_200)
    response_orders = response_to_dict(response, "_id")
    for created_order in create_orders_list:
        formatted_order = json.loads(created_order.data.decode())
        order_id = formatted_order["_id"]
        order_found = order_id in response_orders
        pytest.assume(order_found)