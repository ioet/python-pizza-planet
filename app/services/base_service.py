from flask import jsonify

from app.controllers.base import BaseController


class BaseService:

    def __init__(self, entity:str, entitycontroller: BaseController):
        self.entity = entity
        self.entitycontroller = entitycontroller

    def create(self, request)-> dict[jsonify]:
        self.entity, error = self.entitycontroller.create(request.json)
        response = self.entity if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response),status_code

    def get_all(self) -> dict[jsonify]:
        self.entity, error = self.entitycontroller.get_all()
        response = self.entity if not error else {'error': error}
        status_code = 200 if self.entity else 404 if not error else 400
        return jsonify(response), status_code

    def get_by_id(self, _id: int) -> dict[jsonify]:
        self.entity, error = self.entitycontroller.get_by_id(_id)
        response = self.entity if not error else {'error': error}
        status_code = 200 if self.entity else 404 if not error else 400
        return jsonify(response), status_code

    def update(self, request):
        self.entity, error = self.entitycontroller.update(request.json)
        response = self.entity if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code