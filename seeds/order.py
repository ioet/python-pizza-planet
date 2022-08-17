from this import s
from flask_seeder import Seeder, Faker, generator
from flask_seeder.generator import Generator
from datetime import datetime

from app.repositories.managers import Order
from random import random, randrange
from datetime import timedelta

class DateGenerator(generator.Generator):
    def generate(self):
        start=datetime.strptime('1/1/2022 1:30 PM', '%m/%d/%Y %I:%M %p')
        end=datetime.strptime('8/16/2022 1:30 PM', '%m/%d/%Y %I:%M %p')
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)

class DemoxxxSeeder(Seeder):


  def random_date():
    start=datetime.strptime('1/1/2019 1:30 PM', '%m/%d/%Y %I:%M %p')
    end=datetime.strptime('1/1/2022 1:30 PM', '%m/%d/%Y %I:%M %p')
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

  def __init__(self, db=None):
    super().__init__(db=db)
    self.priority = 10

    #client_name, client_dni, client_address, client_phone, date, total_price, size_id

  def run(self):
    self.priority = 1
    month = 8
    faker = Faker(
      cls=Order,
      init= {
        "client_name": generator.Name(),
        "client_dni": generator.Integer(start=1715123900, end=1715124000),
        "client_address": generator.Name(),
        "client_phone": generator.Integer(),
        "date": DateGenerator(),
        "total_price": generator.Integer(10),
        "size_id": generator.Integer(start=1, end=5)

      }
    )

    # Create 5 users
    for order in faker.create(100):
      print("Adding user: %s" % order)
      self.db.session.add(order)

  
