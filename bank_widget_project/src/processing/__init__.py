# bank_widget_project/src/processing/__init__.py

from datetime import datetime
from typing import Dict
from typing import List


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список операций по значению state.
    :param data: список словарей с операциями
    :param state: значение поля 'state', по которому фильтруем (по умолчанию 'EXECUTED')
    :return: отфильтрованный список операций
    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(transactions: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по дате.

    :param transactions: список словарей с ключом 'date'
    :param descending: порядок сортировки (по убыванию, по умолчанию True)
    :return: новый отсортированный список словарей
    """
    return sorted(
        transactions,
        key=lambda x: datetime.fromisoformat(x['date']),
        reverse=descending
    )
