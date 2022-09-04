import json
import random, requests

from app.test.utils.functions import (get_random_phone, get_random_sequence)

names = ["Jorge Salinas", "Carlos Martinez", "Pedro Perez", "Luis Rodriguez", "Amaranto Lopez", "Andres Parra", 
"Alejandra Zinisterra", "Caroline Verjel", "Rosilveris Carrillo", "Judit Perez", "Daniela Alvarez", "Leidy Molina",
"Katty Hoyos", "Edgardo Mojica", "Andrea Torres", "Ramiro Ranauro", "Andres Garrido", "Ted Mosby", "Barney Steanson",
"David Verjel"]

addresses = ["Avenue "+str(i)+"th" for i in range(1,21)]

beverages = [i for i in range(1,8)]
ingredients = [i for i in range(1,8)]

order_url = "http://127.0.0.1:5000/order/"

client_info=[]
orders = []

for i in range(1,20):
    client_info.append(
        {
            i:{
        "client_address":random.choice(addresses),
        "client_dni":get_random_sequence(),
        "client_name":random.choice(names),
        "client_phone":get_random_phone(),
            }
        }
    )
    names.remove(client_info[i-1][i]["client_name"])
    addresses.remove(client_info[i-1][i]["client_address"])

for i in range(1,101):
    random_index = (random.randrange(1,20))
    data = {
            **client_info[random_index-1][random_index],
            "ingredients":random.choices(ingredients, k=random.randrange(1,7)),
            "size_id" : random.randrange(1,4),
            "beverages": random.choices(beverages, k=random.randrange(1,6))
        }
    create_order = requests.post(order_url, json=data)
    json_response = json.loads(create_order.text)
