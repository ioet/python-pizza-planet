from app.common.http_methods import POST, PUT, GET
from flask import Blueprint


class FactoryService:
    @staticmethod
    def create_blueprint(service_class):
        blueprint = Blueprint(service_class.blueprint_name, __name__)

        blueprint.route('/', methods=POST)(service_class.create)
        blueprint.route('/', methods=PUT)(service_class.update)
        blueprint.route('/id/<_id>', methods=GET)(service_class.get_by_id)
        blueprint.route('/', methods=GET)(service_class.get_all)

        return blueprint