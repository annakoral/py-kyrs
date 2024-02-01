from util import refactor_account, refactor_amount, refactor_string


def test_refactor_account():
    ar = ["Счет", "90424923579946435907"]
    ar2 = ["Maestro", "3928549031574026"]
    assert refactor_account(ar) == "Счет **5907"
    assert refactor_account(ar2) == "Maestro 3928 54XX XXXX 4026"


def test_refactor_amount():
    s = {
        'amount': '31957.58',
        'currency': {
            'name': 'руб.',
            'code': 'RUB'
            }
        }
    assert refactor_amount(s) == '31957.58 руб.'


def test_refactor_string():
    text1 = {
        "id": 863064926,
        "state": "EXECUTED",
        "date": "2019-12-08T22:46:21.935582",
        "operationAmount": {
            "amount": "41096.24",
            "currency": {
                "name": "USD",
                "code": "USD"
                }
            },
        "description": "Открытие вклада",
        "to": "Счет 90424923579946435907"
        }
    text2 = {
        "id": 863064926,
        "state": "EXECUTED",
        "date": "2019-12-08T22:46:21.935582",
        "operationAmount": {
            "amount": "41096.24",
            "currency": {
                "name": "USD",
                "code": "USD"
                }
            },
        "description": "Открытие вклада",
        "to": "Счет 90424923579946435907",
        "from": "Maestro 90424923579946439034"
        }
    assert refactor_string(text1) == '''08.12.2019 Открытие вклада
Счет **5907
41096.24 USD'''
    assert refactor_string(text2) == '''08.12.2019 Открытие вклада
Maestro 9042 49XX XXXX 9034 -> Счет **5907
41096.24 USD'''