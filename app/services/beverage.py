from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, jsonify, request

from ..controllers import BeverageController
from .base import *

beverage = Blueprint('beverage', __name__)


@beverage.route('/', methods=POST)
def create_beverage():
    return create_entity(BeverageController)


@beverage.route('/', methods=PUT)
def update_beverage():
    return update_entity(BeverageController)


@beverage.route('/id/<_id>', methods=GET)
def get_beverage_by_id(_id: int):
    return get_entity_by_id(BeverageController, _id)


@beverage.route('/', methods=GET)
def get_beverages():
    return get_all_entities(BeverageController)
