from time import perf_counter
import matplotlib.pyplot as plt
from typing import List, Tuple


def question1(first_list: List[int], second_list: List[int]) -> List[int]:
    res: List[int] = []
    for el_first_list in first_list:
        if el_first_list in second_list:
            res.append(el_first_list)
    return res


def question2(n: int) -> int:
    for _ in range(10):
        n **= 3
    return n


def question3(first_list: List[int], second_list: List[int]) -> List[int]:
    temp: List[int] = first_list[:]
    for el_second_list in second_list:
        flag = False
        for check in temp:
            if el_second_list == check:
                flag = True
                break
        if not flag:
            temp += second_list
    return temp


def question4(input_list: List[int]) -> int:
    res: int = 0
    for el in input_list:
        if el > res:
            res = el
    return res


def question5(n: int) -> List[Tuple[int, int]]:
    res: List[Tuple[int, int]] = []
    for i in range(n):
        for j in range(n):
            res.append((i, j))
    return res


def question6(n: int) -> int:
    while n > 1:
        n /= 2
    return n


def plot_graph(number):
    x = []
    y = []
    for i in range(1, 1000):
        first = [i for i in range(i)]
        second = [i for i in range(i)]
        x.append(i)

        dict_func = {
            1: question1,
            2: question2,
            3: question3,
            4: question4,
            5: question5,
            6: question6
        }
        dict_arg = {
            1: (first, second),
            2: (i, ),
            3: (first, second),
            4: (first, ),
            5: (i, ),
            6: (i, )
        }
        t1 = perf_counter()
        dict_func.get(number)(*dict_arg.get(number))
        t2 = perf_counter()
        y.append(t2 - t1)

    fig, ax = plt.subplots()
    ax.plot(x, y, color='blue')
    fig.savefig(f'time_complexity{number}.png')
    plt.show()


# for i in range(1, 7):
plot_graph(2)
