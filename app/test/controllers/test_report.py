import pytest
from app.controllers import ReportController


def test_get_most_requested_ingredient(app):
    most_requested_ingredient, error = ReportController.get_most_requested_ingredient()
    pytest.assume(error is None)
    pytest.assume(most_requested_ingredient is None)


def test_get_month_with_most_revenue(app):
    month_with_more_revenue, error = ReportController.get_month_with_more_revenue()
    pytest.assume(error is None)
    pytest.assume(month_with_more_revenue is None)


def test_get_best_customers(app):
    best_customers, error = ReportController.get_best_customers()
    pytest.assume(error is None)
    pytest.assume(best_customers is None)