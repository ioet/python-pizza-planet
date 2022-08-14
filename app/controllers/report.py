from ..repositories.managers import ReportManager
from .base import BaseController


class ReportController(BaseController):
    manager = ReportManager

    @classmethod
    def generate_report(cls):
        return ReportManager.get_report(), None
