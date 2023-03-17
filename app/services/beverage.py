from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request
from ..controllers import BeverageController
from app.services.utils.handle import handle_response

beverage = Blueprint('beverage', __name__)

@beverage.route('/', methods=POST)
def create_beverage():
    beverage, error = BeverageController.create(request.json)
    return handle_response(beverage, error)


@beverage.route('/', methods=PUT)
def update_beverage():
    beverage, error = BeverageController.update(request.json)
    return handle_response(beverage, error)


@beverage.route('/id/<_id>', methods=GET)
def get_beverage_by_id(_id: int):
    beverage, error = BeverageController.get_by_id(_id)
    return handle_response(beverage, error)


@beverage.route('/', methods=GET)
def get_beverages():
    beverages, error = BeverageController.get_all()
    return handle_response(beverages, error)
