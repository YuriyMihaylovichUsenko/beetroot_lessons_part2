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


# Task 3
class Product:
    def __init__(self, type_, name, price):
        self.name = name
        self.type = type_
        self.price = price
        self.amount = None


p1 = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
p3 = Product('Food', 'Bread', 1)


class Store:
    def __init__(self, *args: Product):
        self.income = 0
        self.all_products = []
        for product in args:
            self.product = product
            self.product.amount = 1
            self.all_products.append(product)

    def add_product(self, product, amount, price_premium=0.3):
        if product in self.all_products:
            product.amount += amount
        else:
            self.all_products.append(product)
            product.price *= (1 + price_premium)
            product.amount = amount

    def set_discount(self, identifier, percent, identifier_type='name'):
        if identifier_type == 'name':
            for prod in self.all_products:
                if prod.name == identifier:
                    prod.price *= (1 - percent/100)
        elif identifier_type == 'type':
            for prod in self.all_products:
                if prod.type == identifier:
                    prod.price *= (1 - percent/100)

    def sell_product(self, product_name, amount):
        for prod in self.all_products:
            if prod.name == product_name and prod.amount >= amount:
                prod.amount -= amount
                self.income += prod.price * amount

    def get_income(self):
        return self.income

    def get_all_products(self):
        for prod in self.all_products:
            print(prod.name, prod.type, prod.price, prod.amount)

    @staticmethod
    def get_product_info(product):
        return product.name, product.amount


def main():
    # Task 1
    # print(dir(stud1)[-6:])
    # print(teach1.salary)
    # print(dir(teach1)[-6:])
    #
    # # Task 2
    # print(m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16],
    #       m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90],
    #       m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020])

    # Task 3
    my_store = Store(p1, p2)

    my_store.add_product(p3, 100)
    my_store.get_all_products()
    my_store.add_product(p3, 100)
    print(p3.amount)
    print(p3.price)
    my_store.set_discount('Food', 20, 'type')
    print(p3.price)
    my_store.sell_product('Football T-Shirt', 1)
    my_store.sell_product('Bread', 20)
    print(my_store.get_income())
    print(my_store.get_product_info(p1))


if __name__ == '__main__':
    main()
