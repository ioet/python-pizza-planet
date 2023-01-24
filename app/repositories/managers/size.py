from .base import BaseManager
from ..models import Size
from ..serializers.size import SizeSerializer


class SizeManager(BaseManager):
    model = Size
    serializer = SizeSerializer
