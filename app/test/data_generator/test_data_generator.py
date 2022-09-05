import pytest
from app.data_generator import create_data 


def test_dummy_orders_created():

    assert create_data.main() == {}