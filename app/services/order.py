from app.common.http_methods import GET, POST
from flask import Blueprint, jsonify, request

from ..controllers import OrderController

order = Blueprint('order', __name__)


@order.route('/', methods=POST)
def create_order():
    order, error = OrderController.create(request.json)
    response = order if not error else {'error': error}
    status_code = 200 if not error else 400
    return jsonify(response), status_code


@order.route('/id/<_id>', methods=GET)
def get_order_by_id(_id: int):
    order, error = OrderController.get_by_id(_id)
    response = order if not error else {'error': error}
    status_code = 200 if order else 404 if not error else 400
    return jsonify(response), status_code


@order.route('/', methods=GET)
def get_orders():
    orders, error = OrderController.get_all()
    response = orders if not error else {'error': error}
    status_code = 200 if orders else 404 if not error else 400
    return jsonify(response), status_code
