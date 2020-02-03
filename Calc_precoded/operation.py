import math


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def sin(a,b):
    return math.sin(a)


def cos(a,b):
    return math.cos(a)


def tan(a,b):
    return math.tan(a)


def cotan(a,b):
    return 1 / math.tan(a)


registered = {'add': add, 'sub': sub, 'mul': mul, 'div': div, 'sin': sin, 'cos': cos, 'tan': tan, 'cotan': cotan}
public = {'add': add, 'sub': sub, 'mul': mul, 'div': div}

if __name__ == '__main__':
    print('Hello WOrld!')
    print(__file__)

    assert add(2, 2) == 4
    assert add(2, 2) == 5

    assert add(2, 2) == 56
