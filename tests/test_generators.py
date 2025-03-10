from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

import pytest


# Тест положительного сценария filter_by_currency
@pytest.mark.parametrize(
    "expected_result_1, expected_result_2, expected_result_3",
    [
        (
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            },
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188",
            },
            {
                "id": 895315941,
                "state": "EXECUTED",
                "date": "2018-08-19T04:27:37.904916",
                "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод с карты на карту",
                "from": "Visa Classic 6831982476737658",
                "to": "Visa Platinum 8990922113665229",
            },
        )
    ],
)
def test_filter_by_currency(transactions_test, expected_result_1, expected_result_2, expected_result_3):
    currency_transactions = filter_by_currency(transactions_test)
    assert next(currency_transactions) == expected_result_1
    assert next(currency_transactions) == expected_result_2
    assert next(currency_transactions) == expected_result_3


# Случай, когда транзакции в заданной валюте отсутствуют
def test_not_currency_filter_by_currency(transactions_not_currency):
    currency_transactions = filter_by_currency(transactions_not_currency)
    with pytest.raises(KeyError):
        next(currency_transactions)


# Обработка пустого списка
def test_empty_currency_filter_by_currency(empty_list):
    currency_transactions = filter_by_currency(empty_list)
    with pytest.raises(KeyError):
        next(currency_transactions)


# Тест положительного сценария
@pytest.mark.parametrize(
    "expected_result_1, expected_result_2, expected_result_3, expected_result_4",
    [("Перевод организации", "Перевод со счета на счет", "Перевод со счета на счет", "Перевод с карты на карту")]
)
def test_transaction_descriptions(
    transactions_test, expected_result_1, expected_result_2, expected_result_3, expected_result_4
):
    descriptions = transaction_descriptions(transactions_test)
    assert next(descriptions) == expected_result_1
    assert next(descriptions) == expected_result_2
    assert next(descriptions) == expected_result_3
    assert next(descriptions) == expected_result_4


# Тест с пустым списком
def test_empty_transaction_descriptions(empty_list):
    descriptions = transaction_descriptions(empty_list)
    with pytest.raises(KeyError):
        next(descriptions)


# Тест положительного сценария
def test_card_number_generator():
    new_card_number_generator = card_number_generator(1111112221056789, 1111112221056795)
    assert next(new_card_number_generator) == "1111 1122 2105 6789"


# Провека корректности форматирования номеров карт
def test_type_card_number_generator():
    new_card_number_generator = card_number_generator("11111122210567890", "1111112221056795")
    with pytest.raises(TypeError):
        next(new_card_number_generator)


def test_mistake_value_card_number_generator():
    new_card_number_generator = card_number_generator(11111122210567890, 1111112221056795)
    with pytest.raises(ValueError):
        next(new_card_number_generator)
