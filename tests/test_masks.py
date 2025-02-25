import pytest

from src.masks import get_mask_account, get_mask_card_number


# тест с положительным сценарием
@pytest.mark.parametrize(
    "nomber_card, expected_result",
    [
        ("1234567891011121", "1234 56** **** 1121"),
        ("2003004005556677", "2003 00** **** 6677"),
        ("3458971560114489", "3458 97** **** 4489"),
    ],
)
def test_get_mask_card_number(nomber_card, expected_result):
    assert get_mask_card_number(nomber_card) == expected_result


# тест с неверными значениями
@pytest.mark.parametrize("mistake_value", [(-1), (0), (20)])
def test_get_mask_card_number_mistake(mistake_value):
    with pytest.raises(TypeError):
        get_mask_card_number(mistake_value)


# тест с граничным случаем
def test_get_mask_card_number_boundary_case():
    assert get_mask_card_number("123456789012345678") == "1234 56** **** 3456 78"


# тест с положительным сценарием
def test_get_mask_account():
    assert get_mask_account("12345678912345678901") == "**8901"


@pytest.mark.parametrize("mistake_value", [(-1), (0), (20)])
def test_get_mask_account(mistake_value):
    with pytest.raises(TypeError):
        get_mask_account(mistake_value)
