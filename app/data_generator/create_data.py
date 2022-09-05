from random import randint
from app.controllers.order import OrderController

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

    for round in range(1):
        order = {
            "client_address": "c 12 #36",
            "client_dni": "1234",
            "client_name": names[randint(1,15)],
            "client_phone": "555-555-5555",
            "ingredients": [
                randint(1,10)
            ],
            "size_id": randint(13,17)
        }
        print(OrderController.create(order))


if __name__ == '__main__':
    main()
