import json
import random
from urllib import response
from faker import Faker
from faker_food import FoodProvider
import requests
import csv


url = 'http://127.0.0.1:5000/order/'
data_clients = []

with open('seeders\clients.csv',"r",encoding="utf-8-sig") as File:
    reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    data_clients = list(reader)


def seed_order(count):
    fake = Faker()
    fake.add_provider(FoodProvider)
    for _ in range(count):
        random_client = data_clients[random.randint(0, len(data_clients)-1)]
        random_date = fake.date_time_between(
            start_date='-1y', end_date='now', tzinfo=None)
        order = {
            "client_name": random_client[0],
            "client_dni": random_client[1],
            "client_address": random_client[2],
            "client_phone": random_client[3],
            "date": str(random_date),
            "size_id": str(random.randint(20, 24)),
            "ingredients": [
                str(random.randint(20, 35)),
                str(random.randint(20, 35)),
                str(random.randint(20, 35))
            ],
            "beverages": [
                str(random.randint(20, 35)),
                str(random.randint(20, 35)),
            ]
        }
        response = requests.post(url, json=order)
        print(response.text)


seed_order(50)


