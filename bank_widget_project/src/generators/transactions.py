from typing import Iterator


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """
    Генератор, возвращающий описания транзакций.

    :param transactions: список транзакций (словарей)
    :return: итератор по строкам описаний
    """
    for tx in transactions:
        if "description" in tx:
            yield tx["description"]
