import pytest

from typing import Any

from app.controllers import (IngredientController, OrderController,
                             SizeController, BeverageController)
from app.controllers.base import BaseController
from app.test.utils.functions import get_random_choice, get_random_sample, shuffle_list, get_random_quantity


def __order(details: list, client_data: dict):
    return {
        **client_data,
        'details': details
    }


def __create_items(items: list, controller: BaseController):
    created_items = []
    for item in items:
        created_item, _ = controller.create(item)
        created_items.append(created_item)
    return created_items


def __create_sizes_and_ingredients(ingredients: list, sizes: list):
    created_ingredients = __create_items(ingredients, IngredientController)
    created_sizes = __create_items(sizes, SizeController)
    return created_sizes if len(created_sizes) > 1 else created_sizes.pop(), created_ingredients


def __create_beverages(b: list):
    created_beverages = __create_items(b, BeverageController)
    return created_beverages


def __pizza(ingredients: list, size: dict):
    ingredients = [{'_id': ingredient.get('_id'), 'quantity': get_random_quantity()} for ingredient in ingredients]
    size_id = size.get('_id')
    return {
        'product_type': 'pizza',
        'ingredients': sorted(ingredients, key=lambda i: str(i.get('_id'))+str(i.get('quantity'))),
        'size_id': size_id
    }


def __product(product: dict):
    id = product.get('_id')
    if id is None:
        return product
    product_type = product.get('product_type')
    return {
        '_id': id,
        'product_type': product_type
    }


def __random_pizza(ingredients: list, sizes: list):
    size = get_random_choice(sizes)
    random_ingredients = get_random_sample(ingredients, get_random_quantity(0, len(ingredients)))
    return __pizza(random_ingredients, size)


def __detail_from_created(created_detail: dict):
    created_product = created_detail.get('product')
    product = {}
    if created_product.get('product_type') == 'pizza':
        product['product_type'] = 'pizza'
        product['size_id'] = created_product.get('size').get('_id')
        product['ingredients'] = sorted([{'_id': i.get('_id'), 'quantity': i.get('quantity')} for i in created_product.get('ingredients')], key=lambda i: str(i.get('_id'))+str(i.get('quantity')))
    if created_product.get('product_type') == 'beverage':
        product['product_type'] = 'beverage'
        product['_id'] = created_product.get('_id')
    return {
        'product': product,
        'quantity': created_detail.get('quantity')
    }


def __generate_order(created_ingredients, created_sizes, created_beverages, client_data):
    order_pizzas = [__random_pizza(created_ingredients, created_sizes) for _ in range(get_random_quantity())]
    order_beverages = get_random_sample(created_beverages, get_random_quantity(0, len(created_beverages)))
    details = [{'product': __product(p), 'quantity': get_random_quantity()} for p in order_pizzas]
    details.extend([{'product': __product(b), 'quantity': get_random_quantity()} for b in order_beverages])
    return __order(details, client_data)
    

def test_create(app, ingredients, sizes, beverages, client_data):
    created_sizes, created_ingredients = __create_sizes_and_ingredients(ingredients, sizes)
    created_beverages = __create_beverages(beverages)
    order = __generate_order(created_ingredients, created_sizes, created_beverages, client_data)
    created_order, error = OrderController.create(order)
    pytest.assume(error is None)
    pytest.assume(created_order['_id'])
    pytest.assume(created_order['total_price'])
    pytest.assume(created_order['date'])
    created_details = [__detail_from_created(d) for d in created_order.get('details')]
    order_details = order.get('details')
    for created_detail in created_details:
        pytest.assume(created_detail in order_details)
    for order_detail in order_details:
        pytest.assume(order_detail in created_details)
        

def test_calculate_order_price(app, ingredients, sizes, beverages, client_data):
    created_sizes, created_ingredients = __create_sizes_and_ingredients(ingredients, sizes)
    created_beverages = __create_beverages(beverages)
    order = __generate_order(created_ingredients, created_sizes, created_beverages, client_data)
    created_order, error = OrderController.create(order)
    expected_price = 0
    details = order.get('details')
    for detail in details:
        quantity = detail.get('quantity')
        product = detail.get('product')
        product_price = None
        if product.get('product_type') == 'pizza':
            size_id = product.get('size_id')
            size_price = None
            for s in created_sizes:
                if s.get('_id') == size_id:
                    size_price = s.get('price')
                    break
            ingredients_cost = 0
            for igredient in product.get('ingredients'):
                ingredient_quantity = igredient.get('quantity')
                ingredient_id = igredient.get('_id')
                ingredient_price = None
                for i in created_ingredients:
                    if i.get('_id') == ingredient_id:
                        ingredient_price = i.get('price')
                        break
                ingredients_cost += ingredient_price * ingredient_quantity
            product_price = size_price + ingredients_cost
        else:
            id = product.get('_id')
            for b in created_beverages:
                if b.get('_id') == id:
                    product_price = b.get('price')
                    break
        detail_price = product_price * quantity
        expected_price += detail_price

    pytest.assume(created_order['total_price'] == expected_price)


def test_get_by_id(app, ingredients, sizes, beverages, client_data):
    created_sizes, created_ingredients = __create_sizes_and_ingredients(ingredients, sizes)
    created_beverages = __create_beverages(beverages)
    order = __generate_order(created_ingredients, created_sizes, created_beverages, client_data)
    created_order, error = OrderController.create(order)
    order_from_db, error = OrderController.get_by_id(created_order['_id'])
    pytest.assume(error is None)
    pytest.assume(order_from_db == created_order)


def test_get_all(app, ingredients, sizes, beverages, client_data):
    created_sizes, created_ingredients = __create_sizes_and_ingredients(ingredients, sizes)
    created_beverages = __create_beverages(beverages)
    created_orders = []
    for _ in range(5):
        order = __generate_order(created_ingredients, created_sizes, created_beverages, client_data)
        created_order, error = OrderController.create(order)
        pytest.assume(error is None)
        created_orders.append(created_order)
    orders_from_db, error = OrderController.get_all()
    pytest.assume(error is None)
    for order_from_db in orders_from_db:
        pytest.assume(order_from_db in created_orders)
    for created_order in created_orders:
        pytest.assume(created_order in orders_from_db)
