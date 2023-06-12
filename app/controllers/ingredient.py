from ..repositories.managers import IngredientManager
from .base import BaseController
from ..common.utils import check_required_keys


class IngredientController(BaseController):
    manager = IngredientManager
    __required_info = ('name', 'price')

    @classmethod
    def create(cls, ingredient: dict):
        current_ingredient = ingredient.copy()
        if not check_required_keys(cls.__required_info, current_ingredient):
            return 'Invalid ingredient payload', None

        return cls.manager.create(current_ingredient), None
    
    
