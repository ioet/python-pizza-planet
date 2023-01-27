from random import choices, randrange, sample
from faker import Faker
from datetime import datetime, timedelta

from app.database_seed.constans_seed import MAX_PRICE, MIN_PRICE

from .data import ingredients_seed, sizes_seed, beverages_seed
import random as rand

_fake = Faker()


def _client_mock() -> dict:
    return {
        "client_address": _fake.street_address(),
        "client_dni": str(_fake.random_number(digits=10)),
        "client_name": _fake.name(),
        "client_phone": _fake.phone_number(),
    }


def get_random_price(lower_bound: float, upper_bound: float) -> float:
    return round(rand.uniform(lower_bound, upper_bound), 2)


def calculate_order_price(size_price: float, ingredients: list, beverages: list):
    ingredients_price = sum(ingredient.get("price") for ingredient in ingredients)
    beverages_price = sum(beverage.get("price") for beverage in beverages)
    total_price = size_price + ingredients_price + beverages_price
    return round(total_price, 2)


def generate_random_clients(number_clients: int):
    return [_client_mock() for _ in range(number_clients)]


def generate_random_sublist(items: list, numbers_items: int):
    max_item = rand.randint(1, numbers_items)
    return sample(items, k=max_item)


def generate_random_dates(number_orders):
    start = datetime.strptime("1/1/2022 1:30 PM", "%m/%d/%Y %I:%M %p")
    end = datetime.strptime("1/1/2023 4:50 AM", "%m/%d/%Y %I:%M %p")
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    date = [start + timedelta(seconds=random_second)]
    return choices(date, k=number_orders)


def generate_random_ingredients():
    return [
        {"name": ingredient, "price": get_random_price(MIN_PRICE, MAX_PRICE)}
        for ingredient in ingredients_seed
    ]


def generate_random_beverages():
    return [
        {"name": beverage, "price": get_random_price(MIN_PRICE, MAX_PRICE)}
        for beverage in beverages_seed
    ]


def generate_random_sizes():
    return [
        {"name": size, "price": get_random_price(MIN_PRICE, MAX_PRICE)}
        for size in sizes_seed
    ]
