from collections.abc import Iterator


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генератор номеров карт в формате XXXX XXXX XXXX XXXX.

    :param start: начальное значение (например, 1)
    :param stop: конечное значение (например, 5)
    :return: итератор по номерам карт
    """
    for number in range(start, stop + 1):
        # Преобразуем число в строку с ведущими нулями (16 символов)
        card_str = str(number).zfill(16)
        # Форматируем с пробелами
        formatted = " ".join([card_str[i:i + 4] for i in range(0, 16, 4)])
        yield formatted
