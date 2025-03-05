import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "invalid_date", ["18:35:29.512364", "2025-07-03", "2019/07/03T18:35:29", "03-07-2019T18:35:29"]
)
def test_get_date_mistake_value(invalid_date):
    with pytest.raises(ValueError):
        get_date(invalid_date)


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_get_date_empty_value():
    with pytest.raises(ValueError):
        get_date("")


@pytest.mark.parametrize(
    "card_or_account_bank, expected_result",
    [
        ("Visa Classic 1234567891112131", "Visa Classic 1234 56** **** 2131"),
        ("MasterCard 1234567891112131", "MasterCard 1234 56** **** 2131"),
        ("Maestro 1234567891112131", "Maestro 1234 56** **** 2131"),
        ("Счет 12345678911121319876", "Счет **9876"),
    ],
)
def test_mask_account_card(card_or_account_bank, expected_result):
    assert mask_account_card(card_or_account_bank) == expected_result


@pytest.mark.parametrize(
    "mistake_value",
    [
        "Vi Classic 123456781112131",
        "MasterCard 12345891112131",
        "stro 1234567891112131",
        "Счееет 12345678911121319876",
    ],
)
def test_mask_account_card_mistake_value(mistake_value):
    with pytest.raises(ValueError):
        mask_account_card(mistake_value)
