from ..repositories.managers import BeverageManager
from .base import BaseController
from ..common.utils import check_required_keys



class BeverageController(BaseController):
    manager = BeverageManager
    __required_info = ('name', 'price')

    @classmethod
    def create(cls, size: dict):
        current_beverage = size.copy()
        if not check_required_keys(cls.__required_info, current_beverage):
            return 'Invalid size payload', None

        return cls.manager.create(current_beverage), None
    
    
