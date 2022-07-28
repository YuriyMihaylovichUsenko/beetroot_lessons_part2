import re
from functools import wraps
# Task 1


class Email:
    @staticmethod
    def validater(email):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if re.match(pattern, email):
            return True

    def __init__(self, email):
        if self.validater(email):
            self.email = email
        else:
            raise ValueError('Email is not valid')


# Task 2
class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    @property
    def get_workers(self):
        return self.workers

    @get_workers.setter
    def add_workers(self, val):
        if isinstance(val, Worker):
            self.workers.append(val)
        else:
            raise ValueError('must be Worker')

    def __str__(self):
        return f"{self.__class__.__name__} name: {self.name}"

    def __repr__(self):
        return f"{self.__class__.__name__} name: {self.name}"


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss
        self.add_worker_to_boss()

    @property
    def get_boss(self):
        print('get')
        return self.boss

    @get_boss.setter
    def get_boss(self, value):
        print('set')
        if isinstance(value, Boss):
            self.boss = value
        else:
            raise ValueError('must be Boss')

    def add_worker_to_boss(self):
        self.boss.add_workers = self

    def __str__(self):
        return f"{self.__class__.__name__} name: {self.name}"

    def __repr__(self):
        return f"{self.__class__.__name__} name: {self.name}"


# Task 3
class TypeDecorators:
    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return int(func(*args, **kwargs))
            except ValueError:
                return 'result of function not convertible'
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return str(func(*args, **kwargs))
            except ValueError:
                return 'result of function not convertible'
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return bool(func(*args, **kwargs))
            except ValueError:
                return 'result of function not convertible'
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return float(func(*args, **kwargs))
            except ValueError:
                return 'result of function not convertible'
        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


def main():
    # Task 1
    # ins = Email("me@host.com")
    # print(ins.email)

    # Task 2
    # b1 = Boss(1, "Vasya", "STO")
    # b2 = Boss(2, "Petya", "Roshen")
    # w1 = Worker(1, "Vova", "Google", b1)
    # w1.get_boss = b2
    # w1.add_worker_to_boss()
    # print(b1.workers)
    # print(w1.get_boss)
    # b1.add_workers = 'some'
    # print(b2.workers)
    # print(b1.workers)

    # Task 3
    # assert do_nothing('25') == 25
    # assert do_something('True') is True
    # print(do_nothing('2g5'))
    # print(do_something(''))


if __name__ == '__main__':
    main()

