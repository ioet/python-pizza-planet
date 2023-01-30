from flask import jsonify, request
from dataclasses import dataclass

from app.controllers.controller import ControllerFactory


@dataclass
class Service:
    def create(controller: ControllerFactory):
        data, error = controller.create(request.json)
        response = data if not error else {"error": error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code

    def update(controller: ControllerFactory):
        data, error = controller.update(request.json)
        response = data if not error else {"error": error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code

    def get_all(controller: ControllerFactory):
        data, error = controller.get_all()
        response = data if not error else {"error": error}
        status_code = 200 if data else 404 if not error else 400
        return jsonify(response), status_code

    def get_by_id(_id: int, controller: ControllerFactory):
        data, error = controller.get_by_id(_id)
        response = data if not error else {"error": error}
        status_code = 200 if data else 404 if not error else 400
        return jsonify(response), status_code