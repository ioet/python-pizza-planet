from app.common.http_methods import GET, POST
from flask import Blueprint, request
from app.common.utils import handle_response
from ..controllers import OrderController

order = Blueprint('order', __name__)


@order.route('/', methods=POST)
def create_order():
    order, error = OrderController.create(request.json)
    return handle_response(order, error)


@order.route('/id/<_id>', methods=GET)
def get_order_by_id(_id: int):
    order, error = OrderController.get_by_id(_id)
    return handle_response(order, error)


@order.route('/', methods=GET)
def get_orders():
    orders, error = OrderController.get_all()
    return handle_response(orders, error)
