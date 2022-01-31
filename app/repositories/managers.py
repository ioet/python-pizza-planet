from typing import Any, Optional, Sequence, List

from .models import Ingredient, Order, OrderDetail, Size, db
from .serializers import (IngredientSerializer, OrderSerializer,
                          SizeSerializer, ma)


class BaseManager:
    model: Optional[db.Model] = None
    serializer: Optional[ma.SQLAlchemyAutoSchema] = None
    db = db

    @classmethod
    def get_all(cls):
        serializer = cls.serializer(many=True)
        _objects = cls.model.query.all()
        result = serializer.dump(_objects)
        return result

    @classmethod
    def get_by_id(cls, _id: Any):
        entry = cls.model.query.get(_id)
        return cls.serializer().dump(entry)

    @classmethod
    def create(cls, entry: dict):
        serializer = cls.serializer()
        new_entry = serializer.load(entry)
        cls.db.session.add(new_entry)
        cls.db.session.commit()
        return serializer.dump(new_entry)

    @classmethod
    def update(cls, _id: Any, new_values: dict):
        entry = cls.get_by_id(_id)
        entry.update(new_values)
        cls.db.session.commit()
        return cls.serializer().dump(entry)


class SizeManager(BaseManager):
    model = Size
    serializer = SizeSerializer


class IngredientManager(BaseManager):
    model = Ingredient
    serializer = IngredientSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return cls.model.filter(cls.model._id.in_(set(ids))).all()


class OrderManager(BaseManager):
    model = Order
    serializer = OrderSerializer

    @classmethod
    def create(cls, order_data: dict, ingredients: List[Ingredient]):
        new_order = cls.model(**order_data)
        cls.db.session.add(new_order)
        cls.db.session.flush()
        cls.db.session.refresh(new_order)
        cls.db.session.add_all((OrderDetail(order_id=new_order._id, ingredient_id=ingredient._id, ingredient_price=ingredient.price)
                                for ingredient in ingredients))
        cls.db.session.commit()
        return cls.serializer().dump(new_order)

    @classmethod
    def update(cls):
        raise NotImplementedError(f'Method not suported for {cls.__name__}')