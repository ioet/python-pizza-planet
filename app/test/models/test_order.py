import pytest
from app.models import Order
from app.test.utils.functions import get_random_order, get_random_client, get_random_product

def test_order_creation():
    order = get_random_order()
    pytest.assume(type(order) is Order)

def test_get_order_client():
    order = get_random_order()
    client = get_random_client()
    pytest.assume(type(order.getClient()) is type(client))
    
def test_get_order_products():
    order = get_random_order()
    product = get_random_product()
    pytest.assume(type(order.getProduct(0)) is type(product))

def test_get_order_price():
    order = get_random_order()
    pytest.assume(order.getPrice() == 4)

def test_set_order_client():
    order = get_random_order()
    client = get_random_client()
    client.setName('New Client')
    client.setDni('11111111')
    order.setClient(client)
    pytest.assume(order.getClient() is client)

def test_set_order_product():
    order = get_random_order()
    product = get_random_product()
    product.setName('New Product')
    product.setData({'type': '2', 'size': '2'})
    order.setProduct(product)
    pytest.assume(order.getProduct(1) is product)
    
def test_set_order_products():
    order = get_random_order()
    products = [get_random_product(), get_random_product()]
    order.setProducts(products)
    pytest.assume(order.getProduct(0) is products[0])
    pytest.assume(order.getProduct(1) is products[1])

def test_set_order_price():
    order = get_random_order()
    order.setPrice(10)
    pytest.assume(order.getPrice() == 10)