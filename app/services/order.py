from app.common.http_methods import GET, POST
from flask import Blueprint, jsonify, request

from ..common.utils import instance_controller
from ..controllers import OrderController

order = Blueprint('order', __name__)

@order.route('/', methods=POST)
def create_order():
    return instance_controller(OrderController.create(request.json))

@order.route('/id/<_id>', methods=GET)
def get_order_by_id(_id: int):
    return instance_controller(OrderController.get_by_id(_id))

@order.route('/', methods=GET)
def get_orders():
    return instance_controller(OrderController.get_all())

