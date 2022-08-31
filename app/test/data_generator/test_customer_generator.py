import pytest
from app.data_generator.data_generator import CustomerGenerator

from ..utils.functions import *


def test_customer_generator():
    
    assert CustomerGenerator.create_dummy_data(
            customer_address = get_random_string(),
            customer_dni = get_random_sequence(),
            customer_name = get_random_string(),
            customer_phone = get_random_sequence()
    )