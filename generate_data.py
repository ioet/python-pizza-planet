import sqlite3
from app.test.utils.functions import *
import random
import datetime
from faker import Faker
fake = Faker()

conn = sqlite3.connect('pizza.sqlite')

cursor = conn.cursor()


def product(id, product_tag):
    return (id, f'{product_tag}-{get_random_string()}', get_random_price(10, 20))


def get_last_id(cursor, table_name):
    cursor.execute(f'''SELECT MAX(_id) FROM "{table_name}";''')
    id = cursor.fetchone()[0]
    return 0 if id == None else id


def insert_ingredients(cursor, quantity):
    insert_data_query = 'INSERT INTO ingredient VALUES (?, ?, ?)'
    id = get_last_id(cursor, 'ingredient') + 1
    ingredients = [product(i, 'ing') for i in range (id, id + quantity)]
    cursor.executemany(insert_data_query, ingredients)
    conn.commit()
    return ingredients


def insert_sizes(cursor, quantity):
    insert_data_query = 'INSERT INTO size VALUES (?, ?, ?)'
    id = get_last_id(cursor, 'size') + 1
    sizes = [product(i, 'siz') for i in range (id, id + quantity)]
    cursor.executemany(insert_data_query, sizes)
    conn.commit()
    return sizes


def insert_beverages(cursor, quantity):
    insert_data_query = 'INSERT INTO beverage VALUES (?, ?, ?)'
    id = get_last_id(cursor, 'beverage') + 1
    beverages = [product(i, 'bev') for i in range (id, id + quantity)]
    cursor.executemany(insert_data_query, beverages)
    conn.commit()
    return beverages


def insert_orders(cursor, orders):
    insert_data_query = 'INSERT INTO "order" VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
    cursor.executemany(insert_data_query, orders)
    conn.commit()


def insert_orders_detail(cursor, orders_detail):
    insert_data_query = 'INSERT INTO "order_detail" VALUES (?, ?, ?, ?)'
    cursor.executemany(insert_data_query, orders_detail)
    conn.commit()


def insert_orders_beverage(cursor, orders_beverage):
    insert_data_query = 'INSERT INTO "order_beverage" VALUES (?, ?, ?, ?)'
    cursor.executemany(insert_data_query, orders_beverage)
    conn.commit()


def random_datetime():
    start_date = '2022-01-01 00:00:00'
    end_date = '2022-12-31 23:59:59'

    start_timestamp = datetime.datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S').timestamp()
    end_timestamp = datetime.datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S').timestamp()
    random_timestamp = random.uniform(start_timestamp, end_timestamp)
    random_datetime = datetime.datetime.fromtimestamp(random_timestamp)
    microseconds = random.randint(0, 999999)
    random_datetime = random_datetime.replace(microsecond=microseconds)
    return random_datetime.strftime('%Y-%m-%d %H:%M:%S.%f')


def client_info():
    return {
        'name': fake.unique.name(),
        'dni': get_random_sequence(),
        'address': fake.address(),
        'phone': get_random_sequence()
    }


def create_clients(quantity):
    clients = [client_info() for _ in range(quantity)]
    fake.unique.clear()
    return clients


def calculate_order_price(size, ingredients, beverages):
    ingredients_total = sum(ingredient[2] for ingredient in ingredients)
    beverages_total = sum(beverage[2] for beverage in beverages)
    price = size[2] + ingredients_total + beverages_total
    return round(price, 2)


def create_insert_orders(cursor, created_ingredients, created_sizes, created_beverages, clients, quantity):
    orders_to_save = []
    orders_detail_to_save = []
    orders_beverage_to_save = []

    order_id = get_last_id(cursor, 'order') + 1
    order_detail_id = get_last_id(cursor, 'order_detail') + 1
    order_beverage_id = get_last_id(cursor, 'order_beverage') + 1

    for _ in range(quantity):
        size = shuffle_list(created_sizes)[0]
        client = shuffle_list(clients)[0]
        date = random_datetime()

        ingredients_quant =  random.randint(0, len(created_ingredients))
        ingredients = shuffle_list(created_ingredients)[:ingredients_quant]

        beverages_quant =  random.randint(0, len(created_ingredients))
        beverages = shuffle_list(created_beverages)[:beverages_quant]

        order_price = calculate_order_price(size, ingredients, beverages)
        order_to_save = (order_id, client["name"], client["dni"], client["address"], client["phone"], date, order_price, size[0])
        orders_to_save.append(order_to_save)

        for ingredient in ingredients:
            order_detail_to_save = (order_detail_id, ingredient[2], order_id, ingredient[0])
            orders_detail_to_save.append(order_detail_to_save)
            order_detail_id += 1

        for beverage in beverages:
            order_beverage_to_save = (order_beverage_id, beverage[2], order_id, beverage[0])
            orders_beverage_to_save.append(order_beverage_to_save)
            order_beverage_id += 1

        order_id +=1

    insert_orders(cursor, orders_to_save)
    insert_orders_detail(cursor, orders_detail_to_save)
    insert_orders_beverage(cursor, orders_beverage_to_save)


created_ingredients = insert_ingredients(cursor, 10)
created_beverages = insert_beverages(cursor, 10)
created_sizes = insert_sizes(cursor, 5)
clients = create_clients(random.randint(15, 30))
create_insert_orders(cursor, created_ingredients, created_sizes, created_beverages, clients, 100)


conn.close()