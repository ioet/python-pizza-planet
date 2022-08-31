import pytest
from app.data_generator.data_generator import CustomerGenerator

from ..utils.functions import *


def test_customer_generator():
    
    assert CustomerGenerator.create_dummy_data(
        {
            'client_address': get_random_string(),
            'client_dni': get_random_sequence(),
            'client_name': get_random_string(),
            'client_phone': get_random_sequence()
        }
    )