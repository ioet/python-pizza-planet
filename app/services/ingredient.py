from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request

from app.services.base import BaseService

from ..controllers import IngredientController

ingredient = Blueprint('ingredient', __name__)

ingredient_base_service = BaseService(entity = "ingredient", 
        entitycontroller = IngredientController())

@ingredient.route('/', methods=POST)
def create_ingredient():
    return ingredient_base_service.create(request)

@ingredient.route('/', methods=PUT)
def update_ingredient():
    return ingredient_base_service.update(request)


@ingredient.route('/id/<_id>', methods=GET)
def get_ingredient_by_id(_id: int):
    return ingredient_base_service.get_by_id(_id)


@ingredient.route('/', methods=GET)
def get_ingredients():
    return ingredient_base_service.get_all()
    