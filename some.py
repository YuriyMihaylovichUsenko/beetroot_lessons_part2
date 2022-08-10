from dataclasses import dataclass, InitVar, field, replace


@dataclass
class A:
    c: InitVar[int] = 0
    a: int = 0

    def __post_init__(self, c: int):
        self.b = self.a - c
        self.d: int = self.b + c


a = A(6, 2)
print(a.__dict__)
b = replace(a, c=5)
print(b.__dict__)
