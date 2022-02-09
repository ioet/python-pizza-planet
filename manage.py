

import pytest
from flask.cli import FlaskGroup
from flask_migrate import Migrate

from app import flask_app
from app.plugins import db
# flake8: noqa
from app.repositories.models import Ingredient, Order, OrderDetail, Size


manager = FlaskGroup(flask_app)

migrate = Migrate()
migrate.init_app(flask_app, db)


@manager.command('test')
def test():
    return pytest.main(['-v', './test'])


if __name__ == '__main__':
    manager()
