import pytest

def test__get_report_service_when_status_is_200_should_return_the_report(client, report_uri, create_orders):
    response = client.get(report_uri)
    
    pytest.assume(response.status.startswith('200'))
    pytest.assume(response.json['most_popular_ingredient'])
    pytest.assume(response.json['month_more_revenue'])
    pytest.assume(response.json['best_costumers'])



