from ..repositories.managers import SizeManager
from .base import BaseController
from ..common.utils import check_required_keys



class SizeController(BaseController):
    manager = SizeManager
    __required_info = ('name', 'price')

    @classmethod
    def create(cls, size: dict):
        current_size = size.copy()
        if not check_required_keys(cls.__required_info, current_size):
            return 'Invalid size payload', None

        return cls.manager.create(current_size), None
    
    
