import os


def add(a, b):
    return a + b


def div(a, b):
    return a / b


obj = {
    '+': add,
    '/': div
}


def user_input():
    a = float(input('>>> '))
    oper = input(' '.join([oper for oper in obj.keys()]))
    b = float(input('>>> '))

    return {
        'first': a,
        'oper': oper,
        'second': b
    }


def write_text_to_file(filename, text):
    """Функция для записи в	файл filename строки text"""

    # Открытие файла для записи
    f = open(filename, 'a')
    # Запись строки text в файл
    f.write(str(text) + '\n')
    # Закрытие файла
    f.close()


def main():
    try:
        user_data = user_input()
        result_number = obj[user_data['oper']](user_data['first'], user_data['second'])
        result_str = '{first} {oper} {second} = {result}' \
            .format(first=user_data['first'],
                    oper=user_data['oper'],
                    second=user_data['second'],
                    result=result_number)
    except ZeroDivisionError as e:
        result_str = str(e)
    filename = os.path.join('result.txt')
    write_text_to_file(filename=filename, text=result_str)
    print(result_str)


main()
