from app.common.http_methods import POST, PUT, GET
from flask import Blueprint, request
from app.controllers.beverage import BeverageController
from app.services.base import BaseService


beverage = Blueprint('beverage', __name__)

beverage_base_service = BaseService(entity = "beverage", 
        entitycontroller = BeverageController())

@beverage.route('/', methods=POST)
def create_beverage():
    return beverage_base_service.create(request)


@beverage.route('/', methods=PUT)
def update_beverage():
    return beverage_base_service.update(request)

@beverage.route('/id/<_id>', methods=GET)
def get_beverage_by_id(_id: int):
    return beverage_base_service.get_by_id(_id)

@beverage.route('/', methods=GET)
def get_beverage():
    return beverage_base_service.get_all() 
    