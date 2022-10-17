import pytest

def test_get_report(client, report_uri, create_orders):
    response = client.get(report_uri)
    
    pytest.assume(response.status.startswith('200'))
    pytest.assume(response.json['most_popular_ingredient'])
    pytest.assume(response.json['month_more_revenue'])
    pytest.assume(response.json['best_costumers'])



