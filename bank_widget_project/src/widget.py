from datetime import datetime

from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(info: str) -> str:
    """
    Маскирует номер банковской карты или счета, используя функции из модуля masks.

    Аргументы:
        info (str): Строка с типом карты/счета и номером, например,
                    "Visa Platinum 7000792289606361" или "Счет 73654108430135874305".

    Возвращает:
        str: Строку с типом и замаскированным номером.
    """
    # Разделяем строку на слова
    parts = info.split()

    # Последний элемент — номер карты/счета
    number = parts[-1]

    # Всё, что до номера — тип
    card_type = " ".join(parts[:-1])

    if card_type.lower() == "счет":
        masked = get_mask_account(number)
    else:
        masked = get_mask_card_number(number)

    return f"{card_type} {masked}"


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
