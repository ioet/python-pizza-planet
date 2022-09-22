from app.controllers.base import BaseController
from app.test.utils.functions import get_random_choice, get_random_sample, get_random_quantity
from app.controllers import IngredientController, SizeController, BeverageController


def create_items(items: list, controller: BaseController):
    created_items = []
    for item in items:
        created_item, _ = controller.create(item)
        created_items.append(created_item)
    return created_items


def create_sizes_and_ingredients(ingredients: list, sizes: list):
    created_ingredients = create_items(ingredients, IngredientController)
    created_sizes = create_items(sizes, SizeController)
    return created_sizes if len(created_sizes) > 1 else created_sizes.pop(), created_ingredients


def create_beverages(b: list):
    created_beverages = create_items(b, BeverageController)
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


def generate_order(created_ingredients, created_sizes, created_beverages, client_data):
    order_pizzas = [__random_pizza(created_ingredients, created_sizes) for _ in range(get_random_quantity())]
    order_beverages = get_random_sample(created_beverages, get_random_quantity(0, len(created_beverages)))
    details = [{'product': __product(p), 'quantity': get_random_quantity()} for p in order_pizzas]
    details.extend([{'product': __product(b), 'quantity': get_random_quantity()} for b in order_beverages])
    return {
        **client_data,
        'details': details
    }


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


def compare_orders(order_data, created_order_data):
    created_details = [__detail_from_created(d) for d in created_order_data.get('details')]
    order_details = order_data.get('details')
    for fieldname in ("client_name", "client_dni", "client_address", "client_phone"):
        if order_data[fieldname] != created_order_data[fieldname]:
            return False
    for created_detail in created_details:
        if not created_detail in order_details:
            return False
    for order_detail in order_details:
        if not order_detail in created_details:
            return False
    return True


def calculate_order_price(order, created_sizes, created_ingredients, created_beverages):
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
    return expected_price
    