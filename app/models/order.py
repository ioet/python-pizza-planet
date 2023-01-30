from .client import Client
from .product import Product

class Order():

    def __init__(self, client: Client, products: list[Product], price: float):
        self.client = client
        self.products = products
        self.price = price
    
    def getClient(self):
        return self.client
    
    def getProduct(self, index):
        return self.products[index]

    def getPrice(self):
        return self.price
    
    def setClient(self, client: Client):
        self.client = client
    
    def setProduct(self, product: Product):
        self.products.append(product)

    def setProducts(self, products: list[Product]):
        self.products = products

    def setPrice(self, price: float):
        self.price = price
    