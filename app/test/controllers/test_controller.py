import pytest
from app.controllers import controller as factory, SizeController, BeverageController, IngredientController, OrderController


def test_controller_factory():

    controller = factory.ControllerFactory.get_controller('size')
    assert type(controller == SizeController)

    controller = factory.ControllerFactory.get_controller('beverage')
    assert type(controller == BeverageController)

    controller = factory.ControllerFactory.get_controller('ingredient')
    assert type(controller == IngredientController)

    controller = factory.ControllerFactory.get_controller('order')
    assert type(controller == OrderController)