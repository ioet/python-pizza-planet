from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request

from ..controllers import IngredientController
from ..common.utils import instance_controller

ingredient = Blueprint('ingredient', __name__)

@ingredient.route('/', methods=POST)
def create_ingredient():
    return instance_controller(IngredientController.create(request.json))

@ingredient.route('/', methods=PUT)
def update_ingredient():
    return instance_controller(IngredientController.update(request.json))

@ingredient.route('/id/<_id>', methods=GET)
def get_ingredient_by_id(_id: int):
    return instance_controller(IngredientController.get_by_id(_id))

@ingredient.route('/', methods=GET)
def get_ingredients():
    return instance_controller(IngredientController.get_all())