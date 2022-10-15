from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request

from ..controllers import SizeController
from ..common.utils import instance_controller

size = Blueprint('size', __name__)

@size.route('/', methods=POST)
def create_size():
    return instance_controller(SizeController.create(request.json))

@size.route('/', methods=PUT)
def update_size():
    return instance_controller(SizeController.update(request.json))

@size.route('/id/<_id>', methods=GET)
def get_size_by_id(_id: int):
    return instance_controller(SizeController.get_by_id(_id))

@size.route('/', methods=GET)
def get_sizes():
    return instance_controller(SizeController.get_all())
