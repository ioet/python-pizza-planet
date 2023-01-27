from app.database_seed.constans_seed import (
    NUMBERS_CLIENTS,
    NUMBERS_DATES,
)
from app.database_seed.seed_manager import (
    seed_beverages, 
    seed_ingredients, 
    seed_orders, 
    seed_sizes
)

from app.database_seed.seed_utils import (
    generate_random_beverages,
    generate_random_clients,
    generate_random_dates,
    generate_random_ingredients,
    generate_random_sizes,
)

from app.repositories.managers import (
    SizeManager,
    IngredientManager,
    BeverageManager,
)

_seed_sizes = generate_random_sizes()
_seed_ingredients = generate_random_ingredients()
_seed_beverages = generate_random_beverages()
_see_dates = generate_random_dates(NUMBERS_DATES)
_seed_clients = generate_random_clients(NUMBERS_CLIENTS)

def seed_database():
    seed_sizes(sizes=_seed_sizes)
    seed_ingredients(ingredients=_seed_ingredients)
    seed_beverages(beverages=_seed_beverages)

    sizes = SizeManager.get_all()
    ingredients = IngredientManager.get_all()
    beverages = BeverageManager.get_all()

    seed_orders(
        dates=_see_dates,
        sizes=sizes,
        beverages=beverages,
        ingredients=ingredients,
        clients=_seed_clients,
    )
