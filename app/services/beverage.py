from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, jsonify, request

from ..controllers import BeverageController
from ..common.utils import instance_controller

beverage = Blueprint('beverage', __name__)

@beverage.route('/', methods=POST)
def create_beverage():
    return instance_controller(BeverageController.create(request.json))

@beverage.route('/', methods=PUT)
def update_beverage():
    return instance_controller(BeverageController.update(request.json))

@beverage.route('/id/<_id>', methods=GET)
def get_beverage_by_id(_id: int):
    return instance_controller(BeverageController.get_by_id(_id))

@beverage.route('/', methods=GET)
def get_beverages():
    return instance_controller(BeverageController.get_all())
