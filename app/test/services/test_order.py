from telnetlib import RSP
import pytest

from app.test.utils.functions import get_random_string, get_random_price


def test_create_orders_service(create_orders):
    for value in create_orders:
        pytest.assume(value.json['_id'])
        pytest.assume(value.json['client_address'])
        pytest.assume(value.json['client_dni'])
        pytest.assume(value.json['client_name'])
        pytest.assume(value.json['client_phone'])
        pytest.assume(value.status.startswith('200'))

def test_get_order_by_id_service(client, create_orders, order_uri):
    orders = []
    for order in create_orders:
        orders.append(order.json)
    current_order = orders[0]
    response = client.get(f'{order_uri}id/{current_order["_id"]}')
    returned_order = response.json
    for param, value in current_order.items():
        pytest.assume(returned_order[param] == value)
    pytest.assume(response.status.startswith('200'))


def test_get_orders_service(client, create_orders, order_uri):
    orders = []
    for order in create_orders:
        orders.append(order.json)
    response = client.get(order_uri)
    returned_order = {order_received['_id']: order_received for order_received in response.json}
    pytest.assume(response.status.startswith('200'))
    pytest.assume(len(orders) == len(returned_order))
    


