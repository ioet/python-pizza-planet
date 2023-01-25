import pytest
from app.controllers import (IngredientController, OrderController, BeverageController, 
                             SizeController)
from app.controllers.base import BaseController
from app.test.utils.functions import get_random_choice, shuffle_list


def __order(ingredients: list,  beverages: list, size: dict, client_data: dict):
    ingredients = [ingredient.get('_id') for ingredient in ingredients]
    beverages = [beverage.get('_id') for beverage in beverages]
    size_id = size.get('_id')
    return {
        **client_data,
        'ingredients': ingredients,
        'beverages': beverages,
        'size_id': size_id
    }


def __create_items(items: list, controller: BaseController):
    created_items = []
    for item in items:
        created_item, _ = controller.create(entry= item)
        created_items.append(created_item)
    return created_items


def __create_beverages_sizes_and_ingredients(ingredients: list, sizes: list, beverages: list):
    created_ingredients = __create_items(items= ingredients,controller= IngredientController)
    created_sizes = __create_items(items= sizes, controller= SizeController)
    created_beverages = __create_items(items= beverages,controller= BeverageController)
    return created_sizes if len(created_sizes) > 1 else created_sizes.pop(), created_ingredients, created_beverages


def test_create(app, ingredients, beverages, size, client_data):
    created_sizes, created_ingredients , created_beverages = __create_beverages_sizes_and_ingredients(ingredients= ingredients,sizes= [size], beverages= beverages)
    order = __order(ingredients= created_ingredients,beverages =created_beverages, size= created_sizes, client_data= client_data)
    created_order, error = OrderController.create(order= order)
    size_id = order.pop('size_id', None)
    ingredient_ids = order.pop('ingredients', [])
    beverages_ids = order.pop('beverages', [])
    pytest.assume(error is None)
    for param, value in order.items():
        pytest.assume(param in created_order)
        pytest.assume(value == created_order[param])
        pytest.assume(created_order['_id'])
        pytest.assume(size_id == created_order['size']['_id'])

        ingredients_in_detail = set(item['ingredient']['_id'] for item in created_order['detail'])
        beverages_in_detail = set(item['beverage']['_id'] for item in created_order['beverage_detail'])
        pytest.assume(not ingredients_in_detail.difference(ingredient_ids))        
        pytest.assume(not beverages_in_detail.difference(beverages_ids))



def test_calculate_order_price(app, ingredients, beverages, size, client_data):
    created_sizes, created_ingredients , created_beverages = __create_beverages_sizes_and_ingredients(ingredients= ingredients,sizes= [size], beverages= beverages)
    order = __order(ingredients= created_ingredients,beverages =created_beverages, size= created_sizes, client_data= client_data)
    created_order, _ = OrderController.create(order= order)
    pytest.assume(created_order['total_price'] == round(
        created_sizes['price'] + 
        sum(ingredient['price'] for ingredient in created_ingredients)+
        sum(beverage['price'] for beverage in created_beverages), 2))


def test_get_by_id(app, ingredients, beverages, size, client_data):
    created_sizes, created_ingredients , created_beverages = __create_beverages_sizes_and_ingredients(ingredients= ingredients,sizes= [size], beverages= beverages)
    order = __order(ingredients= created_ingredients,beverages =created_beverages, size= created_sizes, client_data= client_data)
    created_order, _ = OrderController.create(order= order)
    order_from_db, error = OrderController.get_by_id(_id= created_order['_id'])
    size_id = order.pop('size_id', None)
    ingredient_ids = order.pop('ingredients', [])
    pytest.assume(error is None)
    for param, value in created_order.items():
        pytest.assume(order_from_db[param] == value)
        pytest.assume(size_id == created_order['size']['_id'])

        ingredients_in_detail = set(item['ingredient']['_id'] for item in created_order['detail'])
        pytest.assume(not ingredients_in_detail.difference(ingredient_ids))


def test_get_all(app, ingredients,  beverages, sizes, client_data):
    created_sizes, created_ingredients,created_beverages  = __create_beverages_sizes_and_ingredients(ingredients= ingredients, sizes= sizes, beverages= beverages)
    created_orders = []
    for _ in range(5):
        order = __order(ingredients= shuffle_list(created_ingredients)[:3], beverages = shuffle_list(created_beverages)[:3], size= get_random_choice(created_sizes), client_data= client_data)
        created_order, _ = OrderController.create(order= order)
        created_orders.append(created_order)

    orders_from_db, error = OrderController.get_all()
    searchable_orders = {db_order['_id']: db_order for db_order in orders_from_db}
    pytest.assume(error is None)
    for created_order in created_orders:
        current_id = created_order['_id']
        assert current_id in searchable_orders
        for param, value in created_order.items():
            pytest.assume(searchable_orders[current_id][param] == value)
