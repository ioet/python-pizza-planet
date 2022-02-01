from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, jsonify, request

from ..controllers import IngredientController

ingredient = Blueprint('ingredient', __name__)


@ingredient.route('/', methods=POST)
def create_ingredient():
    ingredient, error = IngredientController.create(request.json)
    response = ingredient if not error else {'error': error}
    status_code = 200 if not error else 400
    return jsonify(response), status_code


@ingredient.route('/', methods=PUT)
def update_ingredient():
    ingredient, error = IngredientController.update(request.json)
    response = ingredient if not error else {'error': error}
    status_code = 200 if not error else 400
    return jsonify(response), status_code


@ingredient.route('/id/<_id>', methods=GET)
def get_ingredient_by_id(_id: int):
    ingredient, error = IngredientController.get_by_id(_id)
    response = ingredient if not error else {'error': error}
    status_code = 200 if ingredient else 404 if not error else 400
    return jsonify(response), status_code


@ingredient.route('/', methods=GET)
def get_ingredients():
    ingredients, error = IngredientController.get_all()
    response = ingredients if not error else {'error': error}
    status_code = 200 if ingredients else 404 if not error else 400
    return jsonify(response), status_code
