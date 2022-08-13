from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, jsonify, request

from ..controllers import IngredientController
from .base import *

ingredient = Blueprint('ingredient', __name__)


@ingredient.route('/', methods=POST)
def create_ingredient():
    return create_entity(IngredientController)


@ingredient.route('/', methods=PUT)
def update_ingredient():
    return update_entity(IngredientController)


@ingredient.route('/id/<_id>', methods=GET)
def get_ingredient_by_id(_id: int):
    return get_entity_by_id(IngredientController, _id)


@ingredient.route('/', methods=GET)
def get_ingredients():
    return get_all_entities(IngredientController)
