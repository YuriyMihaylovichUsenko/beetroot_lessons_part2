# Task 1
class Stack:
    def __init__(self, sequence):
        self.args = sequence

    def push(self, arg):
        self.args.append(arg)

    def pop(self):
        return self.args.pop(-1)

    def __repr__(self):
        reverse = self.args[::-1]
        return 'stack:' + '\n      '.join(str(i) for i in reverse)

    def is_empty(self):
        if self.args:
            return False
        else:
            return True

    def peek(self):
        if self.is_empty():
            return None
        return self.args[-1]

    def size(self):
        return len(self.args)


def reader_revers(sequence):
    stack = Stack(sequence)
    while stack.size() > 0:
        print(stack.peek())
        stack.pop()


# Task 2
def balanced_parentheses(sequence):
    template = '()[]{}'
    interest_sequence = []
    for i in sequence:
        if i in template:
            interest_sequence.append(i)
    stack = Stack([])
    appropriate = {']': '[', ')': '(', '}': '{'}
    opening = '([{'
    closing = ')]}'
    for i in interest_sequence:
        if i in opening:
            stack.push(i)
        if i in closing:
            if appropriate[i] == stack.peek():
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False


# Task 3
def get_from_stack(elem, stack):
    temp_stack = Stack([])
    desired = None
    while stack.size() > 0:
        current_el = stack.pop()
        if current_el == elem:
            desired = elem
            while temp_stack.size() > 0:
                current_el1 = temp_stack.pop()
                stack.push(current_el1)
            break
        else:
            temp_stack.push(current_el)
    if desired is None:
        while temp_stack.size() > 0:
            stack.push(temp_stack.pop())
        raise ValueError('desired element is absent in stack')
    print(stack)
    return desired


# Task 3
class Queue:
    def __init__(self, sequence):
        self.args = sequence

    def enqueue(self, arg):
        self.args.append(arg)

    def dequeue(self):
        return self.args.pop(0)

    def __repr__(self):
        return f'{self.args[::-1]}'

    def is_empty(self):
        return self.args is None

    def front(self):
        return self.args[0]

    def size(self):
        return len(self.args)

    def get_from_queue(self, elem):
        desired_elem = None
        counter = 0
        while counter < self.size():
            counter += 1
            current_el = self.dequeue()
            if current_el == elem:
                desired_elem = elem
            self.enqueue(current_el)
        if desired_elem is None:
            raise ValueError('desired element is absent in queue')
        print(self)
        return desired_elem


def main():
    # reader_revers(list(range(10)))
    print(balanced_parentheses('(65##@[[*/]+])'))
    # print(get_from_stack(1, Stack([1, 2, 3, 4, 5, 6, 7, 8])))
    # print(Queue([1, 2, 3, 4, 5, 5]).get_from_queue(3))
    # print(Queue([1, 2, 3, 4, 5, 5]).is_empty())


if __name__ == '__main__':
    main()
