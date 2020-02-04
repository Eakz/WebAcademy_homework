import re
import random


# Задачи по спискам и функциям:
# TODO 1. Ввести строку, в которой записана сумма натуральных чисел, например, ‘1+25+3’. Вычислите это выражение.
#  Работать со строкой, как со списком.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def natural_sum1(stri):
    return eval(stri)


def natural_sum2(stri):  # searches for digit sequence
    suml = 0
    nom = ''
    for i in stri:
        if i.isdigit():
            nom += i
        else:
            suml += int(nom)
            nom = ''
    suml += int(nom)
    return suml


def natural_sum3(stri):
    match = re.findall(r'[0-9]+', stri)
    return sum([int(i) for i in match])


def natural_sum4(stri):
    return sum([int(i) for i in stri.split('+')])


# Output
# print('1+25+3 summarizing raw string with eval() = ', natural_sum1('1+25+3'))
# print('1+25+3 summarizing raw string with for loop expecting random numbers = ', natural_sum2('1+25+3'))
# print(f'1+25+3 summarizing raw string with regex into sum(list()) = {natural_sum3("1+25+3")}')
# print(f'1+25+3 summarizing raw string with split() method into list !!!only string with numbers '
#       f'and "+" allowed = {natural_sum4("1+25+3")}')


# TODO 2. Дан список из 5 различных элементов. Используя функции (не использовать цикл), необходимо найти и вывести:
#  • минимальный и максимальный элементы списка;
#  • сумму и среднее арифметическое;
#  • второй минимальный элемент (второй по минимальности).
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def five_elements(list_):
    return f'min is {min(list_)},\nmax is {max(list_)},\nsum is {sum(list_)},\naverage is {sum(list_) / len(list_)}, '


def second_to_min(list_):
    list_ = set(list_)  # removing the chance of duplicates
    list_.remove(min(list_))  # removing the lowest number
    return f'Second to min is {min(list_)}'


#
downlisto = [3, 1, 2, 5, 1, 231, 523, 22, 31]


# Output
# print(five_elements(downlisto), second_to_min(downlisto),sep='\n')


# TODO 3. Проверить, является ли заданное слово палиндромом.
# Примечание:
# • Пример палиндрома: казак, ABBA
# • Использовать функции.
# • Поскольку при присваивании одного списка другому, изменение первого ведет
# к аналогичному изменению второго списка, то необходимо использовать копию (copy)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def palindrome1(word):  # slicing method
    return f'The statement that "{word}" is palindrome is {word == word[::-1]}'


def palindrome2(word):  # copy method
    w1, w2 = list(word), list(word).copy()
    w2.reverse()
    return f'The statement that "{word}" is palindrome is {w1 == w2}'


# Output
# print('With slicing\t-', palindrome1('ABBA'))
# print('With list copy\t-', palindrome2('ABBA'))


# TODO 4. Найдите в списке все простые числа и скопируйте их в новый список.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def is_prime(nom):
    for i in range(2, int(nom ** 0.5) + 1):
        if nom % i == 0:
            return False
    return True


k = [random.randint(0, 100) for _ in range(50)]


def prime_relocate(listik):
    return [i for i in listik if is_prime(i)]


# Output

# print(f'{k} \n {"="*len(k)*2}\nSorted,filtered by primes = {sorted(prime_relocate(k))}')


# TODO 5. Найти среднее арифметическое всех элементов списка.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def average(list_):
    return sum(list_) / len(list_)


# print('Average of a randomly generated list "k" is {}'.format(average(k)))


# TODO 6. Запросить у пользователя элемент списка и вывести его индекс.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def index1(list_, elem_):
    return list_.index(elem_)


def index2(list_, elem_):
    return [i for i in range(0, len(list_)) if list_[i] == elem_]


val = 4
listo = [1, 3, 4, 5, 6, 3, 2, 4, 9]
# print('Using built_in Value {} in the list: {}\n has index {}'.format(val, listo, index1(listo, val)))
# print('Using self_made Value {} in the list: {}\n has indexes {}'.format(val, listo, index2(listo, val)))


# TODO 7. Нaпишите прогрaмму, котoрая принимает на вход спиcок чисел в одной cтроке и выводит на экран в oдну строкy
#  значения, котoрые повторяются в нём бoлее одного раза.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


stringo = 'pizdetsbaradetsvpopukupets'
numbero = [1, 23, 4, 51, 23, 4, 5, 12, 3, 4, 51, 2, 3, 4, 51, 2, 3, 4, 51, 12, 23, 4, 5, 12, 3, 4, 5, 12, 6562, 3, 1, 2,
           4, 2, 35]


def over_two(stri):
    return set([i for i in stri if stri.count(i) >= 2])


# Output
# print(*over_two(stringo), sep=' | ')    # a | u | t | p | e | s | d
# print(*over_two(numbero), sep=' | ')    # 1 | 2 | 3 | 4 | 5 | 12 | 51 | 23


# TODO 8. Написать функцию XOR_cipher, принимающая 2 аргумента: строку,
# которую нужно зашифровать, и ключ шифрования, которая возвращает строку,
# зашифрованную путем применения функции XOR (^) над символами строки с ключом.
# Написать также функцию XOR_uncipher, которая по зашифрованной строке и ключу восстанавливает исходную строку.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def crypting_and_decrypting(stri, key_):  # home_made version without google
    encrypted = []
    for char in stri:
        for val, val2 in zip((char * len(key_)), key_):
            temp = ''.join(str(ord(val) ^ ord(val2)))
        encrypted.append(chr(int(temp)))
    encrypted = ''.join(encrypted)
    return encrypted


# Output
# print(crypting_and_decrypting('Hi, hi! I need mohney! NOW!!! FUcken ASAP', '103'))
# print(crypting_and_decrypting('{Z[Zz]VVW^\[]VJ}|dufPXV]r`rc', '103'))
# print(crypting_and_decrypting('pizdets borodets', '101'))
# print(crypting_and_decrypting('AXKUTEBS^C^UTEB','101' ))


# TODO 9. Найти наименьшее общее кратное (НОК) пары чисел по формуле
# НОК = ab / НОД(a, b),
# где a и b - это натуральные числа, НОД - наибольший общий делитель.\
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def n_o_k(a, b):  # I think I followed
    if a >= b:
        nod = max([i for i in range(1, a) if a % i == 0 == b % i])
    else:
        nod = max([i for i in range(1, b) if a % i == 0 == b % i])
    return a * b / nod, str(nod)


# Input
a = 12
b = 8
nok, nod = n_o_k(a, b)


# Output
# print('NOK for number {} and {} is {} where NOD is {}'.format(a, b, nok, nod))
## NOK for number 12 and 8 is 24.0 where NOD is 4


# TODO 10. Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2),
# вычисляющая расстояние между точкой (x1,y1) и (x2,y2). Считайте четыре действительных числа и выведите
# результат работы этой функции.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


x1, y1, x2, y2 = 33, 44, 55, 78


# Output

# print('Distance btwn point_I at x{}:y{} and point_II x{}:y{} is {}'.format(x1, y1, x2, y2, distance(x1, y1, x2, y2)))


# TODO 11. Напишите функцию capitalize(), которая принимает слово из маленьких латинских букв и возвращает
# его же, меняя первую букву на большую.
# Например, print(capitalize('word')) должно печатать слово Word.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def capitalize1(word):
    return word.title()


def capitalize2(word):
    return word[0].upper() + word[1:]


def capitalize3(word):
    return chr(ord(word[0]) - 32) + word[1:]


# Output
# print(capitalize1('pizdets'))
# print(capitalize2('pizdets'))
# print(capitalize3('pizdets'))


# TODO 12. Дана последовательность целых чисел, заканчивающаяся числом 0. Выведите эту последовательность
#  в обратном порядке.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


popandopalist = [3, 4, 1, 23, 4, 5, 1, 2, 0]


def sequence_reverse1(list_):
    if list_[-1] == 0:
        return list_[::-1]
    else:
        return 'U dont nou dah way'


def sequence_reverse2(list_):
    return list(reversed(list_))


def sequence_reverse3(list_):
    list_.reverse()
    return list_


# Output
# print(sequence_reverse1(popandopalist))
# print(sequence_reverse2(popandopalist))
# print(sequence_reverse3(popandopalist))


# Задачи словарям:
# TODO 1. В единственной строке записан текст. Для каждого слова из данного текста подсчитайте, сколько
# раз оно встречалось в этом тексте ранее.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def word_count(stri):
    table = {}
    for word in stri.lower().split():
        if not word in table:
            table[word] = stri.count(word)
    return table


# Input
teK_st = 'Yagoda  Poli poli poli polina v sadu yagoda malina malina fock you you moder focker'
# print()
# Output
# [print(f'Word |"{a:8}"| is used [{word_count(teK_st)[a]}] times') for a in  # print with SORTED by amount
#  sorted(word_count(teK_st), key=word_count(teK_st).get, reverse=True)]


# TODO 2. Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову.
#  Все слова в словаре различны.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


'''I don't really understand what to do here'''
slovar = {'synonnym1': 'synonnym1a', 'synonnym2': 'synonnym2a', 'synonnym3': 'synonnym3a'}

# TODO 3. Создайте словарь, связав его с переменной school, и наполните данными,
# которые бы отражали количество учащихся в разных классах (1а, 1б, 2б, 6а, 7в и т. п.).
# Внесите изменения в словарь согласно следующему: а) в одном из классов изменилось количество учащихся,
# б) в школе появился новый класс, с) в школе был расформирован (удален) другой класс.
# Вычислите общее количество учащихся в школе.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


school = {'1a': 25, '1b': 23, '2b': 22, '6a': 28, '7v': 18, '11a': 35}
# I/O
# print(*[f'Class |{a:3}| has |{b:02}| students' for a, b in school.items()], sep='\n', end=f'\n{"*" * 40}\n')
# school['1a'] = 45  # changing value of number of students
# print(*[f'Class |{a:3}| has |{b:02}| students' for a, b in school.items()], sep='\n', end=f'\n{"*" * 40}\n')
# school['porno_class'] = 1  # adding new class
# print(*[f'Class |{a:3}| has |{b:02}| students' for a, b in school.items()], sep='\n', end=f'\n{"*" * 40}\n')
# school.__delitem__('1b')  # school.pop('1b')
# print(*[f'Class |{a:3}| has |{b:02}| students' for a, b in school.items()], sep='\n', end=f'\n{"*" * 40}\n')
# print(f'TOTAL students in school:  {sum(school.values())} students')


# TODO 4. Создайте словарь, где ключами являются числа, а значениями – строки. Примените к нему метод items(),
# полученный объект dict_items передайте в написанную вами функцию, которая создает и возвращает новый словарь,
# "обратный" исходному, т. е. ключами являются строки, а значениями – числа
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


dict_nom_keys = {1: 'apple', 2: 'pineapple', 3: 'noapple', 4: 'sideapple', 5: 'samsung'}


def reinversed_dict(dict_items):
    return {b: a for a, b in dict_items}


# Output
# print(dict_nom_keys)
# print(reinversed_dict(dict_nom_keys.items()))


# TODO 5. Для кaждого из зaпроса выведите название стрaны, в кoтором находится дaнный горoд.
# (на каждую страну укажите 2-3 города).
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


country_town_DICK = {'Ukraine': ('Kiev', 'Kharkov', 'Kalomiya'), 'Russia': ('Zalupentsi', 'Buhostan', 'Krasnaya Vodka'),
                     'Poland': ('Warsaw', 'Krakow', 'Zakopane')
                     }


def GET_country1(dick, town):
    return [a for a, b in dick.items() if town in b]


def GET_country2(dick, town):  # dont even look at this - just know - it works ) Was trying to find alternative way
    # to workit out
    return list(dick.keys())[([list(dick.values()).index(a) for a in dick.values() if town in a][0])]


# Output

# print(GET_country1(country_town_DICK, 'Buhostan'))
# print(GET_country2(country_town_DICK, 'Krasnaya Vodka'))


# TODO 6. Напишите программу калькулятор с использованием словаря(пользователь вводит операцию – ключ словаря)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def calculator_dick(nom, opi, nom2=1):
    op = {'+': nom + nom2, '-': nom - nom2, '*': nom * nom2, '/': nom / nom2, 'q': 'Get the fuck outta here'}
    return op[opi]


# Output
# print(calculator_dick(1,'+',2))


# TODO 7. Дан словарь с однозначным соответствием английских и русских слов в таком формате:
# cat - кошка
# dog - собака
# mouse - мышь
# house - дом
# eats - ест
# in - в
# too - тоже
# Требуется сделать подстрочный перевод с помощью имеющегося словаря и вывести результат. Незнакомые словарю
# слова нужно оставлять в исходном виде.
# Mouse in house. Cat in house.
# Cat eats mouse in dog house.
# Dog eats mouse too.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


dictator = {'cat': 'кошак', 'dog': 'собакэн', 'mouse': 'маус ин да хаус', 'house': 'хата', 'eats': 'жрёт',
            'in': 'внутря',
            'too': 'так же'}
stringi = 'Dog eats mouse too.'
print()


def translator_dick(stringe, dick_db):
    naked_and_split = [i.strip('.,:;\'"') for i in stringe.split()]
    result = []
    for word in naked_and_split:
        if word.lower() in dick_db.keys():
            word = dick_db[word.lower()]
            result.append(word)
        else:
            result.append(word)
    return ' '.join(result)


# Output
# print(translator_dick(stringi, dictator)) # собакэн жрёт маус ин да хаус так же


# TODO 8. Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой
#  книге.Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, разделённые пробелом и
#     вывести получившуюся статистику.
#     Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в этой
#     строке число его повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
# Порядок вывода слов может быть произвольным, каждое уникальное слово﻿ должно выводиться только один раз.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# REGEX r"\b(?=\w)" + re.escape(word) + r"\b(?!\w)" for word, but algorithm will be different and can be just to confirm
# the top list

def word_stat_line(stri):
    table = {}
    for word in stri.split():
        word = word.strip('./()\'",')
        # if not word in table and len(word) >= 3:
        #     table[word] = stri.count(word)
        if not word in table:
            table[word] = table[word] = sum([1 for i in stri.split() if i == word])
    return table


def line_stat_merge(new_dic, base_dic):
    for word in new_dic.keys():
        if word in base_dic.keys():
            base_dic[word] += new_dic[word]
        else:
            base_dic[word] = new_dic[word]
    return base_dic


# Uncomment this with I/O- otherwise reading lines will lag
with open('war_n_peace.html', 'r') as war_n_peace:
    stat = {}
    for line in war_n_peace.readlines():
        line_stat_merge(word_stat_line(line), stat)

# Output
[print(f'Word |"{a:8}"| is used [{stat[a]}] times') for a in sorted(stat, key=stat.get, reverse=False)]
#
# Word |"это     "| is used [2959] times
# Word |"был     "| is used [3039] times
# Word |"строка  "| is used [3438] times
# Word |"Стр     "| is used [3513] times
# Word |"как     "| is used [4511] times
# Word |"его     "| is used [5986] times
# Word |"что     "| is used [7679] times


# Word |"distinctio"| is used [5] times
# Word |"assumenda"| is used [5] times
# Word |"numquam "| is used [5] times
# Word |"sequi   "| is used [5] times
# Word |"modi    "| is used [5] times
# Word |"impedit "| is used [5] times
# Word |"optio   "| is used [5] times
# Word |"ratione "| is used [6] times
# Word |"culpa   "| is used [6] times
# Word |"nobis   "| is used [6] times
# Word |"necessitatibus"| is used [6] times
# Word |"repellat"| is used [7] times
# Word |"repudiandae"| is used [8] times
# Word |"mollitia"| is used [9] times

'''Thanks for reading. Here's a cookie'''
# print('This is a checkmark to mark that you are done reading!', u'\u2713')
# print('I ❤ Python‽')
