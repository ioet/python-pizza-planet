from ..repositories.managers import ReportManager
from sqlalchemy.exc import SQLAlchemyError


class ReportController():
    manager = ReportManager

    @classmethod
    def get_report(cls) -> dict:
        try:
            return {'most_requested_ingredient': cls.manager.get_most_requested_ingredient(),
                    'month_with_more_revenue': cls.manager.get_month_with_more_revenue(),
                    'best_customers': cls.manager.get_best_customers()}, None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)

    @classmethod
    def get_most_requested_ingredient(cls) -> dict:
        try:
            return cls.manager.get_most_requested_ingredient(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)

    @classmethod
    def get_month_with_more_revenue(cls) -> dict:
        try:
            return cls.manager.get_month_with_more_revenue(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)

    @classmethod
    def get_best_customers(cls) -> dict:
        try:
            return cls.manager.get_best_customers(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)