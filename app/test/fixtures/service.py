import pytest

from ..utils.functions import get_random_price, get_random_string


def service_mock() -> dict:
    return {
        'name': get_random_string(),
        'price': get_random_price(10, 20)
    }


@pytest.fixture
def service_uri():
    return '/service/'


@pytest.fixture
def service():
    return service_mock()


@pytest.fixture
def services():
    return [service_mock() for _ in range(5)]


@pytest.fixture
def create_service(client, service_uri) -> dict:
    response = client.post(service_uri, json=service_mock())
    return response


@pytest.fixture
def create_services(client, service_uri) -> list:
    services = []
    for _ in range(10):
        new_service = client.post(service_uri, json=service_mock())
        services.append(new_service.json)
    return services
