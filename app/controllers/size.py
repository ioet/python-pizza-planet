from ..repositories.managers.managers import size_manager
from .base import BaseController
class SizeController(BaseController):
    manager = size_manager
