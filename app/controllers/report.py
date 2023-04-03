from sqlalchemy.exc import SQLAlchemyError

from ..repositories.managers import ReportManager
from .base import BaseController


class ReportController(BaseController):
    manager = ReportManager

    @classmethod
    def get_report(cls):
        try:
            return cls.manager.get_report(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)