import pytest


def test_create_orden_service(create_order):
    order = create_order
    pytest.assume(order['size_id'])
    pytest.assume(order['ingredients'])
    pytest.assume(order['client_address'])
    pytest.assume(order['client_dni'])
    pytest.assume(order['client_name'])
    pytest.assume(order['client_phone'])


def test_get_orders_service(client, create_orders, order_uri):
    response = client.get(order_uri)
    pytest.assume(response.status.startswith('200'))
    returned_orders = {
        order['_id']: order for order in response.json}
    for order in create_orders:
        order_json = order.json
        pytest.assume(order_json['_id'] in returned_orders)
