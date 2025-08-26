import pytest


@pytest.fixture
def sample_transactions():
    return [
        {"state": "EXECUTED", "date": "2023-10-01"},
        {"state": "CANCELED", "date": "2023-09-01"},
        {"state": "EXECUTED", "date": "2023-08-15"},
    ]
