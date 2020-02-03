'''Homework Part 2. Recieved 9.1.2020. Same classification system. Each part of the code is separated with "T O D O"
 for highlighting and encapsulated in functions. Have a nice time reading code'''


# TODO 1.Даны два целых числа. Выведите значение нименьшего из них.
# =====================================================================================================================

def two_ints1(num1, num2):
    return (num1 if (num1 < num2) else None) or (num2 if (num1 >= num2) else num1)


def two_ints2(num1, num2):
    return min(list((num1, num2)))


def two_ints3(num1, num2):
    return num1 if num2 - num1 >= 0 else num2


# Output
# print(two_ints1(1,3))
# print(two_ints2(5,1))
# print(two_ints3(3,6))


# TODO 2 и 3. Заданы две клетки шахматной доски. Если они покрашены B один цвет,то выведите слово YES, а если в разные
#  цвета - то NO.Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала
#  для первой клетки, потом для второй клетки.
# =====================================================================================================================

def chess_comparison(num1a, num1b, num2a, num2b):
    return 'Yes' if (num1a + num1b) % 2 == (num2a + num2b) % 2 else 'No'


# print(chess_comparison(1,3,5,6))


# TODO 4. Если вводится температура в градусах по шкале Цельсия, то она переводится в температуру по шкале
#  Фаренгейта. Или наоборот: температура по Фарангейту переводится в температуру по Цельсию.
# =====================================================================================================================
def temp_comp(temp):
    if __name__ == '__main__':
        if 'f' in temp.lower():
            return (int(temp[:-1]) - 32) * 5 / 9, u'\N{DEGREE SIGN}', ' Celsius'
        elif 'c' in temp.lower():
            return (int(temp[:-1]) * 9 / 5) + 32, u'\N{DEGREE SIGN}', 'Fahrenheit'
        else:
            return ValueError('enter temperature, MORON')


# I/O
# temp = input('Please enter your temp with "C" or "F" at the end >>>')
# print(*temp_comp(temp))


# TODO 5. Из списка случайных чисел, определить и вывести на экран нечетные числа.
# =====================================================================================================================

def odds(iter):
    return [i for i in iter if i % 2 != 0] or 'No odds here'


# I/O
# i = range(50)
# b = [2, 4, 6, 8]
# print(odds(i))
# print(odds(b))


# TODO 6. Вводится целое число, обозначающее код символа по таблице ASCII. Определить это код английской буквы или какой
#  -либо иной символ.
# =====================================================================================================================
def char_print(simb):
    print(chr(simb))
    return simb


# char_print(1250)


# TODO 7. Вводятся два целых числа. Проверить делится ли первое на второе. Вывести на экран сообщение об этом, а также остаток
#  (если он есть) и частное (в любом случае)
# =====================================================================================================================

def comp1(num1, num2):
    return num1 / num2, f'{num1} is divisible by {num2}' if num1 % num2 == 0 else (
        num1 / num2 - num1 // num2, num1 / num2, f'{num1} is' \
                                                 f' not divisible by ' \
                                                 f'{num2}')


def comp2(num1, num2):
    if num1 % num2 == 0:
        return num1 / num2, f'{num1} is divisible by {num2}'
    elif num2 % num1 == 0:
        return num2 / num1, f'{num2} is divisible by {num1}'
    else:
        return num1 / num2, f'{num1 // num2} with {num1 / num2 - num1 // num2} left'


# I/O
# print(comp1(8, 4))
# print(comp2(8, 4))


# TODO 8. Написать функцию is_prime, принимающую 1 аргумент - число от 0 до 1000, и
#  возвращающую True, если оно простое, и False - иначе
# =====================================================================================================================

def is_prime(num):  # Prime numbers start from "2" not from 0
    if num in range(2, 1000):
        divisor = 2
        while divisor <= num ** 0.5:
            if num % divisor == 0:
                return False
            divisor += 1
        return True
    else:
        return False  # ("Don't be BamBook")


# [print(i) for i in range(100) if is_prime(i)]


# TODO 9. Написать функцию date, принимающую 3 аргумента - день, месяц, год. Вернуть True. если такая
#  дата есть в нашем календаре, и False иначе.
# =====================================================================================================================

import datetime
import pytz


def time_check_worldwide(day, month: int, year: int(2)):  # pytz covers all DST db,2 DIGITS INPUT!!!!
    try:
        p = (datetime.datetime.strptime(f'{day}/{month}/{year}', '%d/%m/%y'))
        local_with_dst = pytz.utc.localize(p).strftime('%d/%m/%Y')
        return local_with_dst + ' is valid'
    except ValueError:
        return "Such date doesn't exist"


def time_check_simple(day, month, year):
    return f"{day:02}/{month:02}/{year}" if 1 <= day <= 31 and 1 <= month <= 12 else 'You entered some bs boi'


# I/O
# print(time_check_worldwide(29, 2, 34))
# print(time_check_simple(1, 5, 1986))


# TODO 10. Написать функцию season, принимающую 1 аргумент - номер месяца (от 1 до 12), и возвращающую время года, которому
#  этот месяц принадлежит (зима, весна, лето или осень).
# =====================================================================================================================

def season1(mon_num: int) -> [str]:
    if mon_num in range(1, 13):
        seasons = {'Winter': (12, 1, 2), 'Spring': (3, 4, 5), 'Summer': (6, 7, 8), 'Autumn': (9, 10, 11)}
        return [i for i, b in seasons.items() if mon_num in b]
    else:
        raise ValueError('Come on there are 12 months')


def season2(mon_num):
    if mon_num in range(1, 13):
        return 'Spring' if mon_num in range(3, 6) else 'Summer' if mon_num in range(6, 9) else \
            "Autumn" if mon_num in range(9, 12) else 'Winter'
    else:
        raise ValueError('Come on there are 12 months')


# I/O
# print(season1(11))
# print(season2(12))


# TODO 11. Написать функцию, которая вычисляет среднее арифметическое элементов массива, переданного ей в качестве аргумента.
# =====================================================================================================================

import numpy


def array_average1(array):
    try:
        return sum(array) / len(array)
    except:
        return 'Please have array ready with proper values'


def array_average2(array):
    return numpy.average(array)


# I/O
# numb = [1, 2, 3, 33, 5, 6.5]
# numb_math = numpy.array([1, 2, 3, 4, 5, 6.5])  # makes no difference as its only rank 1 array
# print(array_average1(numb))
# print(array_average1(numb_math))
# print(array_average2(numb))
# print(array_average2(numb_math))


# TODO 12. Пользователь вводит число. Сообщить есть ли оно в массиве, элементы коророго расположены по возрастанию
#  значений,а также, если есть, в каком месте находится. При решении задачи использовать бинарный(двоичный) поиск,
#  который оформитьв виде отдельной функции
# =====================================================================================================================
"""One function was written by me, another 'modified'. Mines is clumsy, but serves the purpose"""


def bin_search1(array, nom):  # my binary search without google's help
    array = sorted(array)
    location = []
    for _ in range(0, len(array) ** 2):
        if len(array) >= 4:
            half = round(len(array) / 2)
            if array[half] == nom:
                location.append(half)
                return True, f'array has {nom} on position{location}'
            elif array[half] < nom:
                array = array[half:]
                location.append(half)
            elif array[half] > nom:
                array = array[:half + 1]
                location.append(half)
        else:
            for i in array:
                if i == nom:
                    location.append(half - 1)
                else:
                    if location != []:
                        return True, f'array has {nom} on position {sum(location) + 1}'
                    else:
                        pass
    else:
        return False, f'array has no {nom}'


def binary_search2(arr, l, r, x):  # recursive bin search from google - thx God for google... but it only works for
    # half the results if not <sorted>

    # Check base case
    if r >= l:

        mid = round(l + (r - l) / 2)

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

            # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search2(arr, l, mid - 1, x)
        else:
            return binary_search2(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1


def binary_search3(item_list, item):  # another option for binary search. I like my option better anyway
    first = 0
    last = len(item_list) - 1
    found = False
    while (first <= last and not found):
        mid = (first + last) // 2
        if item_list[mid] == item:
            found = True
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found


# I/O
# a = [1, 2, 3, 4, 4, 4, 4, 4, 6, 3, 3, 1, 2, 3, 5, 2, 2]
a = [1, 5, 2, 3, 33, 59, 67, 12, 4, 45, 8]
# num = int(input('Enter number to check in array >>>'))
num = 4


# FUNCTION 1 output and checks

def i_o(array, nom):
    return bin_search1(sorted(array), nom), sorted(array).index(nom)


#
#
# print(sorted(a))                            #sorted list a
# print(*bin_search1(a, 5))                   #result - True array has 5 on position[6, 4]
# print(sorted(a).index(5))                     #result - 4 (position)
#
#
#
# print(i_o(a, num))                             #((True, 'array has 4 on position 13'), 3)
# f2 I/O
# print(f'{num} is on postion {binary_search2(sorted(a), 0, len(a) - 1, num)}')   # 4 is on postion 3
# print(binary_search3(sorted(a), 4))                    #True


# TODO 13. Поочередно вводится 5 цифр, вывести их сумму(используя for)
# =====================================================================================================================

def sum_row_with_for(mop):
    som = 0
    for i in mop:
        som += i
    return som


# I/O
# nom = list(map(int, input('Please enter numbers separated with "," >> ').split(',')))
# print(sum_row_with_for(nom))


# TODO 14. Даны два целых числа А и В. Выведите все числа от А до В включительно, в порядке возрастания,если
#  А < B, или в порядке убывания в противном случае.
# =====================================================================================================================

def numrange(a, b):
    return [i for i in range(a, b + 1) if a < b] or [i for i in range(a, b - 1, -1) if
                                                     a > b]  # two actions on a<b and a>b


# I/O
# print(numrange(3, 15))
# print(numrange(15,3))


# TODO 15. Есть список a=[1,12,2,33,5,8,3,21,4,2,89]. Выведите все елементы которые меньше 5.
# =====================================================================================================================

a_list = [1, 12, 2, 33, 5, 8, 3, 21, 4, 2, 89]


def unpack_list(list, nom):
    return [i for i in list if i < nom]


# I/O
# print(unpack_list(a_list, 5))


# TODO 16. Циклом for вывести ромб
# =====================================================================================================================

def romb(size):
    [print(str(i * 'o').center(size * 2)) for i in range(1, size + 1, 2)], [print(str(i * 'o').center(size * 2)) for i
                                                                            in range(size, 0, -2)]


# Output
# romb(25)


# TODO 17. Посчитать сумму числового ряда от 0 до 14 включительно. Например 0+..14
# =====================================================================================================================

def sum_list(a, b):
    return sum(
        [i for i in range(a, b + 1) if a < b] or [i for i in range(b, a + 1) if a > b])


# Output
# print(sum_list(0,14)) # 105


# TODO 18. Перемножить все чётные значения в диапазоне от 0 до 436
# =====================================================================================================================
def factor(num):  # recursive
    if num <= 1:
        return num
    else:
        return num * factor(num - 1)


def factor2(num):  # for loop
    fock = 1
    for i in range(1, num + 1):
        fock *= i
    return fock


# Output with comparison
# for i in range(436):
#     print('recursion', factor(i))
#     print('for_loop', factor2(i))


# TODO 19. Задается случайное вещественное число. Определить максимальную цифру этого числа. Пример выполнения: 56.457 Output 7
# =====================================================================================================================

def max_digi1(nom):
    return max(map(int, str(nom).replace('.', '')))  # replace instead of strip or list/remove
    # cause lazy and to remove for floats '.'


def max_digi2(nom):
    max = 0
    for i in str(nom).replace('.', ''):  # getting rid of '.' with floats
        max = int(i) if max < int(i) else max
    return max


# Output
# print(max_digi1(123456312))
# print(max_digi2(123456312))
# print(max_digi1(56.457))

# TODO 20. Генерируется квадратная матрица. Найдите сумму элементов ее главной и побочной диагоналей.
# =====================================================================================================================

import numpy as iamlazy

'''Using numpy instead of row/lists cause its easier and flexible'''
matrix_size = 6  # Custom size of matrix
l = iamlazy.random.randint(0, 9, (matrix_size, matrix_size), int)

res1 = [l[i][i] for i in range(0, matrix_size)]
res2 = [l[i][matrix_size - 1 - i] for i in range(0, matrix_size)]


##Output
# print(l)
# print('*' * 40)
# print('True diag list', *res1)
# print('Sum of true diag', sum(res1))
# # side diag
# print('*' * 40)
# print('Untrue diag', *res2)
# print('Sum of untrue', sum(res2))


# TODO 1. Напишите программу, которая считывает три числа и выводит их сумму. Каждое число записано в отдельной строке.
# =====================================================================================================================

def dif_lanes_sum():
    a, b, c = int(input('Enter three numbers to sum up >>> first\n')), int(input('2nd\tnumber>>>\n')), int(
        input('3d\tnumber>>>\n'))
    return a + b + c


# Output
# print(dif_lanes_sum())


# TODO 2. n школьников делят k яблок поровну, неделящийся остаток отсается в корзинке. Сколько яблок достанется
#  каждомушкольнику? Сколько яблок отсанется в корзинке? Программа получает на вход числа n k должна вывести
#  исколмоеколичество яблок(два числа).
# =====================================================================================================================

def apples(n, k):
    return f"{n} students have {k} apples.  Each student will get {k // n} apples and {k % n} apples will " \
           f"be left in the bucket"


# Output
# print(apples(3,26)) #3 students have 26 apples.  Each student will get 8 and 2 apples will be left in the bucket


# TODO 3. Дано число n. С начала суток прошло n минут. Определите, сколько часов и минуту будут показывать
#  электронныечасы в этот момент. Программа должна вывести два числа: количество часов( от 0 до 23) и количество
#  минут (от 0 до 59).Учтите, что число n может быть больше, чем количество минут в сутках.
# =====================================================================================================================

def time_passed(minutes):
    d, h, m = 0, 0, 0
    if minutes // 1440 >= 1:
        d = minutes // 1440
    minutes -= d * 1440
    if minutes // 60 >= 1:
        h = minutes // 60
    minutes -= h * 60
    m = minutes
    return f'{d} days / {h} hour and {m} minutes. Clock - {h:02}:{m:02} ...' \
           f' {f"{h}:{m:02} AM" if h < 12 else f"{h - 12}:{m:02} PM"}'


# Output
# print(time_passed(5235))   #3 days / 15 hour and 15 minutes. Clock - 15:15 ... 3:15 PM


# TODO 4. Напишите программу, которая приветствует пользователя, выводя слово Hello, введенное имя
#  и zнаки препинания по образцу: <<Hello, Harry!>>
# =====================================================================================================================
def hello(name):
    return '<<Hello, {}!>>'.format(name.title())


# Output
# print(hello('paul')) # <<Hello, Paul!>>


# TODO 5. Напишите программу,которая считывает целое число и выводит текст, аналогичный приведенному в примере(пробелы важны!).
# The next number for the number 1534 is 1535
# The previous number for the number 1534 is 1533
# =====================================================================================================================

def nombres(nom: int):
    return 'The next number for the number {0} is {2}\nThe previous number for the number {0} is {1}'.format(nom,
                                                                                                             nom - 1,
                                                                                                             nom + 1)


# print(nombres(1534)) #The next number for the number 1534 is 1535
#                      #The previous number for the number 1534 is 1533


# TODO 6. В школе решили набрать три новых математических класса. Так как занятия по математике у них проходятв
#  одно и то же время, было решено выделить кабинет для каждого класса и купить в них новые парты.За каждой партой
#  может сидеть не больше двух учеников. Известно количество учащихся в каждом из трёх классов.Сколько всего нужно
#  зкупить парт чтобы их хватило на всех учеников? Программа получает на вход три натуральных числа:количество учащихся
#  в каждом из трех классов.
# =====================================================================================================================

def tables(students):  # rounding up tables for students
    return int(students / 2) + 1 if students % 2 != 0 else int(students / 2)


def math_classes(cl1, cl2, cl3):
    return '{} is the total amount of tables we need to buy for 3 classes\n' \
           'class 1 needs {} tables, class 2 needs {} tables, class 3 needs {} tables'.format(
        ((cl1) + tables(cl2) + tables(cl3)),
        tables(cl1), tables(cl2), tables(cl3))


# Output
# print(math_classes(31, 21, 25))  #55 is the total amount of tables we need to buy for 3 classes
#                                  #class 1 needs 16 tables, class 2 needs 11 tables, class 3 needs 13 tables


# TODO 7. Сделать проверку на тип данных.
# =====================================================================================================================

def type_check1(data, typ):
    return data is typ(data)


def type_check2(data, typ):  # sort of eval transformation - works :)
    return str(typ) == str(type(data))


def type_check3(data, typ):  # simple if comparison to main types
    if 'list' in typ:
        return data is list(data)
    elif 'int' in typ:
        return data is int(data)
    elif 'str' in typ:
        return data is str(data)
    elif 'float' in typ:
        return data is float(data)
    elif 'complex' in typ:
        return data is complex(data)


# Input/Output
# nom, type_nom = eval(input("Please enter your data you want to know the type of >>> ")), eval(input(
#     'Enter type as in "str","int","float",'
#     '"complex","list"... >> '))
# print(type_check1(nom, type_nom))
# print(type_check2(nom, type_nom))
# print(type_check3(nom, str(type_nom)))  # 3d function has EVAL included

# TODO 8. Напишите программу, которая вычисляет сумму, разность, произведение и частное двух числе, разделяя результаты,
#  записанные в одну строчку, значком "@".
# =====================================================================================================================
def multi_op(nom1, nom2):
    return f'{nom1 + nom2} @ {nom1 - nom2} @ {nom1 * nom2} @ {nom1 / nom2}'


# Output
# print(multi_op(44,24))

# TODO 9. Напишите программу, которая считывает три числа и выводит их сумму. Все числа записано в одной строке.
# =====================================================================================================================
def sum_of_str(nombres):
    sum = 0
    for i in str(nombres):
        sum += float(i)
    return sum


def sum_of_str2(nombres):
    return sum([float(i) for i in str(nombres)])


# I/O
# nombresio = input('Please enter the numbers')
# print(sum_of_str(nombresio))
# print(sum_of_str2(nombresio))


# TODO 10. Пользователь вводит имя, записать через запятую, "Hello, "имя пользователя"!"
# =====================================================================================================================
def greeting_fart(name='Your fucken name'):
    return f'Hello,{name}'


# I/O
# namio=input('What is your name hombre, amigo?')
#
# print(greeting_fart(namio))
# print(greeting_fart())

# TODO =================================================================================================================
'''Thanks for reading. Here's a cookie '''

# print('This is a checkmark to mark that you are done reading!', u'\u2713')
