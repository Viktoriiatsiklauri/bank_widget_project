from typing import List, Dict, Optional


def filter_by_state(
    operations: List[Dict],
    state: Optional[str] = 'EXECUTED'
) -> List[Dict]:
    """
    Фильтрует операции по значению ключа 'state'.

    :param operations: список словарей с операциями
    :param state: значение для фильтра по ключу 'state', по умолчанию 'EXECUTED'
    :return: список операций с указанным состоянием
    """
    return [op for op in operations if op.get('state') == state]


def sort_by_date(
    operations: List[Dict],
    descending: bool = True
) -> List[Dict]:
    """
    Сортирует операции по дате.

    :param operations: список словарей с операциями
    :param descending: порядок сортировки (по убыванию по умолчанию)
    :return: отсортированный список операций
    """
    return sorted(operations, key=lambda op: op.get('date', ''), reverse=descending)
