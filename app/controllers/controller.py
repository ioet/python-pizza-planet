from dataclasses import dataclass

from app.controllers.report import ReportController

from .beverage import BeverageController
from .size import SizeController
from .ingredient import IngredientController
from .order import OrderController


@dataclass
class ControllerFactory:
    @staticmethod
    def get_controller(controller: str):
        if controller == "size":
            return SizeController
        if controller == "beverage":
            return BeverageController
        if controller == "ingredient":
            return IngredientController
        if controller == "order":
            return OrderController
