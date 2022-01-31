from ..repositories.managers import OrderManager
from .base import BaseController


class OrderController(BaseController):
    manager = OrderManager
