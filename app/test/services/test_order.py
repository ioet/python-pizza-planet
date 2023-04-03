import pytest

def test_create_order_service(get_order_by_id):
    # Create an order
    order = get_order_by_id
    
    # Verify that the required fields of the order exist
    assert 'client_name' in order, 'Order should have a client name'
    assert 'client_dni' in order, 'Order should have a client DNI'
    assert 'client_address' in order, 'Order should have a client address'
    assert 'client_phone' in order, 'Order should have a client phone number'
    assert 'date' in order, 'Order should have a date'

def test_get_order_by_id(get_order_by_id):
    # Get an order by ID
    order = get_order_by_id
    
    # Verify that the required fields of the order exist
    assert '_id' in order, 'Order should have an _id'
    assert 'client_name' in order, 'Order should have a client name'
    assert 'client_dni' in order, 'Order should have a client DNI'
    assert 'client_address' in order, 'Order should have a client address'
    assert 'client_phone' in order, 'Order should have a client phone number'
    assert 'date' in order, 'Order should have a date'
    assert 'total_price' in order, 'Order should have a total price'
    assert 'size' in order, 'Order should have a size'
    assert '_id' in order['size'], 'Size should have an _id'

