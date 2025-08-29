from src.processing import filter_by_state
from src.processing import sort_by_date


def test_filter_by_state_executed(sample_transactions):
    result = filter_by_state(sample_transactions, "EXECUTED")
    assert len(result) == 2
    for r in result:
        assert r["state"] == "EXECUTED"


def test_filter_by_state_none(sample_transactions):
    result = filter_by_state(sample_transactions, "PENDING")
    assert result == []


def test_sort_by_date_desc(sample_transactions):
    result = sort_by_date(sample_transactions, descending=True)
    assert result[0]["date"] == "2023-10-01"
    assert result[-1]["date"] == "2023-08-15"


def test_sort_by_date_asc(sample_transactions):
    result = sort_by_date(sample_transactions, descending=False)
    assert result[0]["date"] == "2023-08-15"
    assert result[-1]["date"] == "2023-10-01"
