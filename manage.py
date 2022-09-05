

import pytest
from flask.cli import FlaskGroup
from flask_migrate import Migrate
from app.data_generator import create_data

from app import flask_app
from app.plugins import db
# flake8: noqa
from app.repositories.models import Ingredient, Order, OrderDetail, Size


manager = FlaskGroup(flask_app)

migrate = Migrate()
migrate.init_app(flask_app, db)

@manager.command('generate_orders', with_appcontext=True)
def generate_orders():
    return create_data.main()


@manager.command('test', with_appcontext=False)
def test():
    return pytest.main(['-v', '-s', './app/test'])


if __name__ == '__main__':
    manager()
