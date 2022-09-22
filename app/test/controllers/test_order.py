import pytest

from app.controllers import OrderController
from ..utils.helpers import calculate_order_price, compare_orders, generate_order, create_sizes_and_ingredients, create_beverages, create_sizes_and_ingredients


def test_create(app, ingredients, sizes, beverages, client_data):
    created_sizes, created_ingredients = create_sizes_and_ingredients(ingredients, sizes)
    created_beverages = create_beverages(beverages)
    order = generate_order(created_ingredients, created_sizes, created_beverages, client_data)
    created_order, error = OrderController.create(order)
    pytest.assume(error is None)
    pytest.assume(created_order['_id'])
    pytest.assume(created_order['total_price'])
    pytest.assume(created_order['date'])
    orders_equal = compare_orders
    pytest.assume(orders_equal)
        

def test_calculate_order_price(app, ingredients, sizes, beverages, client_data):
    created_sizes, created_ingredients = create_sizes_and_ingredients(ingredients, sizes)
    created_beverages = create_beverages(beverages)
    order = generate_order(created_ingredients, created_sizes, created_beverages, client_data)
    created_order, error = OrderController.create(order)
    pytest.assume(error is None)
    expected_price = calculate_order_price(order, created_sizes, created_ingredients, created_beverages)
    pytest.assume(created_order['total_price'] == expected_price)


def test_get_by_id(app, ingredients, sizes, beverages, client_data):
    created_sizes, created_ingredients = create_sizes_and_ingredients(ingredients, sizes)
    created_beverages = create_beverages(beverages)
    order = generate_order(created_ingredients, created_sizes, created_beverages, client_data)
    created_order, error = OrderController.create(order)
    order_from_db, error = OrderController.get_by_id(created_order['_id'])
    pytest.assume(error is None)
    pytest.assume(order_from_db == created_order)


def test_get_all(app, ingredients, sizes, beverages, client_data):
    created_sizes, created_ingredients = create_sizes_and_ingredients(ingredients, sizes)
    created_beverages = create_beverages(beverages)
    created_orders = []
    for _ in range(5):
        order = generate_order(created_ingredients, created_sizes, created_beverages, client_data)
        created_order, error = OrderController.create(order)
        pytest.assume(error is None)
        created_orders.append(created_order)
    orders_from_db, error = OrderController.get_all()
    pytest.assume(error is None)
    for order_from_db in orders_from_db:
        pytest.assume(order_from_db in created_orders)
    for created_order in created_orders:
        pytest.assume(created_order in orders_from_db)
