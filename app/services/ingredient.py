from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, jsonify, request

from app.services.base_service import BaseService
from app.services.factory_service import FactoryService


from ..controllers import IngredientController

class IngredientService(BaseService):
    controller_class = IngredientController
    blueprint_name = 'ingredient'

    @staticmethod
    def create_blueprint():
        return FactoryService.create_blueprint(IngredientService)
