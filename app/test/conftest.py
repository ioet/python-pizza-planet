import os
import tempfile

import pytest
from app import create_app, register_blueprints
from app.plugins import db, ma
# flake8: noqa
# pylint: disable=wildcard-import, unused-import, unused-wildcard-import
from app.repositories.models import Ingredient, Order, OrderDetail, Size, Beverage

from .fixtures.ingredient import *
from .fixtures.order import *
from .fixtures.size import *
from .fixtures.beverage import *


@pytest.fixture(name='app')
def app_fixture():

    db_fd, dbpath = tempfile.mkstemp()

    class Config:
        SQLALCHEMY_DATABASE_URI = f'sqlite:///{dbpath}'
        TESTING = True
        SQLALCHEMY_TRACK_MODIFICATIONS = False

    flask_app = create_app(Config)
    register_blueprints(flask_app)
    flask_app.app_context().push()
    db.init_app(flask_app)
    ma.init_app(flask_app)

    db.create_all()

    yield flask_app

    db.session.remove()
    db.drop_all()
    os.close(db_fd)
    os.remove(dbpath)


@pytest.fixture
def client(app):
    return app.test_client()
