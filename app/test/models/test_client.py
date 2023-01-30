import pytest
from app.models import Client
from app.test.utils.functions import get_random_client

def test_client_creation():
    client = get_random_client()
    pytest.assume(type(client) is Client)

def test_get_name():
    client = get_random_client()
    pytest.assume(client.getName() == 'Albert Tester')

def test_get_dni():
    client = get_random_client()
    pytest.assume(client.getDni() == '1102699926')

def test_get_address():
    client = get_random_client()
    pytest.assume(client.getAddress() == 'Test Address')

def test_get_phone():
    client = get_random_client()
    pytest.assume(client.getPhone() == '2589502')

def test_set_name():
    client = get_random_client()
    client.setName('Juan Buencodigo')
    pytest.assume(client.getName() == 'Juan Buencodigo')

def test_set_dni():
    client = get_random_client()
    client.setDni('1234567890')
    pytest.assume(client.getDni() == '1234567890')

def test_set_address():
    client = get_random_client()
    client.setAddress('Test Address 2')
    pytest.assume(client.getAddress() == 'Test Address 2')

def test_set_phone():
    client = get_random_client()
    client.setPhone('25050999')
    pytest.assume(client.getPhone() == '25050999')
