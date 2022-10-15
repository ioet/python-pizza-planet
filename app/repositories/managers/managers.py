from ..models import Beverage, Ingredient, Order, Size
from ..serializers import (BeverageSerializer, IngredientSerializer, OrderSerializer,
                          SizeSerializer)
from .base_manager import BaseManager

size_manager = BaseManager(Size, SizeSerializer)

beverage_manager = BaseManager(Beverage, BeverageSerializer)
    
ingredient_manager = BaseManager(Ingredient, IngredientSerializer)

order_manager = BaseManager(Order, OrderSerializer)

index_manager = BaseManager(None, None)
