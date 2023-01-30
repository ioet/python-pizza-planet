import pytest
from faker import Faker

fake = Faker()


def test_get_most_requested_ingredient_service(client, report_uri):
    response = client.get(f'{report_uri}ingredient')
    pytest.assume(response.status.startswith('200'))


def test_get_month_with_most_revenue_service(client, report_uri):
    response = client.get(f'{report_uri}month')
    pytest.assume(response.status.startswith('200'))


def test_get_best_customers_service(client, report_uri):
    response = client.get(f'{report_uri}customer')
    pytest.assume(response.status.startswith('200'))