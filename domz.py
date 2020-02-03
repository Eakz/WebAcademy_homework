'''Выполнил все задания в функциях что б если что можно было вызвать не затемняя, методы ввода и вывода затемнены
    Все пронумерованные функции - это варианты написания одной и той же задачи. Легкий переход между заданиями -
    коммент-функция "TO_ DO" '''


# TODO 1 Напишите программу, которая спрашивает у пользователя два слова и выводит их разделёнными запятой.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def two_words(w1, w2):
    return w1 + ', ' + w2


# I/O
# wor1 = input('Enter 2 words pressing enter after each >>>')
# wor2 = input('2nd>>>>')
# print(two_words(wor1, wor2))
# print('-' * 40)


# TODO 2 Напишите программу, которая запрашивает три целых числа a, b и x и выводит True, если x лежит между a и b, иначе – False.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def compare(a, b, x):
    return a < x < b


# I/O
# n1 = int(input('#1 >>> '))
# n2 = int(input('#2 >>> '))
# n3 = int(input('#3 >>> '))
# print('{0} is less then {2} and {1} larger then {2} is '.format(n1, n2, n3), compare(n1, n2, n3), )
# print('-' * 40)

# TODO 3 Напишите программу, которая решает квадратное уравнение ax^2 + bx + c = 0 Значения a, b и c вводятся с клавиатуры.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import sys


# INPUT check
# while True:
#     try:
#         a = int(input("Enter  of a(cannot be equal to zero), b and c for Quadratic equation a >>> : "))
#         b = int(input("Enter b >>> : "))
#         c = int(input("Enter c >>> : "))
#         break
#
#     except ValueError:
#         print('-' * 40)
#         print('Value Error - please enter actual numbers from the beginning! bitch')

def quadratic(a, b, c):
    if a == 0:
        print('Wrong turn boi')
        sys.exit('This is so wrong, I told u "a" cannot be equal zero')

    d = b ** 2 - 4 * a * c  # discriminant

    if d < 0:
        print("ax^2 + bx + c = 0 has no solution")
    elif d == 0:
        x = -b / 2 * a
        print("ax^2 + bx + c = 0 solutions:  {}".format(x))
    else:
        x_1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
        x_2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
        print(f"This equation has two solutions: {x_1} and {x_2}")


# OUTPUT
# quadratic(a, b, c)
# TODO 4 Напишите программу, которая запрашивает у пользователя радиус круга и выводит его площадь. Формула площади круга S=pi*R^2 .
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import math  # already imported earlier, but still just as a reminder that it should be present


# Input
# radiance=int(input('What is the radius of your circle, boi?'))

def circle_square(rad):
    return math.pi * rad ** 2  # parentheses are not necessary due to the operator precedence


# OUTPUT
# print(circle_square(radiance))
# TODO 5 Напишите программу-калькулятор, в которой пользователь сможет ввести выбрать операцию, ввести необходимые числа и
# получить результат. Операции, которые необходимо реализовать: сложение, вычитание, умножение, деление, возведение в
# степень, синус, косинус и тангенс числа.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


'''I decided not to write code for obvious if..elif add/sub/mul etc...'''
import math

'''Input is below the functions'''


def calc1(num1, op, num2=None):
    e = 2.718281828459045
    if op.lower() == 'sin':  # can also be done with math.sin
        return (e ** (num1 * 1j)).imag
    elif op.lower() == 'cos':  # can also be done with math.cos
        return (e ** (num1 * 1j)).real
    elif op.lower() == 'tan':  # coundn't find tan formula and yes I am bad in math
        return math.tan(num1)
    return eval(f'{num1}{op}{num2}')


def calc2(num1, op, num2=1):  # second option of calculator
    l_op = {'+': (num1 + num2), '-': (num1 - num2), '/': (num1 / num2), '*': (num1 * num2), '**': (num1 ** num2),
            'sin': math.sin(num1),
            'cos': math.cos(num1), 'tan': math.tan(num1)}
    return l_op[op]


'''output with input control, showed input control in exercise #5'''
# I/O
# while True:
#     try:
#         num1=float(input('Please enter two numbers and an operation. \n >>> Num1>>> '))
#         op = input('Operations: + , - , / , * , ** , sin , cos , tan >>>')
#         break
#     except ValueError or KeyError:
#         print("Please enter the value you are asked for, don't invent the fucking wheel. Damn mongoloid \n")
#
# if op.lower() in 'sincostan':
#     print(f'Getting your {op}')
#     num2=1
# else:
#     num2 = float(input('num2 >>>'))
#     print(f'Performing your {op}')
#
# print(f'the result of you operation is {calc2(num1,op.lower(),num2)}')
#
# print('-'*40)

# TODO 6 Напишите программу, которая спрашивает у пользователя его имя, и если оно совпадает с вашим, выдаёт определённое сообщение.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''Sorry for explicit language'''


def name_checker(name):
    if 'paul' in name.lower():
        if name == 'Paul':
            print('Yeh, baby its exactly my name')
        else:
            print('Yes, this is looks like my name')
    else:
        print('Not even close, bitch')


#
# OUTPUT
# nm=input('What is my name?')
# name_checker(nm)


# TODO 7 Даны числа a и b (a < b). Выведите сумму всех натуральных чисел от a до b (включительно).
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def numrange(a, b):
    return sum(
        [i for i in range(a, b + 1) if a < b] or [i for i in range(b, a + 1) if a > b])  # two actions on a<b and a>b


# I/O
# nom1 = int(input('num1>>> '))
# nom2 = int(input('num2>>> '))
# print(numrange(nom1, nom2))


# TODO 8 Факториалом числа n называется число 𝑛!=1∙2∙3∙…∙𝑛. Создайте программу, которая вычисляет факториал введённого пользователем числа.(цыкл!)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def fac1(n):  # Recursion
    if n == 1:
        return 1
    return n * fac1(n - 1)


def fac2(n):  # non-recursion
    fact = 1
    for num in range(1, n + 1):
        fact *= num
    return fact


# OUTPUT
# print(fac2(6))
# print(fac1(4))

# TODO 9 Используя вложенные циклы и функции print(‘*’, end=’’), print(‘ ‘, end=’’) и print() выведите на экран прямоугольный треугольник.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def triangle1():
    for i in range(1, 30, 2):  # triangle with l-b allighnment
        print(i * '*', end='')
        print()
    print('=' * 35)
    for i in range(1, 30, 2):  # triangle with r-t allignment
        print((i * ' ' + (30 - i) * '*'))
    print('=' * 35)
    for i in range(30, 1, -2):  # triangle with l-t allignment
        print(i * '*')
    print('*')
    print('=' * 35)
    print(29 * ' ' + '*', end='')
    for i in range(30, 1, -2):  # triangle with r-b allignment
        print((i * ' ' + (30 - i) * '*'))
    print('=' * 35)


def triangle2():
    [print(i * '*') for i in range(1, 30, 2)]  # l-b
    print('=' * 35 + '\n')
    [print((i * ' ' + (30 - i) * '*')) for i in range(1, 30, 2)]  # r-t
    print('=' * 35 + '\n')
    ([print(i * '*') for i in range(30, 1, -2)] + [print(i) for i in ["*"]])  # l-t
    print('=' * 35 + '\n')
    [print(29 * ' ' + '*', end='')] + [print((i * ' ' + (30 - i) * '*')) for i in range(30, 1, -2)]  # r-b
    print('=' * 35 + '\n')


# Output
# triangle1()
# triangle2()

# TODO 10 Функция принимает 2 параметра - высоту и ширину прямоугольника. Рисует прямоугольник :)) и возвращает True если
#  был нарисован квадрат и False - если нет.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def square_pr_draw(a, b):
    for y_axis in range(0, a):
        print()
        for x_axis in range(0, b):
            print('o', end='')
    if a == b:
        print('\n \t \tthis is square even thos it doesn"t look like it')
        return True
    else:
        print('\n \t \t This is not square, bitch')
        return False


# Output
# print(square_pr_draw(4,4))
# print('-'*40+'\n')
# print(square_pr_draw(5,3))

# TODO 11     Создайте функцию, которая выводит приветствие для пользователя с заданным именем. Если имя не указано,
#  она должна выводить приветствие для пользователя с Вашим именем.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def greeting():
    name = input('What is ur name?')
    if name == '':
        name = 'Paul'
    print(f'Hello mein liebe,{name}')


def greeting2(name='Paul'):
    print(f'Hello mein liebe,{name}')


# #I/O
# name = input('What is ur name?')
# if name:
#     greeting2(name)
# else:
#     greeting2()
#
# greeting()


# TODO 1    Фунция принимает любое число и возвращает суму всех цыфр числа.
#     Примеры вызова:
#     sum_digit_from_number(34) => 7
#     sum_digit_from_number(2) => 2
#     sum_digit_from_number(1342) => 10
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def digit_sum1(num):
    nomero = 0
    for i in str(num):
        nomero += int(i)
    return nomero


def digit_sum2(num):
    return sum(map(int, str(num)))


# print(digit_sum1(87))
# print(digit_sum2(347))

# TODO 2 Пользователь делает вклад в размере N $ сроком на years лет под 11.5% годовых (каждый год размер его вклада
#  увеличивается на 11.5%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
#  Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя через years лет.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def investment(amount: int, time, rate) -> float:  # amount in int(.2f point ignored for precision),
    # time in years,rate in percentage e.g 11.5 for 11.5%
    time_round = int(time)  # how many whole years are there
    for years in range(1, (time_round + 1)):
        amount += (amount * (rate / 100))
    amount += amount * (rate / 100) * (time - time_round)  # getting extra amount if time imput was float(e.g 1.6 years)
    return round((amount / 100), 2)  # converting int to float to get $ value instead of Cents


#
# #Output
# print(investment(50000, 4.5, 11.5))  # displays value of your
# investment account with starting balance of $500.00 in 2 years
# with pro rate of 11.5%/year = result $615.00

# TODO 3 Написать функцию проверки пароля пользователя при регистрации. Что она должна делать.
#     Пользователь вводит два раза пароль(стандартная регистрация)
#  Возвращает True , если пользователь ввел два раза пароль верно и есть как минимум 2(заглянуть на функции ord() и chr())
#  символа с большой буквы. Иначе-False.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''I didnt find any efficient way to use ord() and chr() for this'''


def password_check1(input1, input2):
    upper_count = 0
    if str(input1) == str(input2):
        for simb in input1:
            if simb.isupper():
                upper_count += 1
    if upper_count >= 2:
        return True
    else:
        return False


def password_check2(input1, input2):  # short version of previous functino with comprehension

    return 2 <= sum(1 for simb in input1 if input1 == input2 if simb.isupper())
    # return 2 <= sum(1 for simb in input1 if input1 == input2 if simb in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ') ##2nd option
    # return 2 <= sum(1 for simb in input1 if input1 == input2 if simb ==simb.upper()) ##3d option


# print(password_check1('AMGddA', 'AMGddA'))
# print(password_check2('OMGthisispassword', 'OMGthisispassword'))

# TODO 4  Написать функцию проверки года на высокосный. Возращает True- если высокосний.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def leap_year_check(year):
    return 0 == year % 4, print(f'it is {0 == year % 4} that {year} is leap year')


# leap_year_check(2016)
