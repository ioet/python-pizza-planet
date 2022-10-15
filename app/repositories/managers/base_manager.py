from typing import Any, Optional, List, Sequence

from ..models import Ingredient, OrderDetail, Beverage
from ..serializers import ma, db

from sqlalchemy.sql import text, column

class BaseManager:

    def __init__(self, model: Optional[db.Model], serializer: Optional[ma.SQLAlchemyAutoSchema]):
        self.model = model
        self.serializer = serializer
        self.session = db.session

    def get_all(self):
        serializer = self.serializer(many=True)
        _objects = self.model.query.all()
        result = serializer.dump(_objects)
        return result

    def get_by_id(self, _id: Any):
        entry = self.model.query.get(_id)
        return self.serializer().dump(entry)

    def create(self, entry: dict):
        serializer = self.serializer()
        new_entry = serializer.load(entry)
        self.session.add(new_entry)
        self.session.commit()
        return serializer.dump(new_entry)

    def update(self, _id: Any, new_values: dict):
        self.session.query(self.model).filter_by(_id=_id).update(new_values)
        self.session.commit()
        return self.get_by_id(_id)

    def get_by_id_list(cls, ids: Sequence):
        return cls.session.query(cls.model).filter(
            cls.model._id.in_(set(ids))).all() or []

    def create_order(cls, order_data: dict,  ingredients: List[Ingredient], beverages: List[Beverage]):
        new_order = cls.model(**order_data)
        cls.session.add(new_order)
        cls.session.flush()
        cls.session.refresh(new_order)
        cls.session.add_all((
            OrderDetail(
                order_id=new_order._id,
                ingredient_id=ingredient._id,
                ingredient_price=ingredient.price,
            ) for ingredient in ingredients
        )
        )
        cls.session.add_all((
            OrderDetail(
                order_id=new_order._id,
                beverage_id=beverage._id,
                beverage_price=beverage.price,
            ) for beverage in beverages
        )
        )
        cls.session.commit()
        return cls.serializer().dump(new_order)

    def test_connection(cls):
        cls.session.query(column('1')).from_statement(text('SELECT 1')).all()
