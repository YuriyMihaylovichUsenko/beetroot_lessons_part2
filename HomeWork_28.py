class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self, data):
        self._data = data

    def set_next(self, new_next):
        self._next = new_next

    def __repr__(self):
        return f'{self._data}'

    def __str__(self):
        return self.__repr__()


class UnorderedList:

    def __init__(self):
        self._head = Node(None)

    def is_empty(self):
        return self._head is None

    def add(self, item):
        if self._head.get_data():
            temp = Node(item)
            temp.set_next(self._head)
            self._head = temp
        else:
            self._head = Node(item)

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current: Node = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def __repr__(self):
        representation = "<UnorderedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + "> None"

    def append(self, item):
        if self._head.get_data():
            current = self._head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(Node(item))
        else:
            self._head = Node(item)

    def index(self, index):
        current = self._head
        count = 0
        while count < index:
            count += 1
            current = current.get_next()
        return current

    def pop(self, index):
        current = self._head
        previous = None
        count = 0
        while count < index:
            count += 1
            previous = current
            current = current.get_next()
        previous.set_next(current.get_next())

    def insert(self, index, obj):
        current = self._head
        previous = None
        count = 0
        while count < index:
            count += 1
            previous = current
            current = current.get_next()
        new = Node(obj)
        previous.set_next(new)
        new.set_next(current)

    def slice(self, start, stop):
        current = self._head
        count = 0
        while count < start:
            count += 1
            current = current.get_next()
        slise = UnorderedList()
        slise.add(current)
        while count < stop - 1:
            count += 1
            current = current.get_next()
            slise.append(current)
        return slise

    def __str__(self):
        return self.__repr__()


# Task 2
class Stack:
    def __init__(self):
        self._head = Node(None)

    def is_empty(self):
        return self._head is None

    def push(self, item):
        if self._head.get_data():
            temp = Node(item)
            temp.set_next(self._head)
            self._head = temp
        else:
            self._head = Node(item)

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def pop(self):
        self._head = self._head.get_next()

    def peek(self):
        return self._head

    def __repr__(self):
        representation = "<Stack: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + "]"


# Task 3
class Queue:
    def __init__(self):
        self._head = Node(None)

    def is_empty(self):
        return self._head is None

    def enqueue(self, item):
        if self._head.get_data():
            temp = Node(item)
            temp.set_next(self._head)
            self._head = temp
        else:
            self._head = Node(item)

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def dequeue(self):
        current = self._head
        previous = 0
        while current.get_next():
            previous = current
            current = current.get_next()
        previous.set_next(None)

    def front(self):
        current = self._head
        while current.get_next():
            current = current.get_next()
        return current

    def __repr__(self):
        representation = "[Queue: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"


if __name__ == "__main__":
    my_list = UnorderedList()

    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)

    print(my_list)
    my_list.pop(2)
    print(my_list)
    my_list.insert(3, 10)
    print(my_list)
    slice_ = my_list.slice(1, 3)
    print(slice_)
    print(my_list)
    my_list.append(100)
    print(my_list)
    print(my_list.search(100))
    print(my_list.size())
    my_list.remove(31)
    print(my_list)
############################################
    stack = Stack()
    stack.push(15)
    stack.push(18)
    stack.push(25)
    print(stack)
    stack.pop()
    print(stack)
    print(stack.peek())
#############################################
    queue = Queue()
    queue.enqueue(2)
    queue.enqueue(6)
    queue.enqueue(9)
    print(queue)
    queue.dequeue()
    print(queue)
    print(queue.front())



