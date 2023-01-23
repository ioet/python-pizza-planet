import pytest

from app.test.utils.functions import get_random_string, get_random_price

def test_create_size_service(create_size):
        size = create_size.json
        pytest.assume(create_size.status.startswith('200'))
        pytest.assume(size['_id'])
        pytest.assume(size['name'])
        pytest.assume(size['price'])

def test_get_sizes_service(client, create_sizes, size_uri):
    response = client.get(size_uri)
    pytest.assume(response.status.startswith('200'))
    returned_sizes = {size['_id']: size for size in response.json}
    for size in create_sizes:
        pytest.assume(size['_id'] in returned_sizes)