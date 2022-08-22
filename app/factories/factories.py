import random
from faker import Faker
from ..repositories.models import  Order, OrderDetail, Size, Ingredient, Beverage, db

PIZZA_SIZES = ["Small", "Medium", "Personal", "Large"]
PIZZA_INGREDIENTS = ["Tomatoes", "Onion", "Cheese", "Sausage", "Pepper", "Salami", "Olives"]
BEVERAGES = ["Coca-cola", "Fanta", "Inca-cola", "Orange", "Pepsi", "Fiora"]

fake = Faker()
def fill_data_base():
    db.session()
    factory_sizes = [
        Size(
            name = _size,
            price = fake.pyfloat(left_digits=2, right_digits=2, positive=True)
        ) for _index, _size in enumerate(PIZZA_SIZES)
    ]
    db.session.add_all(factory_sizes)

    
    factory_ingredients = [
        Ingredient(
            name = _ingredient,
            price = fake.pyfloat(left_digits=2, right_digits=2, positive=True)
        ) for _index, _ingredient in enumerate(PIZZA_INGREDIENTS)
    ]
    db.session.add_all(factory_ingredients)

    factory_beverages = [
        Beverage(
            name = _beverage,
            price = fake.pyfloat(left_digits=2, right_digits=2, positive=True)
        ) for _index, _beverage in enumerate(BEVERAGES)
    ]
    db.session.add_all(factory_beverages)

    fake_orders = [
        Order(
            _id=_idx+1,
            client_name=fake.name(),
            client_dni=fake.pyint(),
            client_address=fake.address(),
            client_phone=fake.phone_number(),
            date=fake.date_time_ad(),
            total_price=fake.pyint(),
            size_id=random.randint(1, len(PIZZA_SIZES)),
        ) for _idx in range(50)
    ]
    db.session.add_all(fake_orders)
    db.session.flush()
    fake_order_ingredients = [
        OrderDetail(
            order_id=order._id,
            ingredient_price=_ingredient.price,
            ingredient_id=_ingredient._id
        ) for _index in range(3) 
          for _ingredient in [factory_ingredients[random.randint(0, len(PIZZA_SIZES))]]
          for order in fake_orders
    ]
    db.session.add_all(fake_order_ingredients)
    db.session.commit()

