from app.common.http_methods import GET, POST
from flask import Blueprint, request

from app.services.base import BaseService

from ..controllers import OrderController

order = Blueprint('order', __name__)

order_base_service = BaseService(entity = "ingredient", 
        entitycontroller = OrderController())
        
@order.route('/', methods=POST)
def create_order():
    return order_base_service.create(request)

@order.route('/id/<_id>', methods=GET)
def get_order_by_id(_id: int):
    return order_base_service.get_by_id(_id)

@order.route('/', methods=GET)
def get_orders():
    return order_base_service.get_all()
