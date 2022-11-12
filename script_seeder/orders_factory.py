from datetime import datetime
from random import randrange
from .ingredients_beverages_sizes_factory import ingredients_beverages_sizes_factory
from .clients_factory import clients_factory

from faker import Faker


def orders_factory():

    fake = Faker()
    clients = clients_factory()
    ingredients, beverages, sizes = ingredients_beverages_sizes_factory()
    min_number_orders = 1
    min_number_ingredients = 1
    min_number_beverages = 1
    max_number_orders = 10
    max_number_ingredients = 8
    max_number_beverages = 4
    start_date = datetime(2022, 6, 6)
    end_date = datetime.now()
    def calculate_order_price(size_price: float, ingredients: list, beverages: list):
            ingredient_price = sum(ingredient["price"] for ingredient in ingredients)
            beverages_price = sum(beverage["price"] for beverage in beverages)
            price = ingredient_price + beverages_price  + size_price
            return round(price, 2)

    orders = []
    for client in clients:
        for _ in range(randrange(min_number_orders, max_number_orders)):
            ingredients_order = [ingredients[randrange(0, len(ingredients) - 1)] for _ in range(randrange(min_number_ingredients, max_number_ingredients))]
            beverages_order = [beverages[randrange(0, len(beverages) - 1)] for _ in range(randrange(min_number_beverages, max_number_beverages))]
            index_size = randrange(0, len(sizes) - 1)
            size_order = sizes[index_size]
            price_order = calculate_order_price(size_order["price"], ingredients_order, beverages_order)
            date_order =  fake.date_time_between(
                start_date = start_date,
                end_date = end_date
            )
            orders.append({
                "order_data" : {**client, "size_id": size_order["_id"], "total_price": price_order, "date": date_order},
                "ingredients" : ingredients_order,
                "beverages" : beverages_order,
                })
    return orders