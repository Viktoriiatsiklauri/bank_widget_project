def get_mask_card_number(card_number: int) -> str:
    """
    Маскирует номер карты в формате: XXXX XX** **** XXXX.
    Показываются первые 6 и последние 4 цифры.
    """
    card_str = str(card_number)
    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def get_mask_account(account_number: int) -> str:
    """
    Маскирует номер счёта в формате: **XXXX.
    Показываются только последние 4 цифры.
    """
    account_str = str(account_number)
    return f"**{account_str[-4:]}"
