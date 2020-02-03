'''Main file.
    -has 2 major sequences login_menu_choice and operational menu'''


from operation import *
from database import User, Database, show_stat
from auth import quit_filter, check_pass, register, check_user_in_db, write_to_db, init_db

anon = User(login='Ananymous', password='titi')
anon.user_group = 'public'


def login_input():  # shortcut to get input
    print('=' * 40, '\n')
    login = quit_filter(input('Login: '))
    password = quit_filter(input("Password: "))
    print('=' * 40)
    return login, password


def choice():  # menu choice for secondary menu
    while True:
        try:
            choice = int(quit_filter(input('>>>> ')))
            return choice
        except Exception as e:
            print(f'{e},please input correct menu choice or "quit"')


def login_menu_choice():  # sequence for starting menu
    login_count = 3
    active_user = None
    print(
        'Calculator.Simple.\n1. Register\n2. Log in(existing user)\n3.Fast calculations\t\t\t\t\t'
        'At any time type "quit" to quit')
    while True:
        try:
            menu = float(quit_filter(input('>>> ')))
            break
        except Exception as e:
            print(f'{e} Please re-enter')

    while True:
        if active_user:
            print(f'Logged in as {active_user.login}')
            break
        if login_count <= 3 and active_user == None:
            print(f'{login_count} attempts to log in left...\n\n\n{"*" * 40}')
        if login_count <= 0:
            menu = 3

        if menu == 1:
            while True:
                try:
                    print('Create new user')
                    init_db()
                    user = register()
                    if user:
                        active_user = User(login=user['login'], password=user['password'], id=user['id'],
                                           log=user['log'])
                    else:
                        active_user = anon
                    break
                except Exception as e:
                    print(f'{e}, dude come on, its not that hard! ◕_◕')

        elif menu == 2:
            while True:
                try:
                    login, password = login_input()
                    break
                except Exception as e:
                    print(e)

            for user in Database.read_users('pipi'):
                if user['login'] == login and user['password'] == password:
                    print(f'logging in as {user["login"]}')
                    active_user = User(user['login'], user['password'], user['log'], user['id'])
                    break
            else:
                login_count -= 1
        elif (menu != 1 and menu != 2):
            print('Welcome my dear Anonymous')
            active_user = anon
            print(active_user)
    return active_user


def operational_menu(active_user):  # program sequence after active_user has been assigned
    while True:
        print('\n\nMenu:\n1.User Stat\n2.Calculations log\n3.Calculate\n\t\t\t\t\t\tType quit any time to quit')
        oper = choice()
        if oper == 1:
            if active_user.user_group == 'regs':
                print(active_user)
            else:
                print('Anons have no stats, you pleb')
        elif oper == 2:
            if active_user.user_group == 'regs':
                file = Database.read_users('yo')
                for users in file:
                    if users['id'] == active_user.id:
                        print(show_stat(users, active_user.login))
            else:
                print('Anons have no log, you rediska')
        elif oper == 3:
            operators = {'*': 'mul', '+': 'add', '-': 'sub', '/': 'div', 'sin': 'sin', 'cos': 'cos', 'tan': 'tan',
                         'cotan': 'cotan'}
            if active_user.user_group == 'public':
                print(' | '.join([i for i in operators.keys() if len(i) < 2]))
            else:
                print(' | '.join(operators.keys()))
            while True:
                while True:
                    try:
                        nom1 = float(quit_filter(input('Nom1>>>')))
                        break
                    except Exception as e:
                        print(f'{e} I need nomber dude')
                pip = True
                while pip:
                    print('Please enter correct operator')
                    op = quit_filter(input('operator'), tb=False)
                    for ops in operators.keys():
                        if str(op) == str(ops):
                            pip = False
                while True:
                    while True:
                        try:
                            if op in 'sincosancotan':
                                nom2 = 1
                                break
                            else:
                                nom2 = float(quit_filter(input('Nom2>>>')))
                                break
                        except Exception as e:
                            print(f'{e}, please enter smthing, dude')
                    print('*' * 40)
                    try:
                        print(active_user.user_group)
                        if active_user.user_group == 'regs':
                            resolt = registered[operators[op]](nom1, nom2)
                            Database(active_user).add_calc(resolt)
                            break
                        else:
                            if op in 'sincostancotan':
                                print('dont have access')
                                resolt = 'No access'
                                break
                            else:
                                resolt = public[operators[op]](nom1, nom2)
                                break

                    except Exception as e:
                        print(e, "you either don't have access or u don't know math. \nTry again, dude\n\n\n\n")
                print('\n\n', '=' * 40, '\n', resolt, '\n', '=' * 40)
                break


if __name__ == '__main__':
    operational_menu(login_menu_choice())
