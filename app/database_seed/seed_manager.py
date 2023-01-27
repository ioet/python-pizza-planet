import random
from .constans_seed import (
    NUMBERS_BEVERAGES,
    NUMBERS_INGREDIENTS,
    NUMBERS_ORDERS,
)

from .seed_utils import (
    calculate_order_price,
    generate_random_sublist
)

from app.repositories.managers import (
    SizeManager,
    IngredientManager,
    BeverageManager,
    OrderManager,
)


def seed_beverages(beverages: list):
    for beverage in beverages:
        BeverageManager.create(beverage)


def seed_ingredients(ingredients: list):
    for ingredient in ingredients:
            IngredientManager.create(ingredient)


def seed_sizes(sizes: list):
    for size in sizes:
        SizeManager.create(size)


def seed_orders(
    dates: list, sizes: list, beverages: list, ingredients: list, clients: list
):
    for _ in range(NUMBERS_ORDERS):
        client_data = random.choice(clients)
        size_order = random.choice(sizes)
        ingredients_order = generate_random_sublist(ingredients, NUMBERS_INGREDIENTS)
        beverages_order = generate_random_sublist(beverages, NUMBERS_BEVERAGES)
        
        total_price = calculate_order_price(
            ingredients=ingredients_order,
            beverages=beverages_order,
            size_price=size_order.get("price"),
        )
        
        order = client_data | {
            "date": random.choice(dates),
            "size_id": size_order.get("_id"),
            "total_price": total_price,
        }

        ingredients_ = IngredientManager.get_by_id_list(
            [ingredient.get('_id') for ingredient in ingredients_order]
        )
        beverages_ = BeverageManager.get_by_id_list(
            [beverage.get('_id') for beverage in beverages_order]
        )
        
        OrderManager.create(
            order_data=order,
            ingredients=ingredients_,
            beverages=beverages_,
        )
      
