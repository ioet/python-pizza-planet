import pytest
from app.controllers import IngredientController


def test_create(app, ingredient: dict):
    created_ingredient, error = IngredientController.create(ingredient)
    assert error is None
    for param, value in ingredient.items():
        assert param in created_ingredient
        assert value == created_ingredient[param]
        assert created_ingredient['_id']


def test_update(app, ingredient: dict):
    created_ingredient, _ = IngredientController.create(ingredient)
    updated_fields = {
        'name': 'updated',
        'price': 10
    }
    updated_ingredient, error = IngredientController.update({
        '_id': created_ingredient['_id'],
        **updated_fields
    })
    assert error is None
    ingredient_from_database, error = IngredientController.get_by_id(created_ingredient['_id'])
    assert error is None
    for param, value in updated_fields.items():
        assert updated_ingredient[param] == value
        assert ingredient_from_database[param] == value

def test_get_by_id(app, ingredient: dict):
    created_ingredient, _ = IngredientController.create(ingredient)
    ingredient_from_db, error = IngredientController.get_by_id(created_ingredient['_id'])
    assert error is None
    for param, value in created_ingredient.items():
        assert ingredient_from_db[param] == value


def test_get_all(app, ingredients: list):
    created_ingredients = []
    for ingredient in ingredients:
        created_ingredient, _ = IngredientController.create(ingredient)
        created_ingredients.append(created_ingredient)

    ingredients_from_db, error = IngredientController.get_all()
    searchable_ingredients = {db_ingredient['_id']: db_ingredient for db_ingredient in ingredients_from_db}
    assert error is None
    for created_ingredient in created_ingredients:
        current_id = created_ingredient['_id']
        assert current_id in searchable_ingredients
        for param, value in created_ingredient.items():
            assert searchable_ingredients[current_id][param] == value