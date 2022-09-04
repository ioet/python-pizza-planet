from app.data_generator.db_connector import insert_data, insert_order, insert_order_detail
from app.data_generator.db_connector import get_ingredient, get_size
from tqdm import tqdm
from app.data_generator.data_generator import CustomerGenerator
from app.test.utils.functions import *
from datetime import datetime
from random import randint
from tqdm import tqdm

def main():

    sizes = [('Mini', '5.0'), ('Small', '7.0'), ('Medium', '12.0'), ('XBIG', '17')]
    Ingredients = [('Mushrooms', '5.0'), ('Veggie ', '7.0'), ('Double cheese', '7.0'), ('Triple cheese', '10.0'), ('Special', '10.0'), ('Super special', '15.0'), ('Ham', '5.0')]

    # for item_to_create in tqdm(sizes):
    #     name, price = item_to_create
    #     insert_data('size', 'name, price', [name, price])

    # for item_to_create in tqdm(Ingredients):
    #     name, price = item_to_create
    #     insert_data('ingredient', 'name, price', [name, price])


    names = [
        'Aagaard Ally',
        'Abadi Alex',
        'Abbatiello Nicole', 
        'Abbott Elizabeth', 
        'Abbott Bryce',
        'Abella Daniela',
        'Abraham Jacob',
        'Acevedo Nicholas', 
        'Acevedo Zoe', 
        'Adam Marie', 
        'Adam June', 
        'Adams Ann', 
        'Adams Paul', 
        'Adams Tiana', 
        'Adams Samuel',
        'Adams Marie', 
    ]

    customers = []

    for name in names:
        customers.append(
            CustomerGenerator.create_dummy_data(
            customer_name = name,
            customer_dni = get_random_sequence(),
            customer_address = get_random_string(),
            customer_phone = get_random_sequence()
            )
        )
        

    def create_orders():
        
        for round in tqdm(range(1)):
            order_owner = customers[randint(1,15)]
            ingredient = get_ingredient(randint(1,10))
            size = get_size(randint(13,17))

            insert_order(
                '"order"', 
                'client_name,  client_dni, client_address, client_phone, date, total_price, size_id', 
                ['John', '1234', 'c7# 22', '555-555-5556', '2022-02-22 00:00:00.0', '15.0', '14']
            )
    create_orders()

if __name__ == '__main__':
    main()