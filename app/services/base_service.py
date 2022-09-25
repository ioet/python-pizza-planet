from flask import jsonify, request
from ..controllers.base import BaseController


class BaseService:
    def __init__(self, entity_controller: BaseController):
        self.entity_controller = entity_controller

    def create(self):
        entity, error = self.entity_controller.create(request.json)
        response = entity if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code

    def update(self):
        entity, error = self.entity_controller.update(request.json)
        response = entity if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code

    def get_by_id(self, _id: int):
        entity, error = self.entity_controller.get_by_id(_id)
        response = entity if not error else {'error': error}
        status_code = 200 if entity else 404 if not error else 400
        return jsonify(response), status_code

    def get(self):
        entity, error = self.entity_controller.get_all()
        response = entity if not error else {'error': error}
        status_code = 200 if entity else 404 if not error else 400
        return jsonify(response), status_code
