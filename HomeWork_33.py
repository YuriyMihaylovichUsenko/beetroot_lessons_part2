# Task 1
import random
from time import perf_counter
from functools import wraps

def bubble_sort_both_dir(list_):
    for i in range(len(list_)):
        for i_ in range(i, len(list_) - 1 - i):
            j = i_ + 1
            if list_[i_] > list_[j]:
                list_[i_], list_[j] = list_[j], list_[i_]
        for i_ in range(len(list_) - 3 - i, i - 1, -1):
            j = i_ + 1
            if list_[i_] > list_[j]:
                list_[i_], list_[j] = list_[j], list_[i_]
    return list_


# Task 2
def merge(l1, l2):
    i = 0
    j = 0
    res = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            res.append(l1[i])
            i += 1
        else:
            res.append(l2[j])
            j += 1
    res += [l1[item] for item in range(i, len(l1))] + \
           [l2[item] for item in range(j, len(l1))]
    return res


def merge_sort(list_):
    if len(list_) < 2:
        return list_
    middle = len(list_) // 2
    left = [list_[i] for i in range(middle)]
    right = [list_[i] for i in range(middle, len(list_))]
    return merge(merge_sort(left), merge_sort(right))


# Task 3
def insertion_sort(list_):
    for i in range(1, len(list_)):
        temp = list_[i]
        while list_[i - 1] > temp:
            list_[i] = list_[i - 1]
            i -= 1
            if i == 0:
                break
        list_[i] = temp
    return list_


def hybrid_quick_sort(list_, l=9):
    if len(list_) < 2:
        return list_
    pivot = list_[random.randint(0, len(list_))]
    smaller = [i for i in list_ if i < pivot]
    bigger = [i for i in list_ if i > pivot]
    equal = [i for i in list_ if i == pivot]
    if len(bigger) < l:
        sort_bigger = insertion_sort(bigger)
    else:
        sort_bigger = hybrid_quick_sort(bigger)
    if len(smaller) < l:
        sort_smaller = insertion_sort(smaller)
    else:
        sort_smaller = hybrid_quick_sort(smaller)
    return sort_smaller + equal + sort_bigger


# Additional Task
def bubble_sort_reverse(list_):
    j = 0
    for i in range(len(list_) - 1, j, -1):
        while list_[i] > list_[i - 1]:
            list_[i], list_[i - 1] = list_[i - 1], list_[i]
            i -= 1
            if i == 0:
                break
        j += 1
    return list_


def selection_sort_reverse(list_):
    j = 0
    while j < len(list_):
        for i in range(j, len(list_)):
            if list_[j] < list_[i]:
                list_[j], list_[i] = list_[i], list_[j]
        j += 1
    return list_


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t1 = perf_counter()
        res = func(*args, **kwargs)
        print(perf_counter() - t1)
        return res
    return wrapper


@timer
def insert_sort_reverse(list_):
    for i in range(len(list_) - 1):
        temp = list_[i + 1]
        while list_[i] < temp:
            list_[i], list_[i + 1] = list_[i + 1], list_[i]
            i -= 1
            if i == -1:
                break
        list_[i + 1] = temp
    return list_


def merge_reverse(l1, l2):
    i = 0
    j = 0
    res = []
    while i < len(l1) and j < len(l2):
        if l1[i] > l2[j]:
            res.append(l1[i])
            i += 1
        else:
            res.append(l2[j])
            j += 1
    res += l1[i:] + l2[j:]
    return res


def merge_sort_reverse(list_):
    if len(list_) < 2:
        return list_
    middle = len(list_) // 2
    left = list_[:middle]
    right = list_[middle:]
    return merge_reverse(merge_sort_reverse(left), merge_sort_reverse(right))


def quick_sort_reverse(list_):
    if len(list_) < 2:
        return list_
    pivot = list_[random.randint(0, len(list_) - 1)]
    less = [i for i in list_ if i < pivot]
    more = [i for i in list_ if i > pivot]
    equal = [i for i in list_ if i == pivot]
    return quick_sort_reverse(more) + equal + quick_sort_reverse(less)


def main():
    l = [5, 4, 6, 3, 7, 2, 3, 1]
    # print(merge_sort(l))
    # print(hybrid_quick_sort(l, 3))
    # print(insertion_sort(l))
    # print(bubble_sort_reverse(l))
    # print(selection_sort_reverse(l))
    print(insert_sort_reverse(l))
    # print(merge_sort_reverse(l))
    # print(quick_sort_reverse(l))


if __name__ == '__main__':
    main()
