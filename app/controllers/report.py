from ast import Tuple
from typing import Any, Optional
from sqlalchemy.exc import SQLAlchemyError

from ..repositories.managers.managers import (report_manager)
from .base import BaseController


class ReportController(BaseController):
    manager = report_manager

    @classmethod
    def get(cls) -> str:
        try:
            return cls.manager.get_report(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)