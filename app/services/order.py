from app.common.http_methods import GET, POST
from flask import Blueprint, request

from app.services.base_service import BaseService
from app.services.factory_service import FactoryService


from ..controllers import OrderController

class OrderService(BaseService):
    controller_class = OrderController
    blueprint_name = 'order'

    @staticmethod
    def create_blueprint():
        return FactoryService.create_blueprint(OrderService)