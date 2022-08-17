from flask_seeder import Seeder, Faker, generator

from app.repositories.managers import Beverage


class DemoSeeder(Seeder):
  def __init__(self, db=None):
    super().__init__(db=db)
    self.priority = 10

  def run(self):
    self.priority = 1
    faker = Faker(
      cls=Beverage,
      init={
        "name": generator.Name(),
        "price": generator.Integer(start=1, end=5)
      }
    )

    # Create 5 users
    for beverage in faker.create(10):
      print("Adding user: %s" % beverage)
      self.db.session.add(beverage)

  
