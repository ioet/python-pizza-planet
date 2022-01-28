from app.common.http_methods import GET, POST
from flask import Blueprint

order = Blueprint('order', __name__)


@order.route('/', methods=POST)
def create_order():
    pass


@order.route('/id/<_id>', methods=GET)
def get_order_by_id(_id: int):
    pass


@order.route('/', methods=GET)
def get_orders():
    pass
