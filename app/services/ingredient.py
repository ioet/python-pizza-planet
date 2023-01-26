from app.common.http_methods import GET, POST, PUT
from flask import Blueprint
from app.controllers.controller_factory import ControllerFactory
from app.services.service import Service

ingredient = Blueprint('ingredient', __name__)
controller = ControllerFactory.get_controller('ingredient')

@ingredient.route('/', methods=POST)
def create_ingredient():
    return Service.create(controller= controller)


@ingredient.route('/', methods=PUT)
def update_ingredient():
    return Service.update(controller= controller)


@ingredient.route('/id/<_id>', methods=GET)
def get_ingredient_by_id(_id: int):
    return Service.get_by_id(_id= _id ,controller= controller)


@ingredient.route('/', methods=GET)
def get_ingredients():
    return Service.get_all(controller= controller)