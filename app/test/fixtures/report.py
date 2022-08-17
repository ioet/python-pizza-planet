import pytest

from ..utils.functions import get_random_price, get_random_string



@pytest.fixture
def report_uri():
    return '/report/'


@pytest.fixture
def get_report(client, report_uri) -> dict:
    response = client.get(report_uri)
    return response

