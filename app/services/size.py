from flask import Blueprint
from app.common.http_methods import GET, POST, PUT

from .base_service import BaseService

from ..controllers import SizeController

size = Blueprint('size', __name__)
size_service = BaseService(entity_controller=SizeController)


@size.route("/", methods=POST)
def create_size():
    return size_service.create()


@size.route("/", methods=PUT)
def update_size():
    return size_service.update()


@size.route('/id/<_id>', methods=GET)
def get_size_by_id(_id: int):
    return size_service.get_by_id(_id)


@size.route("/", methods=GET)
def get_sizes():
    return size_service.get()
