import json, pytz, datetime

timezone = pytz.timezone('EET')


class User:
    '''User object.
    kwargs/args
    id - user id
    login - user login
    password - user password
    user_group - regs or public.
                    regs - registered users with additional rights
                    public - unregistered user limited to *,/,+,- operators
    methods - __init__
              __str__
              check_info - prints __str__'''

    def __init__(self, login: str, password: str, log=None, id: int = 1):
        if log is None:
            log = []  # default value as empty list (Intellij didnt like mutable value in the header
        self.login = login
        self.password = password
        self.log = log
        self.id = id
        self.user_group = 'regs'

    def __repr__(self):
        return 'idi'

    def __str__(self):  # string representation of User class
        return f'User id - {self.id}. Login {self.login} has {len(Database(self).find_user()["log"])} calculations'

    def check_info(self):  # printing ___str___of self
        print(self)


class Database:

    def __init__(self, user):
        self.user = user

    def read_users(self):  # reading JSON file - dict-list-dict
        with open('users.json', 'r+') as db:
            return json.load(db)

    def write_db(self, write):  # dumping all everything that is in the "write" argument into JSON file
        with open('users.json', 'w+') as db:
            return json.dump(write, db)

    def find_user(self):  # searches for specific user and give access to his section of json for ***reading***
        for user in self.read_users():
            if user['id'] == self.user.id:
                return user

    def is_user(self):  # boolean is user check
        for users in self.read_users():
            if users['id'] == self.user.id:
                return True
        return False

    def add_calc(self, result):  # reads db, withdraws whole log and adds to it
        # (using 'write' mode to avoid doubling data with 'append'
        file = self.read_users()
        for user in file:
            if user['id'] == self.user.id:
                user['log'].append(
                    (f"{timezone.localize(datetime.datetime.now())}", result))
                self.write_db(file)


def show_stat(date, name):  # showing stat of calculations with time for given user
    return "\n\n\n{} stat:\n{}\n#  Date:\t\t\t\t\t\tResult:\n{}".format(name, '=' * 40, '\n'.join(
        [f"{a + 1}. {datetime.datetime.strptime(i, '%Y-%m-%d %H:%M:%S.%f%z').strftime('%c')}:\t\t{b}\t\t"
         for
         a, (i, b) in enumerate(date['log'])]))

    # returning formatted pytz data example Sat Jan 25 10:26:15 2020

