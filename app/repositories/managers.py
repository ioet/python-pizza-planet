from typing import Optional

from .models import Ingredient, Order, Size, db
from .serializers import (IngredientSerializer, OrderSerializer,
                          SizeSerializer, ma)


class BaseManager:
    model: Optional[db.Model] = None
    serializer: Optional[ma.ModelSchema] = None

    @classmethod
    def get_all(cls):
        serializer = cls.serializer(many=True)
        _objects = cls.model.query.all()
        result = serializer.dump(_objects)
        return result


class SizeManager(BaseManager):
    model = Size
    serializer = SizeSerializer


class IngredientManager(BaseManager):
    model = Ingredient
    serializer = IngredientSerializer


class OrderManager(BaseManager):
    model = Order
    serializer = OrderSerializer

    @classmethod
    def create_order(cls, db, order):
        pass
