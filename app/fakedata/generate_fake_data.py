import random
from faker import Faker
from app.plugins import db
from app.repositories.models import Ingredient, Beverage, Size
from app.repositories.managers import OrderManager
fake = Faker('es_AR')

def generate_fake_sizes():
    sizes = [
        {'name': 'S', 'price': 5.0},
        {'name': 'M', 'price': 7.0},
        {'name': 'L', 'price': 10.0},
        {'name': 'XL', 'price': 12.0},
        {'name': 'XXL', 'price': 15.0},

    ]
    for size in sizes:
        size_name = size['name']
        size_price = size['price']
        size_entry = Size(name=size_name, price=size_price)
        db.session.add(size_entry)
    db.session.commit()

def generate_fake_ingredients():
    ingredients = [
        {'name': 'Cheese', 'price': 3.0},
        {'name': 'Reggianito', 'price': 5.0},
        {'name': 'Mushrooms', 'price': 1},
        {'name': 'Pepperoni', 'price': 2.0},
        {'name': 'Ham', 'price': 2.0},
        {'name': 'Bacon', 'price': 2.0},
        {'name': 'Pineapple', 'price': 2.0},
        {'name': 'Onion', 'price': 1.0},
        {'name': 'Tomato', 'price': 1.0},
        {'name': 'Olives', 'price': 1.0},
    ]
    for ingredient in ingredients:
        ingredient_name = ingredient['name']
        ingredient_price = ingredient['price']
        ingredient_entry = Ingredient(name=ingredient_name, price=ingredient_price)
        db.session.add(ingredient_entry)
    db.session.commit()

def generate_fake_beverages():
    beverages = [
        {'name': 'Coke', 'price': 2.0},
        {'name': 'Sprite', 'price': 2.0},
        {'name': 'Water', 'price': 1.0},
        {'name': 'Fanta', 'price': 2.0},
        {'name': 'Pepsi', 'price': 2.0},
    ]
    for beverage in beverages:
        beverage_entry = Beverage(**beverage)
        db.session.add(beverage_entry)
    db.session.commit()

def generate_fake_orders(num_orders=100, db_session=None):
    if not db_session:
        db_session = db.session

    sizes = Size.query.all()
    ingredients = Ingredient.query.all()
    beverages = Beverage.query.all()

    client_list = []
    for _ in range(30):
        client_list.append(fake.name())

    def get_random_client_from_list():
        return random.choice(client_list)

    for _ in range(num_orders):
        size = random.choice(sizes)
        
        ingredients_quantity = random.randint(1, len(ingredients))
        ingredients_selected = random.sample(ingredients, ingredients_quantity)

        beverage_quantity = random.randint(1, 5)
        beverages_types_amount = random.randint(1, len(beverages))
        beverages_selected = [
            {'_id': b._id, 'price': b.price, 'quantity': beverage_quantity} for b in (random.sample(beverages, beverages_types_amount))
        ]

        total_price = size.price + sum([i.price for i in ingredients_selected]) + sum([b['price'] * b['quantity'] for b in beverages_selected])
        
        order_data = {
            'client_name': get_random_client_from_list(),
            'client_dni': fake.unique.random_number(digits=8, fix_len=True),
            'client_address': fake.address(),
            'client_phone': fake.phone_number(),
            'date': fake.date_time_between(start_date='-1y', end_date='now'),
            'total_price': total_price, 
            'size_id': size._id,
        }

        OrderManager.create(order_data, ingredients_selected, beverages_selected)

def main():
    db.create_all()
    generate_fake_sizes()
    generate_fake_ingredients()
    generate_fake_beverages()
    generate_fake_orders()

if __name__ == '__main__':
    main()