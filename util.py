import json
from _datetime import datetime

def receive_data(filename):
    """
    получаем данные с файла джейсон
    :param filename: имя файла
    :return: данные из файла джейсон
    """

    with open(filename, 'r', encoding='utf-8') as file:
        data_ex = json.load(file)

    sort_data = sorted(data_ex, key=lambda x: x.get('date', ""), reverse=True)

    return sort_data

def sort_data(data, num):
    """
    Перебираем строки файла
    :param data: данные для выбора
    :param num: строка подсчета
    :return: выводим данные
    """
    count = 0
    new_arr = []
    for str_data in data:
        if str_data["state"].lower() == "EXECUTED".lower():
            new_arr.append(str_data)
            count += 1

            if count == num:
                return new_arr
                break



def format_account(array):
    """
    функция скрывает числа
    :param array: все цифры
    :return: выводим строку
    """
    if array[0] == "Счет":
        str_from = array[1][-4:]
        array[1] = "**" + str_from
    else:
        array[-1] = array[-1][:4] + " " + array[-1][4:6] + "XX" + " " + "XXXX" + " " + array[-1][-4:]

    return " ".join(array)


def refactor_amount(operation_amount):
    """
    функция возвращает сумму денег и валюту
    :return: строка
    """
    res = operation_amount["amount"] + " " + operation_amount["currency"]['name']
    return res



def refactor_string(text):
    result = ""

    # 14.10.2018 Перевод организации
    # Visa Platinum 7000 79** **** 6361 -> Счет **9638
    # 82771.72 руб.
    date_mod = datetime.strptime(text['date'], '%Y-%m-%dT%H:%M:%S.%f')
    date = datetime.strftime(date_mod, '%d.%m.%Y')

    result += date + " " + text["description"] + "\n"
    if "from" in text:
        account_from = format_account(text["from"].split())
        result += account_from + " -> "

    account_to = format_account(text["to"].split())
    result += account_to

    res_amount = refactor_amount(text["operationAmount"])
    result += "\n" + res_amount

    return result
