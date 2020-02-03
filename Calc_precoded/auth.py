import os
import json
import sys
import re
import hashlib
import hmac

file = os.path.join('users.json')


def quit_filter(input,tb=True):  # filter of the input to always
    if 'quit' in input.casefold():
        sys.exit('Respecting your desire to quit')
    elif (re.search(r'[^a-zA-Z\d\s:]', input)or re.search(r' ',input))and tb:
        raise ZeroDivisionError('what the flying fuck are you trying to do? \nAlpha-numeric characters only, bitch')
    else:
        return input.strip()


def check_pass(pass1, pass2):
    return pass1 == pass2


def register():
    repeat_register = True
    user = None
    attempts=0
    while repeat_register:
        try:
            if attempts==3:
                return None
            attempts+=1
            login = quit_filter(input('login >>> '))
            password = quit_filter(input('paswword >>> '))
            confirm_password = quit_filter(input('repeat password >>>'))
            if check_pass(password, confirm_password):
                try:
                    user = write_to_db(login=login, password=password, log=[])
                    repeat_register = False
                    print('register success!')
                except ValueError as e:  # Unnecessary segment
                    repeat_register = True
                    print(e)
            else:
                print('incorrect password')
        except Exception as e:
            print(e)
    return user


def check_user_in_db(login):
    with open(file, 'r') as users:
        list_users = json.load(users)
        for user in list_users:
            if user['login'] == login:
                raise ValueError('user already exists with login {}'.format(login))


def write_to_db(**new_user):
    with open(file, 'r') as users:
        user_data = json.load(users)
        if len(user_data) == 0:
            new_user.update(
                {'id': 1}
            )
        else:
            check_user_in_db(login=new_user['login'])
            new_id = user_data[-1]['id'] + 1
            new_user.update({
                'id': new_id
            })
    user_data.append(new_user)
    with open(file, 'w+') as f:
        json.dump(user_data, f)
    return new_user


def init_db():
    import os
    try:
        if open(file):
            if json.load(open(file))[0]['login'] == 'admin':
                return
            raise FileNotFoundError
    except:
        with open(file, 'w') as foil:
            json.dump([{"login": "admin", "password": "admin", 'id': 1, "log": []}], foil)


def main():
    init_db()
    user = register()
    print(user)


if __name__ == '__main__':
    main()
