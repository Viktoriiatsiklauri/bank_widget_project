from typing import Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    """
    Фильтрует транзакции по валюте.

    :param transactions: список транзакций (словарей)
    :param currency: код валюты (например, "USD")
    :return: итератор по транзакциям с указанной валютой
    """
    for tx in transactions:
        if tx.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield tx


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """
    Генератор, возвращающий описания транзакций.

    :param transactions: список транзакций (словарей)
    :return: итератор по строкам описаний
    """
    for tx in transactions:
        if "description" in tx:
            yield tx["description"]
