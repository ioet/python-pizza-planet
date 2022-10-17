from .orders_factory import orders_factory
from app.repositories.managers.managers import beverage_manager, ingredient_manager, order_manager, size_manager
from flask import jsonify

def seeder_factory():

    orders = orders_factory()

    for order in orders:
        order_manager.create_order(order_data=order["order_data"],
        ingredients=order["ingredients"],
        beverages=order["beverages"],
        from_seeder= True
        )

if __name__ == '__main__':
    seeder_factory()