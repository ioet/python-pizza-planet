import pytest
from ..utils.functions import get_random_price, get_random_string
from faker import Faker

def report_mock() -> dict:
    return {
        'most_popular_ingredient': get_random_string(),
        'month_more_revenue': {"month": Faker().month_name(), "income": get_random_price(10.0, 50.0)},
        'best_costumers': [
            {'client_name': get_random_string()},
            {'client_name': get_random_string()},
            {'client_name': get_random_string()},
        ],
    }

@pytest.fixture
def report_uri():
    return '/report/'


@pytest.fixture
def report():
    return report_mock()

