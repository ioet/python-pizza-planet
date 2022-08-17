import pytest
from app.controllers import ReportController


def test_generate_report(app):
    _, error =  ReportController.generate_report()
    pytest.assume(error is None)


