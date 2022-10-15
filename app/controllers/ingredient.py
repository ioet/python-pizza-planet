from ..repositories.managers.managers import ingredient_manager
from .base import BaseController
class IngredientController(BaseController):
    manager = ingredient_manager
