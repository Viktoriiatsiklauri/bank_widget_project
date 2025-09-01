import pytest
from src.generators import (card_number_generator, filter_by_currency,
                            transaction_descriptions)

# -------------------- Фикстуры --------------------


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2023-08-15",
            "operationAmount": {"amount": "100", "currency": {"code": "USD"}},
            "description": "Перевод организации",
        },
        {
            "id": 2,
            "state": "EXECUTED",
            "date": "2023-08-16",
            "operationAmount": {"amount": "200", "currency": {"code": "EUR"}},
            "description": "Перевод со счета на счет",
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2023-08-17",
            "operationAmount": {"amount": "300", "currency": {"code": "USD"}},
            "description": "Перевод с карты на карту",
        },
    ]

# -------------------- Тест filter_by_currency --------------------


@pytest.mark.parametrize("currency_code,expected_ids", [
    ("USD", [1, 3]),
    ("EUR", [2]),
    ("RUB", []),
])
def test_filter_by_currency(sample_transactions, currency_code, expected_ids):
    results = list(filter_by_currency(sample_transactions, currency_code))
    result_ids = [tx["id"] for tx in results]
    assert result_ids == expected_ids


# -------------------- Тест transaction_descriptions --------------------
def test_transaction_descriptions(sample_transactions):
    gen = transaction_descriptions(sample_transactions)
    descriptions = [next(gen) for _ in range(len(sample_transactions))]
    expected = [tx["description"] for tx in sample_transactions]
    assert descriptions == expected


def test_transaction_descriptions_empty():
    gen = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(gen)


# -------------------- Тест card_number_generator --------------------
@pytest.mark.parametrize("start,stop,expected", [
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    (998, 1000, ["0000 0000 0000 0998", "0000 0000 0000 0999", "0000 0000 0000 1000"]),
])
def test_card_number_generator(start, stop, expected):
    gen = card_number_generator(start, stop)
    results = list(gen)
    assert results == expected


def test_card_number_generator_empty():
    gen = card_number_generator(5, 3)  # start > stop
    assert list(gen) == []
