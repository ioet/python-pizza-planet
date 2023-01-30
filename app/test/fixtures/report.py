import pytest
from faker import Faker

fake = Faker()


@pytest.fixture
def report_uri():
    return "/report/"
