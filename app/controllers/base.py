from typing import Any, Optional, Tuple
from sqlalchemy.exc import SQLAlchemyError
from ..repositories.managers import BaseManager
from app.plugins import db


class BaseController:
    manager: Optional[BaseManager] = None

    @classmethod
    def get_by_id(cls, _id: Any) -> Tuple[Any, Optional[str]]:
        try:
            return cls.manager.get_by_id(_id), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)

    @classmethod
    def get_all(cls) -> Tuple[Any, Optional[str]]:
        try:
            return cls.manager.get_all(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)

    @classmethod
    def create(cls, entry: dict) -> Tuple[Any, Optional[str]]:
        try:
            session = db.session
            manager_obj = cls.manager(session)
            new_entry = manager_obj.create(entry)
            session.commit()
            return new_entry, None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)

    @classmethod
    def update(cls, new_values: dict) -> Tuple[Any, Optional[str]]:
        try:
            _id = new_values.pop('_id', None)
            if not _id:
                return None, 'Error: No id was provided for update'
            session = db.session
            manager_obj = cls.manager(session)
            updated_entry = manager_obj.update(_id, new_values)
            session.commit()
            return updated_entry, None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)
