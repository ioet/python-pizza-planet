from .base import BaseController
from ..repositories.managers.managers import beverage_manager

class BeverageController(BaseController):
    manager = beverage_manager
