# Task 1
class Person:
    def __init__(self, first_name,
                 last_name,
                 age,
                 school_num):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.school_num = school_num


class Student(Person):
    def __init__(self, first_name,
                 last_name,
                 age,
                 school_num,
                 class_num,
                 average_mark):
        super().__init__(first_name,
                         last_name,
                         age,
                         school_num, )
        self.class_num = class_num
        self.average_mark = average_mark


class Teacher(Person):
    def __init__(self, first_name,
                 last_name,
                 age,
                 school_num,
                 salary,
                 subject):
        super(Teacher, self).__init__(first_name,
                                      last_name,
                                      age,
                                      school_num)
        self.salary = salary
        self.subject = subject


stud1 = Student("Martin", "Chepurenko", 48, 11, '1A', 0.5)
teach1 = Teacher("Vasilisa", "Vovk", 25, 11, 3000, "Math")


# Task 2
class Mathematician:
    @staticmethod
    def square_nums(list_):
        return [i ** 2 for i in list_]

    @staticmethod
    def remove_positives(list_):
        return [i for i in list_ if i <= 0]

    @staticmethod
    def filter_leaps(list_):
        return [i for i in list_ if i % 4 == 0]


m = Mathematician()


def main():
    # Task 1
    print(dir(stud1)[-6:])
    print(teach1.salary)
    print(dir(teach1)[-6:])

    # Task 2
    print(m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16],
          m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90],
          m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020])


if __name__ == '__main__':
    main()
