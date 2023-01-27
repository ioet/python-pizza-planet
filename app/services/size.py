from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, jsonify, request

from app.services.service import Service

from ..controllers.controller import ControllerFactory

size = Blueprint('size', __name__)
controller = ControllerFactory.get_controller('size')


@size.route('/', methods=POST)
def create_size():
    return Service.create(controller= controller)


@size.route('/', methods=PUT)
def update_size():
    return Service.update(controller= controller)


@size.route('/', methods=GET)
def get_sizes():
    return Service.get_all(controller= controller)


@size.route('/id/<_id>', methods=GET)
def get_size_by_id(_id: int):
    return Service.get_by_id(_id= _id ,controller= controller)
