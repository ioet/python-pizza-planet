from flask_seeder import Seeder, Faker, generator

from app.repositories.managers import Size


class DemoSeeder(Seeder):
  def __init__(self, db=None):
    super().__init__(db=db)
    self.priority = 10

  def run(self):
    self.priority = 1
    faker = Faker(
      cls=Size,
      init={
        "name": generator.Name(),
        "price": generator.Integer(start=5, end=20)
      }
    )

    # Create 5 users
    for size in faker.create(5):
      print("Adding user: %s" % size)
      self.db.session.add(size)

  
