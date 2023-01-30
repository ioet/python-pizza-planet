from ..models import Order
from ..models import Product
from ..models import Client

class OrderBuilder:
    def __init__(self):
        self.Client: Client = None
        self.Products = []
        self.price = 0

    @staticmethod
    def item():
        return OrderBuilder()
    
    def standardOrder(self, client, product, price):
        self.Client = client
        self.Products = [product]
        self.price = price
        return self
    
    def withMultipleProducts(self, products: list[Product]):
        self.Products.extend(products)
        return self

    def build(self):
        return Order(self.Client, self.Products, self.price)
    
    def orderDict(self):
        return {
            'client_name': self.Client.getName(),
            'client_dni': self.Client.getDni(),
            'client_address': self.Client.getAddress(),
            'client_phone': self.Client.getPhone(),
            'size_id': self.Products[0].getData('size_id'),
            'total_price': self.price
        }
