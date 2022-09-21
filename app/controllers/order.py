from copy import deepcopy

from sqlalchemy.exc import SQLAlchemyError

from app.plugins import db
from ..common.utils import check_required_keys
from ..repositories.managers import (OrderManager, ProductManager)
from .base import BaseController


class OrderController(BaseController):
    manager = OrderManager
    __required_info = ('client_name', 'client_dni', 'client_address', 'client_phone', 'details')

    @classmethod
    def create(cls, order: dict):
        current_order = deepcopy(order)
        if not check_required_keys(cls.__required_info, current_order):
            print('check_required_keys')
            return None, 'Invalid order payload'

        details = current_order.get('details')
        for detail in details:
            product = detail.get('product')
            product_type = product.get('product_type')
            quantity = detail.get('quantity')
            product_price = ProductManager(product_type).calculate_price(data=product)
            detail['price'] = product_price * quantity

        current_order['total_price'] = sum([d.get('price') for d in details])

        try:
            session = db.session
            cls.manager = OrderManager(session)
            new_order = cls.manager.create(current_order)
            session.commit()
            return new_order, None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)
