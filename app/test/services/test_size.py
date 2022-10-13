import pytest

def test_get_sizes_service(client, size_uri, create_sizes):
    response = client.get(size_uri)
    pytest.assume(response.status.startswith('200'))
    returned_sizes = {size['_id']: size for size in response.json}    
    for size in create_sizes:
        pytest.assume(size['_id'] in returned_sizes)