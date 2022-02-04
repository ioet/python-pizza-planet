import pytest

from ..utils.functions import get_random_price, get_random_string


@pytest.fixture
def size_uri():
    return '/size'


@pytest.fixture
def size() -> dict:
    return {
        'name': get_random_string(),
        'price': get_random_price(10, 20)
    }


@pytest.fixture
def create_size(client, size_uri) -> dict:
    response = client.post(size_uri, json=size())
    return response.json


@pytest.fixture
def create_sizes(client, size_uri) -> list:
    sizes = []
    for _ in range(10):
        new_size = client.post(size_uri, json=size())
        sizes.append(new_size.json)
    return sizes
