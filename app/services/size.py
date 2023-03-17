from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request
from app.common.utils import handle_response
from ..controllers import SizeController

size = Blueprint('size', __name__)


@size.route('/', methods=POST)
def create_size():
    size, error = SizeController.create(request.json)
    return handle_response(size, error)


@size.route('/', methods=PUT)
def update_size():
    size, error = SizeController.update(request.json)
    return handle_response(size, error)


@size.route('/id/<_id>', methods=GET)
def get_size_by_id(_id: int):
    size, error = SizeController.get_by_id(_id)
    return handle_response(size, error)


@size.route('/', methods=GET)
def get_size():
    sizes, error = SizeController.get_all()
    return handle_response(sizes, error)
