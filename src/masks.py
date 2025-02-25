def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера карты"""
    if not isinstance(card_number, str):
        raise TypeError("card_number должен быть строкой")
    elif len(card_number) == 16:
        return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    elif len(card_number) == 18:
        return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-6:-2]} {card_number[-2:]}"
    else:
        raise ValueError("Введите 16-и значный номер карты или 18-ти значный номер карты")


# personal_account - это лицевой счет
def get_mask_account(personal_account: str) -> str:
    """Функция маскировки номера счета"""
    if not isinstance(personal_account, str):
        raise TypeError("personal_account должен быть строкой")
    elif len(personal_account) != 20:
        raise ValueError("Введите номер счета состоящий из 20-ти цифр")
    else:
        return f"**{personal_account[-4:]}"
