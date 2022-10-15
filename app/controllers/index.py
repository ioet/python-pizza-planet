from typing import Tuple
from sqlalchemy.exc import SQLAlchemyError

from ..repositories.managers.managers import index_manager

class IndexController:

    @staticmethod
    def test_connection() -> Tuple[bool, str]:
        try:
            index_manager.test_connection()
            return True, ''
        except (SQLAlchemyError, RuntimeError) as ex:
            return False, str(ex)
