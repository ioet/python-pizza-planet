import pytest

from ..utils.functions import get_random_price, get_random_string


def beverage_mock() -> dict:
    return {
        'name': get_random_string(),
        'price': get_random_price(1, 10)
    }


@pytest.fixture
def beverage_uri():
    return '/beverage/'


@pytest.fixture
def beverage():
    return beverage_mock()


@pytest.fixture
def beverages():
    return [beverage_mock() for _ in range(3)]