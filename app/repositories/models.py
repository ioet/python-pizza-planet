from datetime import datetime
from app.plugins import db

class Ingredient(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)

class Beverage(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)

class Size(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)

class OrderXIngredient(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order._id'))
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient._id'))
    order = db.relationship('Order', backref=db.backref('order_ingredients', overlaps="order,order_ingredients"))
    ingredient = db.relationship('Ingredient', backref=db.backref('ingredient'))

class OrderXBeverage(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order._id'))
    beverage_id = db.Column(db.Integer, db.ForeignKey('beverage._id'))
    order = db.relationship('Order', backref=db.backref('order_beverages', overlaps="order,order_beverages"))
    beverage = db.relationship('Beverage', backref=db.backref('beverage'))

class Order(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(80))
    client_dni = db.Column(db.String(10))
    client_address = db.Column(db.String(128))
    client_phone = db.Column(db.String(15))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    size_id = db.Column(db.Integer, db.ForeignKey('size._id'))
    size = db.relationship('Size', backref=db.backref('size'))
    ingredients = db.relationship('Ingredient', secondary='order_x_ingredient', backref=db.backref('orders', lazy=True))
    beverages = db.relationship('Beverage', secondary='order_x_beverage', backref=db.backref('orders', lazy=True))
    total_price = db.Column(db.Float)
    order_x_ingredient = db.relationship('OrderXIngredient', backref=db.backref('order_x_ingredient'))
    order_x_beverage = db.relationship('OrderXBeverage', backref=db.backref('order_x_beverage'))

