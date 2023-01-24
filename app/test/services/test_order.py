import pytest


def test_create_order_service(create_order):
    order = create_order
    assert order['client_name'], 'Order should have a client name'
    assert order['client_dni'], 'Order should have a client DNI'
    assert order['client_address'], 'Order should have a client address'
    assert order['client_phone'], 'Order should have a client phone number'
    assert order['date'], 'Order should have a date'


def test_get_order_by_id_service(get_order_by_id_service):
    order = get_order_by_id_service
    assert order['_id'], 'Order should have an _id'
    assert order['client_name'], 'Order should have a client name'
    assert order['client_dni'], 'Order should have a client DNI'
    assert order['client_address'], 'Order should have a client address'
    assert order['client_phone'], 'Order should have a client phone number'
    assert order['date'], 'Order should have a date'
    assert order['total_price'], 'Order should have a total price'
    assert order['size']['_id'], 'Order should have a size'
    assert order['size'], 'Order should have a size'






