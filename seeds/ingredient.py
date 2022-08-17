from flask_seeder import Seeder, Faker, generator

from app.repositories.managers import Ingredient


class DemoSeeder(Seeder):
  def __init__(self, db=None):
    super().__init__(db=db)
    self.priority = 10

  def run(self):
    faker = Faker(
      cls=Ingredient,
      init={
        "name": generator.Name(),
        "price": generator.Integer(start=1, end=5)
      }
    )

    # Create 5 users
    for ingredient in faker.create(10):
      print("Adding user: %s" % ingredient)
      self.db.session.add(ingredient)


  
