from ..repositories.managers import OrderManager
from .base import BaseController


class ReportController(BaseController):
    manager = OrderManager
