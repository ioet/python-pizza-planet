from flask import jsonify, request


class BaseService:
    controller_class = None
    blueprint_name = None

    @classmethod
    def create(cls):
        service, error = cls.controller_class.create(request.json)
        response = service if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code

    @classmethod
    def update(cls):
        service, error = cls.controller_class.update(request.json)
        response = service if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code

    @classmethod
    def get_by_id(cls, _id: int):
        service, error = cls.controller_class.get_by_id(_id)
        response = service if not error else {'error': error}
        status_code = 200 if service else 404 if not error else 400
        return jsonify(response), status_code

    @classmethod
    def get_all(cls):
        services, error = cls.controller_class.get_all()
        response = services if not error else {'error': error}
        status_code = 200 if services else 404 if not error else 400
        return jsonify(response), status_code