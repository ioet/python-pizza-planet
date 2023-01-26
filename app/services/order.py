from app.common.http_methods import GET, POST
from flask import Blueprint, jsonify, request

from app.services.service import Service

from ..controllers.controller_factory import ControllerFactory

order = Blueprint('order', __name__)
controller = ControllerFactory.get_controller('order')


@order.route('/', methods=POST)
def create_order():
    return Service.create(controller= controller)


@order.route('/id/<_id>', methods=GET)
def get_order_by_id(_id: int):
    return Service.get_by_id(_id= _id ,controller= controller)


@order.route('/', methods=GET)
def get_orders():
    return Service.get_all(controller= controller)
