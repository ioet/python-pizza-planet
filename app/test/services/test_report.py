import pytest

from app.test.utils.functions import get_random_string, get_random_price


def test_get_report_service(get_report):
    report = get_report.json
    pytest.assume(get_report.status.startswith('200'))

