from datetime import datetime

from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(data: str) -> str:
    """
    Определяет, что за данные пришли — карта или счет,
    и применяет соответствующую маску.

    - Карта: 16+ символов, оставляем первые 4 и последние 4
    - Счет: меньше 16 символов, оставляем только последние 4
    """
    if len(data) >= 16:
        # карта
        return get_mask_card_number(data)
    else:
        # счет
        return get_mask_account(data)


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата ISO с временем (например, "2024-03-11T02:26:18.671407")
    в формат "ДД.ММ.ГГГГ" (например, "11.03.2024").

    Аргументы:
        date_str (str): Исходная строка даты.

    Возвращает:
        str: Дата в формате "ДД.ММ.ГГГГ".
    """
    dt = datetime.fromisoformat(date_str)
    return dt.strftime("%d.%m.%Y")
