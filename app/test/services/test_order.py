import pytest


def test_create_order_service(create_orders):
    created_order = create_orders[0]
    order = created_order.json
    pytest.assume(created_order.status.startswith('200'))
    pytest.assume(order['_id'])
    pytest.assume(order['client_address'])
    pytest.assume(order['client_dni'])
    pytest.assume(order['client_name'])
    pytest.assume(order['client_phone'])
    pytest.assume(order['date'])
    pytest.assume(order['detail'])
    pytest.assume(order['size'])
    pytest.assume(order['total_price'])

def test_get_orders_service(client, create_orders, order_uri):
    response = client.get(order_uri)
    pytest.assume(response.status.startswith('200'))
    returned_orders = {order['_id']: order for order in response.json}
    for order in create_orders:
        pytest.assume(order.json['_id'] in returned_orders)
