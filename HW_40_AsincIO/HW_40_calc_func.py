import asyncio
import multiprocessing
from functools import reduce
from time import time, sleep
from pprint import pprint

# Task 1
# Async


def fibonacci(number):
    if number == 0:
        return 0
    if number == 1:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)


async def num_prop(number):
    await asyncio.sleep(1)
    print({'number': number,
            'square': number * number,
            'cube': number ** 3,
            'factorial': reduce(lambda x, y: x * y, range(1, number + 1)),
            'fibonacci': fibonacci(number)})


async def main(numbers):

    tasks = []
    for i in numbers:
        task = asyncio.create_task(num_prop(i))
        tasks.append(task)

    await asyncio.gather(*tasks)
    return

###############################################################################
# Multiprocessing


def num_prop_(number):
    sleep(1)
    return {'number': number,
            'square': number * number,
            'cube': number ** 3,
            'factorial': reduce(lambda x, y: x * y, range(1, number + 1)),
            'fibonacci': fibonacci(number)}

if __name__ == '__main__':
    # Asinc

    input_list = input('input any numbers separated ", "').split(', ')
    numbers = [int(i) for i in input_list]

    t1 = time()

    asyncio.run(main(numbers))

    print(f'Time spent to transform {time() - t1:.2f}')

    ############################################################################
    # Multiprocessing

    input_list = input('input any numbers separated ", "').split(', ')
    numbers = [int(i) for i in input_list]

    t1 = time()

    pool = multiprocessing.Pool()

    result = pool.map(num_prop_, numbers)
    pprint(result)

    print(f'Time spent to transform {time() - t1:.2f}')
