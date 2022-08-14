import random
from traceback import print_tb
from faker import Faker
from faker_food import FoodProvider

import sqlite3


def insert_data(table_name, data):
    conn = sqlite3.connect('pizza.sqlite')
    c = conn.cursor()
    c.execute("INSERT INTO {} VALUES ({})".format(table_name, data))
    conn.commit()
    conn.close()


def seed_beverages(count):
    fake = Faker()
    fake.add_provider(FoodProvider)
    for i in range(count):
        random_price = random.randint(1, 10)
        insert_data('beverage', str(20+i)+",'" +
                    fake.spice()+"'," + str(random_price))


def seed_ingredients(count):
    fake = Faker()
    fake.add_provider(FoodProvider)
    for i in range(count):
        random_price = random.randint(1, 10)
        insert_data('ingredient', str(20+i)+",'" +
                    fake.ingredient()+"'," + str(random_price))


def seed_size(count):
    fake = Faker()
    fake.add_provider(FoodProvider)
    for i in range(count):
        random_price = random.randint(1, 30)
        insert_data('size',str(20+i)+",'"+ fake.ethnic_category()+"',"+ str(random_price))

seed_beverages(15)
seed_ingredients(15)
seed_size(5)