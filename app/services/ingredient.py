from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request
from app.services.utils.handle import handle_response
from ..controllers import IngredientController

ingredient = Blueprint('ingredient', __name__)


@ingredient.route('/', methods=POST)
def create_ingredient():
    ingredient, error = IngredientController.create(request.json)
    return handle_response(ingredient, error)


@ingredient.route('/', methods=PUT)
def update_ingredient():
    ingredient, error = IngredientController.update(request.json)
    return handle_response(ingredient, error)


@ingredient.route('/id/<_id>', methods=GET)
def get_ingredient_by_id(_id: int):
    ingredient, error = IngredientController.get_by_id(_id)
    return handle_response(ingredient, error)


@ingredient.route('/', methods=GET)
def get_ingredients():
    ingredients, error = IngredientController.get_all()
    return handle_response(ingredients, error)
