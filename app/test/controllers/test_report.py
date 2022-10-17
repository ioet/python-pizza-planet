from app.controllers.report import ReportController
import pytest

def test_get(create_orders):
    report, error = ReportController.get()
    pytest.assume(error is None)
    
    pytest.assume(report['most_popular_ingredient'])
    pytest.assume(report['month_more_revenue'])
    pytest.assume(report['best_costumers'])
