import pytest

def test_get_report_service(client, report_uri):
    response = client.get(report_uri)
    pytest.assume(response.status.startswith('200'))
    pytest.assume(item["ingredient"] for item in response.json)
    pytest.assume(item["client_data"] for item in response.json)