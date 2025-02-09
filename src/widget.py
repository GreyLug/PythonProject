from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account: str) -> str:
    """Функция которая номер карты с указанием её типа и счет"""
    card_or_account_list = card_or_account.split()
    if "Счет" in card_or_account_list:
        return f"Счет {get_mask_account(card_or_account_list[1])}"
    elif "MasterCard" in card_or_account_list or "Maestro" in card_or_account_list:
        return f"{card_or_account_list[0]} {get_mask_card_number(card_or_account_list[1])}"
    elif "Visa" in card_or_account_list:
        numbers_card = []
        name_card = []
        for i in card_or_account_list:
            if i.isdigit():
                numbers_card.append(i)
            if i.isalpha():
                name_card.append(i)
        str_numbers_card = "".join(numbers_card)
        return f"{name_card[0]} {name_card[1]} {get_mask_card_number(str_numbers_card)}"


def get_date(my_date: str) -> str:
    """Функция конвертирования даты"""
    date_obj = datetime.strptime(my_date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")


print(get_date("2024-03-11T02:26:18.671407"))
print(mask_account_card("Visa Classic 1234567891112131"))
print(mask_account_card("MasterCard 1234567891112131"))
print(mask_account_card("Maestro 1234567891112131"))
print(mask_account_card("Счет 12345678911121319876"))
