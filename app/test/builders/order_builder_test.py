import pytest
from app.builders.order_builder import OrderBuilder
from app.models.order import Order
from app.test.utils.functions import get_random_client, get_random_product

def test_type_order_builder():
    order_builder = OrderBuilder().item()
    pytest.assume(type(order_builder) is OrderBuilder)

def test_build_order():
    order_builder = OrderBuilder().item()
    order = order_builder.build()
    pytest.assume(type(order) is Order)

def test_build_order_with_multiple_products():
    order_builder = OrderBuilder().item()
    order = order_builder.withMultipleProducts([1,2,3]).build()
    pytest.assume(type(order) is Order)

def test_build_standard_order():
    order_builder = OrderBuilder().item()
    order = order_builder.standardOrder(get_random_client(), get_random_product(), 3).build()
    pytest.assume(type(order) is Order)


