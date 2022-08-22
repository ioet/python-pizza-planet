from urllib import request
from ..controllers.base import BaseController
from flask import jsonify, request


class BaseService():
    def __init__(cls, entity_controller: BaseController):
        cls.entity_controller = entity_controller

    def create(cls):
        entity, error = cls.entity_controller.create(request.json)
        response = entity if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code
    
    def update(cls):
        entity, error = cls.entity_controller.update(request.json)
        response = entity if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code

    def get_by_id(cls, _id: int):
        entity, error = cls.entity_controller.get_by_id(_id)
        response = entity if not error else {'error': error}
        status_code = 200 if entity else 404 if not error else 400
        return jsonify(response), status_code

    def get(cls):
        entity, error = cls.entity_controller.get_all()
        response = entity if not error else {'error': error}
        status_code = 200 if entity else 404 if not error else 400
        return jsonify(response), status_code
