from flask import Blueprint, jsonify
from app.common.http_methods import GET, POST
from .base_service import BaseService
from ..controllers import OrderController

order = Blueprint('order', __name__)
order_service = BaseService(entity_controller=OrderController)


@order.route("/", methods=POST)
def create_order():
    return order_service.create()


@order.route('/id/<_id>', methods=GET)
def get_order_by_id(_id: int):
    return order_service.get_by_id(_id)


@order.route("/", methods=GET)
def get_orders():
    entity, error = OrderController.get_all()
    response = entity if not error else {'error': error}
    status_code = 200 if not error else 400
    return jsonify(response), status_code
