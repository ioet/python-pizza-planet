from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request

from app.services.base_service import BaseService
from app.services.factory_service import FactoryService


from ..controllers import SizeController

class SizeService(BaseService):
    controller_class = SizeController
    blueprint_name = 'size'

    @staticmethod
    def create_blueprint():
        return FactoryService.create_blueprint(SizeService)