import pytest

@pytest.fixture
def report_uri():
    return '/report/'

# def report_mock() -> dict:
#     return {
#         'Top 3 clients': get_random_string(),
#         'Most request ': get_random_price(10, 20)
#     }


# @pytest.fixture
# def create_report(client, report_uri):
#     response = client.post(report_uri, json = )