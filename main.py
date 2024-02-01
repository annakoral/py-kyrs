from util import receive_data, refactor_string, sort_data


def main():
    count_str = 5

    filename = "operations.json"
    data = receive_data(filename)
    data_select = sort_data(data, count_str,)

    for item in data_select:

        try:
            str_amount = refactor_string(item)
            if str_amount:
                print(str_amount)
                print()
                str_amount = ""
        except:
            pass


if __name__ == '__main__':
    main()