import pytest

from src.widget import get_date
from src.widget import mask_account_card


@pytest.mark.parametrize("data, expected", [
    ("1234567812345678", "1234 ** ** 5678"),
    ("40817810099910004312", "4081 ** ** 4312"),
])
def test_mask_account_card(data, expected):
    assert mask_account_card(data) == expected


@pytest.mark.parametrize("date_str, expected", [
    ("2023-08-15T12:34:56", "15.08.2023"),
    ("2022-01-01T00:00:00", "01.01.2022"),
])
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected
