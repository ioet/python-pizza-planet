from flask import jsonify, request
from ..controllers.base import BaseController


class BaseService():
    entity_controller: BaseController

    def __init__(self, entity_controller: BaseController):
        self.entity_controller = entity_controller

    @classmethod
    def create(cls):
        entity, error = cls.entity_controller.create(request.json)
        response = entity if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code

    @classmethod
    def update(cls):
        entity, error = cls.entity_controller.update(request.json)
        response = entity if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code

    @classmethod
    def get_by_id(cls, _id: int):
        entity, error = cls.entity_controller.get_by_id(_id)
        response = entity if not error else {'error': error}
        status_code = 200 if entity else 404 if not error else 400
        return jsonify(response), status_code

    @classmethod
    def get(cls):
        entity, error = cls.entity_controller.get_all()
        response = entity if not error else {'error': error}
        status_code = 200 if entity else 404 if not error else 400
        return jsonify(response), status_code
