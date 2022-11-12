from random import randrange
from faker import Faker

def clients_factory():
    fake = Faker()
    min_number_clients = 10
    max_number_clients = 70
    digits = 10
    quantity_clients = randrange(min_number_clients, max_number_clients)

    names = [fake.unique.first_name() for _ in range(quantity_clients)]
    dnis = [fake.unique.random_number(digits=digits) for _ in range(quantity_clients)]
    address = [fake.unique.address() for _ in range(quantity_clients)]
    phone = [fake.unique.phone_number() for _ in range(quantity_clients)]
    clients = [
        {       
        "client_name": names[index],
        "client_dni": dnis[index],
        "client_address": address[index],
        "client_phone": phone[index],
        } for index in range(quantity_clients)]

    return clients