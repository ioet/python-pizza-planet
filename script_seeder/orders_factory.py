from datetime import datetime
from random import randrange
from .ingredients_beverages_sizes_factory import ingredients_beverages_sizes_factory
from .clients_factory import clients_factory

from faker import Faker

fake = Faker()

def orders_factory():

    clients = clients_factory()
    ingredients, beverages, sizes = ingredients_beverages_sizes_factory()

    def calculate_order_price(size_price: float, ingredients: list, beverages: list):
            ingredient_price = sum(ingredient["price"] for ingredient in ingredients)
            beverages_price = sum(beverage["price"] for beverage in beverages)
            price = ingredient_price + beverages_price  + size_price
            return round(price, 2)

    orders = []
    for client in clients:
        for _ in range(randrange(1, 10)):
            ingredients_order = [ingredients[randrange(0, len(ingredients) - 1)] for _ in range(randrange(1, 8))]
            beverages_order = [beverages[randrange(0, len(beverages) - 1)] for _ in range(randrange(1, 4))]
            index_size = randrange(0, len(sizes) - 1)
            size_order = sizes[index_size]
            price_order = calculate_order_price(size_order["price"], ingredients_order, beverages_order)
            date_order =  fake.date_time_between(
                start_date = datetime(2022, 6, 6),
                end_date = datetime.now()
            )
            orders.append({
                "order_data" : {**client, "size_id": size_order["_id"], "total_price": price_order, "date": date_order},
                "ingredients" : ingredients_order,
                "beverages" : beverages_order,
                })
    return orders