import pytest


def test_get_orders_for_report(client, create_orders, order_uri):
    response = client.get(order_uri)
    pytest.assume(response.status.startswith('200'))
    pytest.assume(len(response.json) == 10)
    for order in response.json:
        pytest.assume(order['_id'])