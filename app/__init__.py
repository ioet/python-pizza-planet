import inspect

from flask import Blueprint, Flask


def create_app(config_class: str):
    flask_application = Flask(__name__)
    flask_application.config.from_object(config_class)
    return flask_application


def register_blueprints(flask_application):
    from app import services  # pylint: disable=import-outside-toplevel
    blueprints = inspect.getmembers(
        services, lambda member: isinstance(member, Blueprint))
    for name, blueprint in blueprints:
        prefix = '/' if name == 'index' else f'/{name.replace("_", "-")}'
        flask_application.register_blueprint(blueprint, url_prefix=prefix)


def register_plugins(flask_application):
    from .plugins import db, ma  # pylint: disable=import-outside-toplevel
    db.init_app(flask_application)
    ma.init_app(flask_application)


def cors_app(flask_application):
    from flask_cors import CORS  # pylint: disable=import-outside-toplevel
    CORS(flask_application)


def configure_app(config_class):
    flask_application = create_app(config_class)
    register_blueprints(flask_application)
    register_plugins(flask_application)
    cors_app(flask_application)

    return flask_application


flask_app = configure_app('app.settings.Config')
