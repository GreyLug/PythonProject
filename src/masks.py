from typing import Union


# card_number - номер карты
def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция маскировки номера карты"""
    card_number_str = str(card_number)
    if len(card_number_str) != 16:
        return "Введите 16-и значный номер карты"
    elif not card_number_str.isdigit():
        return "Все значения должны быть цифрами"
    else:
        return f"{card_number_str[0:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"


# personal_account - это лицевой счет
def get_mask_account(personal_account: Union[int, str]) -> str:
    """Функция маскировки номера счета"""
    personal_account_str = str(personal_account)
    if len(personal_account_str) != 20:
        return "Введите 20-и значный номер лицевого счета"
    elif not personal_account_str.isdigit():
        return "Все значения должны быть цифрами"
    else:
        return f"**{personal_account_str[-4:]}"


print(get_mask_card_number(1200334599106670))
print(get_mask_account(12345678912345678912))
