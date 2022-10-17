from app.repositories.managers.managers import beverage_manager, ingredient_manager, order_manager, size_manager

def ingredients_beverages_sizes_factory():

    ingredients = [
        {"name": "Cheese", "price": 1.0},
        {"name": "Tomato sauce", "price": 1.0},
        {"name": "Salami", "price": 3.0},
        {"name": "Pepperoni", "price": 3.0},
        {"name": "Olives", "price": 4.0},
        {"name": "Oregano", "price": 2.0},
        {"name": "Shredded chicken", "price": 5.0},
        {"name": "Mozzarella cheese", "price": 2.0},
        {"name": "Pineapple", "price": 1.0},
        {"name": "Ham", "price": 2.0}
    ]

    ingredients_factory = []
    for ingredient in ingredients:
        ingredients_factory.append(ingredient_manager.create({"name": ingredient["name"], "price": ingredient["price"]}))
        
    sizes = [
        {"name": "Personal size", "price": 2.0},
        {"name": "Small", "price": 5.0},
        {"name": "Medium", "price": 8.0},
        {"name": "Big", "price": 15.0},
        {"name": "Family size", "price": 20.0}
    ]
    sizes_factory = []
    for size in sizes:
        sizes_factory.append(size_manager.create({"name": size["name"], "price": size["price"]}))

    beverages = [
        {"name": "Cocacola", "price": 1.0},
        {"name": "Pepsi", "price": 1.0},
        {"name": "Fanta", "price": 1.0},
        {"name": "Corona Beer", "price": 2.0},
        {"name": "Paso de los toros", "price": 1.0},
        {"name": "Colombiana", "price": 1.0},
        {"name": "Poker Beer", "price": 2.0},
        {"name": "7Up", "price": 1.0},
        {"name": "Quatro", "price": 1.0},
        {"name": "Water", "price": 1.0}
    ]

    beverages_factory = []
    for beverage in beverages:
        beverages_factory.append(beverage_manager.create({"name": beverage["name"], "price": beverage["price"]}))
    
    return ingredients_factory,  beverages_factory, sizes_factory
