from app.repositories.managers.managers import beverage_manager, ingredient_manager, order_manager, size_manager
from faker import Faker

def ingredients_beverages_sizes_factory():
    fake = Faker()
    min_price_ingredients = 1.0
    max_price_ingredients = 5.0
    min_price_sizes = 5.0
    max_price_sizes = 20.0
    min_price_beverages = 1.0
    max_price_beverages = 5.0

    def factory_price(min_price: float, max_price: float):
        price = fake.pyfloat(
            positive=True,
            min_value=min_price,
            max_value=max_price,
            right_digits=1,
        )
        return price

    ingredients_names = [
        "Cheese",
        "Tomato",
        "Salami",
        "Pepperoni",
        "Olives",
        "Oregano",
        "Shredded",
        "Mozzarella",
        "Pineapple",
        "Ham",
    ]
    ingredients = [{"name": name, "price": factory_price(min_price_ingredients, max_price_ingredients)} for name in ingredients_names]

    ingredients_factory = []

    for ingredient in ingredients:
        ingredients_factory.append(ingredient_manager.create({"name": ingredient["name"], "price": ingredient["price"]}))

    sizes_names = [
        "Personal size",
        "Small",
        "Medium",
        "Big",
        "Family size",
    ]
    sizes = [{"name": name, "price": factory_price(min_price_sizes, max_price_sizes)} for name in sizes_names]

    sizes_factory = []
    for size in sizes:
        sizes_factory.append(size_manager.create({"name": size["name"], "price": size["price"]}))

    beverages_names =  [
        "Cocacola",
        "Pepsi",
        "Fanta",
        "Corona",
        "Paso",
        "Colombiana",
        "Poker",
        "7Up",
        "Quatro",
        "Water",
    ]
    beverages = [{"name": name, "price": factory_price(min_price_beverages, max_price_beverages)} for name in beverages_names]

    beverages_factory = []
    for beverage in beverages:
        beverages_factory.append(beverage_manager.create({"name": beverage["name"], "price": beverage["price"]}))
    
    return ingredients_factory,  beverages_factory, sizes_factory
