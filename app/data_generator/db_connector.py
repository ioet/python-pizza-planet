import sqlite3
from random import randint

conn = sqlite3.connect('C:\ioet\python-pizza-planet\pizza.sqlite')
cur = conn.cursor()


def insert_data(table: str, columns: str, values: list):    
    with conn:
        try:
            cur.execute(f'INSERT INTO {table} ({columns}) VALUES (?,?);', values) 
        except :
            return False


def insert_order(name):  
    with conn:
        size = get_size(randint(13,16)) 
        try:
            values = (name, 1232, 'c24 #3', '555-555-5555', f'2022-{randint(1,9)}-{randint(1,28)} 00:00:00.0', size[0][2], size[0][0])
            cur.execute('INSERT INTO "order" (client_name, client_dni, client_address, client_phone, date, total_price, size_id) VALUES (?,?,?,?,?,?,?);', values)
        except sqlite3.Error as e:
            return e


def insert_order_detail(table: str, columns: str, values: list):
    with conn:
        try:
            orders = cur.execute(f'SELECT * FROM "order"') 
            # cur.execute(f'INSERT INTO {table} ({columns}) VALUES (?,?,?);', values) 
            for i in orders:
                print(i)
        except :
            return False


def get_size(size_id):
    res = cur.execute(f'SELECT * FROM size WHERE _id = {size_id}')
    return res.fetchall()


def get_ingredient(ingredient_id):
    res = cur.execute(f'SELECT * FROM ingredient WHERE _id = {ingredient_id}')
    return res.fetchall()


def get_orders(order_id):
    res = cur.execute(f'SELECT * FROM "order" WHERE _id = {order_id}')
    return res.fetchall()

conn.commit()   