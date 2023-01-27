from app.common.http_methods import GET, POST, PUT
from flask import Blueprint
from app.controllers.controller import ControllerFactory

from app.services.service import Service


beverage = Blueprint("beverage", __name__)
controller = ControllerFactory.get_controller("beverage")


@beverage.route("/", methods=POST)
def create_beverage():
    return Service.create(controller=controller)


@beverage.route("/", methods=PUT)
def update_beverage():
    return Service.update(controller=controller)


@beverage.route("/id/<_id>", methods=GET)
def get_beverage_by_id(_id: int):
    return Service.get_by_id(_id=_id, controller=controller)


@beverage.route("/", methods=GET)
def get_beverages():
    return Service.get_all(controller=controller)
