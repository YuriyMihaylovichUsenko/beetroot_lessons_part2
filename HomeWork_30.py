class Add:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self, data):
        return self.left.eval(data) + self.right.eval(data)

    def __str__(self):
        return '(' + str(self.left) + '+' + str(self.right) + ')'


class Subtraction:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self, data):
        return self.left.eval(data) - self.right.eval(data)

    def __str__(self):
        return '(' + str(self.left) + '-' + str(self.right) + ')'


class Divide:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self, data):
        return self.left.eval(data) / self.right.eval(data)

    def __str__(self):
        return '(' + str(self.left) + '/' + str(self.right) + ')'


class Exponent:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self, data):
        return self.left.eval(data) ** self.right.eval(data)

    def __str__(self):
        return '(' + str(self.left) + '^' + str(self.right) + ')'


class Constant:
    def __init__(self, value):
        self.value = value

    def eval(self, data):
        return self.value

    def __str__(self):
        return str(self.value)


class Variable:
    def __init__(self, var):
        self.var = var

    def eval(self, data):
        return data[self.var]

    def __str__(self):
        return str(self.var)


data = {'x': 2, 'y': 1}
expression = Add(Divide(Add(Variable('x'), Variable('y')), Constant(3)),
                 Subtraction(Constant(1), Exponent(Variable('x'), Constant(2))))

print(expression.eval(data))
print(expression)