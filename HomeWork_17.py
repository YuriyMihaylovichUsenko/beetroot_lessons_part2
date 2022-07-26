import json
from pprint import pprint

from requests import Session
from bs4 import BeautifulSoup


def get_response(url):
    with Session() as session:

        response = session.get(url, timeout=10)

        assert response.status_code == 200, 'Bad response'

    return response


def html_parser(response):
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.select('#bookTitle')
    author = soup.select('#bookAuthors span div a span')
    rating = soup.select('span[itemprop="ratingValue"]')
    text = soup.select('#description span')
    img_url = soup.select('#coverImage')
    reviews = [review.text.strip() for review
               in soup.select('.reviewText span span')]

    return {
        'title': title[0].text.strip(),
        'author': author[0].text.strip(),
        'rating': float(rating[0].text.strip()),
        'text': text[1].text,
        'img_url': img_url[0]['src'],
        'reviews': reviews
    }


def json_file_writer(data, indent=4):
    with open('book.json', 'w') as file:
        json.dump(data, file, indent=indent)


class MyScraper:
    def __init__(self):
        ...

    @staticmethod
    def scrape(url):
        response = get_response(url)
        data = html_parser(response)
        json_file_writer(data, indent=8)


# Task 1
class Animal:
    @staticmethod
    def talk():
        ...


class Dog(Animal):
    @staticmethod
    def talk():
        print("Gav-gav")


class Cat(Animal):
    @staticmethod
    def talk():
        print("Myau-myau")


# Task 2
class Author:
    def __init__(self, name, country, birthday, books):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books

    def __str__(self):
        return f'{self.name} from {self.country} born {self.birthday}'

    def __repr__(self):
        return f'{self.name} from {self.country} born {self.birthday}'


class Book:
    instances_amount = 0

    def __init__(self, name, year, author: Author):
        self.name = name
        self.year = year
        self.author = author
        Book.instances_amount += 1
        author.books.append(self)

    def __str__(self):
        return f'{self.name} by {self.author} writen {self.year}'

    def __repr__(self):
        return f'{self.name} by {self.author} writen {self.year}'


class Library:
    def __init__(self, name, books: list, authors: list):
        self.name = name
        self.books = books
        self.authors = authors

    def new_book(self, name: str, year: int, author: Author):
        book = Book(name, year, author)
        self.books.append(book)
        return book

    def group_by_author(self, author: Author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year: int):
        return [book for book in self.books if book.year == year]

    def __str__(self):
        return f'{self.name} library'

    def __repr__(self):
        return f'{self.name} library'


# Task 3
class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return f'str Fraction({self.num}, {self.den})'

    def __add__(self, other):
        total_den = self.den * other.den
        new_num = other.den * self.num + other.num * self.den
        new_den = total_den
        temp_list = [1]
        for i in range(2, min(new_num, new_den) + 1):
            if new_num % i == 0 and new_den % i == 0:
                temp_list.append(i)
        nok = max(temp_list)
        return Fraction(new_num//nok, new_den//nok)

    def __sub__(self, other):
        total_den = self.den * other.den
        new_num = other.den * self.num - other.num * self.den
        new_den = total_den
        temp_list = [1]
        for i in range(2, min(new_num, new_den) + 1):
            if new_num % i == 0 and new_den % i == 0:
                temp_list.append(i)
        nok = max(temp_list)
        return Fraction(new_num // nok, new_den // nok)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        temp_list = [1]
        for i in range(2, min(new_num, new_den) + 1):
            if new_num % i == 0 and new_den % i == 0:
                temp_list.append(i)
        nok = max(temp_list)
        return Fraction(new_num // nok, new_den // nok)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        temp_list = [1]
        for i in range(2, min(new_num, new_den) + 1):
            if new_num % i == 0 and new_den % i == 0:
                temp_list.append(i)
        nok = max(temp_list)
        return Fraction(new_num // nok, new_den // nok)

    # Чому не працює з __div__

    def __eq__(self, other):
        if other.den * self.num == other.num * self.den:
            return True
        else:
            return False

    def __ne__(self, other):
        if other.den * self.num != other.num * self.den:
            return True
        else:
            return False

    def __lt__(self, other):
        if other.den * self.num < other.num * self.den:
            return True
        else:
            return False

    def __gt__(self, other):
        if other.den * self.num > other.num * self.den:
            return True
        else:
            return False


def main():
    # url = 'https://www.goodreads.com/book/show/1.' \
    #       'Harry_Potter_and_the_Half_Blood_Prince'
    #
    # scraper = MyScraper()
    # scraper.scrape(url)

    # Task 1
    # Dog.talk()

    # Task 2
    # shevchenko = Author('Shevchenko T.G.', 'Ukraine', 1816, [])
    # kotlyarevskiy = Author('Kotlyarevskiy', 'Ukraine', 1769, [])
    # zapovit = Book('Zapovit', 1840, shevchenko)
    # print(zapovit.__repr__())
    # lib_1 = Library('First', [], [])
    # lib_1.new_book('Kobzar', 1830, shevchenko)
    # lib_1.new_book('Eneida', 1842, kotlyarevskiy)
    # print(lib_1.books)
    # print(lib_1.group_by_author(shevchenko))
    # print(lib_1.group_by_year(1830))
    # print(shevchenko.books)
    # print(Book.instances_amount)

    # Task 3
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    print(x - y)
    print(Fraction(3, 4) < y)


if __name__ == '__main__':
    main()