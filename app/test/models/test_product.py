import pytest
from app.models import Product
from app.test.utils.functions import get_random_product

def test_product_creation():
    product = get_random_product()
    pytest.assume(type(product) is Product)

def test_get_name():
    product = get_random_product()
    pytest.assume(product.getName() == 'Pizza')

def test_get_data():
    product = get_random_product()
    pytest.assume(product.getData('size_id') == 1)
    pytest.assume(product.getData('ingredient') == [1,2,3,4,5])

def test_set_name():
    product = get_random_product()
    product.setName('New Product')    
    pytest.assume(product.getName() == 'New Product')

def test_set_data():
    product = get_random_product()
    product.setData({'type': '2', 'size': '2'})
    pytest.assume(product.getData('type') == '2')
    pytest.assume(product.getData('size') == '2')