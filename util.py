import json
from _datetime import datetime

def download_data(filename):
    """
    function for downloads from file json
    :param filename: file name for downloads
    :return: data from file json
    """

    with open(filename, 'r', encoding='utf-8') as file:
        data_ex = json.load(file)

    sort_data = sorted(data_ex, key=lambda x: x.get('date', ""), reverse=True)

    return sort_data

def select_data(data, num):
    """
    Function select num string, where "state" = "EXECUTED"
    :param data: data for select
    :param num: count string
    :return: select data
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



def refactor_account(array):
    """
    function hides numbers amount
    :param array: array for refactor
    :return: refactor string
    """
    if array[0] == "Счет":
        str_from = array[1][-4:]
        array[1] = "**" + str_from
    else:
        array[-1] = array[-1][:4] + " " + array[-1][4:6] + "XX" + " " + "XXXX" + " " + array[-1][-4:]

    return " ".join(array)


def refactor_amount(operation_amount):
    """
    function return amount of money and currency
    :param operation_amount: data obout operation amount
    :return: string
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
        account_from = refactor_account(text["from"].split())
        result += account_from + " -> "

    account_to = refactor_account(text["to"].split())
    result += account_to

    res_amount = refactor_amount(text["operationAmount"])
    result += "\n" + res_amount

    return result
