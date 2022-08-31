import pytest


def test_create_order_service(create_orders):
    for created_order in create_orders:
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
