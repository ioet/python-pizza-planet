from flask_seeder import Seeder, Faker, generator
from app.repositories.managers import OrderDetail


class DemoSeeder(Seeder):
  def __init__(self, db=None):
    super().__init__(db=db)
    self.priority = 10

    #ingredient_price, order_id, ingredient_id, beverage_price, beverage_id

  def run(self):
    self.priority = 1
    faker = Faker(
      cls=OrderDetail,
      init={
        "ingredient_price": generator.Integer(start=1, end=4),
        "order_id": generator.Integer(start=1, end=100),
        "ingredient_id": generator.Integer(start=1, end=10),
        "beverage_price": generator.Integer(start=1, end=4),
        "beverage_id": generator.Integer(start=1, end=10)

      }
    )

    # Create 5 users
    for order_detail in faker.create(200):
      print("Adding user: %s" % order_detail)
      self.db.session.add(order_detail)

  
