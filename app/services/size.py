from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, jsonify, request

from ..controllers import SizeController
from .base import *

size = Blueprint('size', __name__)


@size.route('/', methods=POST)
def create_size():
    return create_entity(SizeController)


@size.route('/', methods=PUT)
def update_size():
    return update_entity(SizeController)


@size.route('/id/<_id>', methods=GET)
def get_size_by_id(_id: int):
    return get_entity_by_id(SizeController, _id)


@size.route('/', methods=GET)
def get_sizes():
    return get_all_entities(SizeController)
