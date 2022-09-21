from datetime import datetime

from app.plugins import db


class Order(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(80))
    client_dni = db.Column(db.String(10))
    client_address = db.Column(db.String(128))
    client_phone = db.Column(db.String(15))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    total_price = db.Column(db.Float)
    details = db.relationship('OrderDetail', backref=db.backref('order'))


class Ingredient(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)


class Size(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)


class OrderDetail(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order._id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product._id'), nullable=False)
    product = db.relationship('Product', backref=db.backref('order_detail'))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)


class Product(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    product_type = db.Column(db.String(32), nullable=False)

    __mapper_args__ = {'polymorphic_on': product_type}


class Beverage(Product):
    name = db.Column(db.String(80))
    price = db.Column(db.Float)

    __mapper_args__ = {'polymorphic_identity': 'beverage'}


class Pizza(Product):
    size_id = db.Column(db.Integer, db.ForeignKey('size._id'))
    size = db.relationship('Size', backref=db.backref('pizzas_of_size'))
    ingredients = db.relationship('PizzaIngredient', backref=db.backref('pizza'))

    __mapper_args__ = {'polymorphic_identity': 'pizza'}


class PizzaIngredient(db.Model):
    pizza_id = db.Column(db.Integer, db.ForeignKey('product._id'), nullable=False, primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient._id'), nullable=False, primary_key=True)
    ingredient = db.relationship('Ingredient', backref=db.backref('pizzas_with_ingredient'))
    quantity = db.Column(db.Integer, nullable=False)
