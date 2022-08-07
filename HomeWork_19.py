# Task 1
def with_index(it, start=1):
    ind = 0
    while start <= len(it):
        yield start, it[ind]
        start += 1
        ind += 1


# Task 2
def in_range(start=0, stop=0, step=1):
    val = start
    while val < stop:
        yield val
        val += step


# Task 3
class MyIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.iterable)-1:
            self.index += 1
            return self.iterable[self.index]
        raise StopIteration


class MyIterable:
    def __init__(self, list_):
        self.list = list_

    def __iter__(self):
        return MyIterator(self.list)

    def __getitem__(self, key):
        return self.list[key]


def main():
    # Task 1
    print(next(with_index('asd')))
    ###########################################
    # Task 2
    # print(list(in_range(0, 10)))
    ###########################################
    # Task 3
    iterable = MyIterable([12, 23, 34])
    print(iterable[2])
    for i in iterable:
        print(i)


if __name__ == '__main__':
    main()
