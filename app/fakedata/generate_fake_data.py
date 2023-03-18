import random
from datetime import timedelta
from faker import Faker
from app.plugins import db
from app.repositories.models import Order, IngredientDetail, BeveragesDetail, Ingredient, Beverage, Size
from app.repositories.managers import OrderManager
fake = Faker()

def generate_fake_sizes():
    sizes = [
        {'name': 'S', 'price': 5.0},
        {'name': 'M', 'price': 7.0},
        {'name': 'L', 'price': 10.0},
    ]
    for size in sizes:
        size_entry = Size(**size)
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
    ]
    for ingredient in ingredients:
        ingredient_entry = Ingredient(**ingredient)
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

    for _ in range(num_orders):
        size = random.choice(sizes)
        selected_ingredients = random.sample(ingredients, random.randint(1, len(ingredients)))
        selected_beverages = [{'_id': b._id, 'price': b.price, 'quantity': random.randint(1, 5)} for b in random.sample(beverages, random.randint(1, len(beverages)))]

        total_price = size.price + sum([i.price for i in selected_ingredients]) + sum([b['price'] * b['quantity'] for b in selected_beverages])

        order_data = {
            'client_name': fake.name(),
            'client_dni': fake.unique.random_number(digits=10, fix_len=True),
            'client_address': fake.address(),
            'client_phone': fake.phone_number(),
            'date': fake.date_time_this_year(),
            'total_price': total_price, 
            'size_id': size._id,
        }

        OrderManager.create(order_data, selected_ingredients, selected_beverages)

def main():
    db.create_all()
    generate_fake_sizes()
    generate_fake_ingredients()
    generate_fake_beverages()
    generate_fake_orders()

if __name__ == '__main__':
    main()