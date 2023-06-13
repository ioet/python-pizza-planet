from ...repositories.models import Ingredient, Order, Beverage, Size
from typing import List

class OrderBuilder:
    def __init__(self):
        self.order_data = {}
        self.ingredients = []
        self.beverages = []

    def with_client_name(self, client_name: str) -> 'OrderBuilder':
        self.order_data['client_name'] = client_name
        return self

    def with_client_dni(self, client_dni: str) -> 'OrderBuilder':
        self.order_data['client_dni'] = client_dni
        return self

    def with_client_address(self, client_address: str) -> 'OrderBuilder':
        self.order_data['client_address'] = client_address
        return self

    def with_client_phone(self, client_phone: str) -> 'OrderBuilder':
        self.order_data['client_phone'] = client_phone
        return self
    
    def with_size(self, size_id: int) -> 'OrderBuilder':
        self.order_data['size_id'] = size_id
        return self
    
    def with_total_price(self, total_price: float) -> 'OrderBuilder':
        self.order_data['total_price'] = total_price
        return self

    def with_ingredients(self, ingredients: List[Ingredient]) -> 'OrderBuilder':
        self.ingredients = ingredients
        return self

    def with_beverages(self, beverages: List[Beverage]) -> 'OrderBuilder':
        self.beverages = beverages
        return self
    

    def build(self) -> Order:
        new_order = Order(**self.order_data)
        for ingredient in self.ingredients:
            new_order.ingredients.append(ingredient)
        for beverage in self.beverages:
            new_order.beverages.append(beverage)
        return new_order
