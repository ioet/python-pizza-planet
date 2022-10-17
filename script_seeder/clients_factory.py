from random import randrange
from faker import Faker

def clients_factory():
    fake = Faker()
    quantity_clients = randrange(10, 70)

    names = [fake.unique.first_name() for _ in range(quantity_clients)]
    dnis = [fake.unique.random_number(digits=10) for _ in range(quantity_clients)]
    address = [fake.unique.address() for _ in range(quantity_clients)]
    phone = [fake.unique.phone_number() for _ in range(quantity_clients)]
    clients = []

    for index in range(quantity_clients):
        clients.append({
            "client_name": names[index],
            "client_dni": dnis[index],
            "client_address": address[index],
            "client_phone": phone[index],
        })

    return clients