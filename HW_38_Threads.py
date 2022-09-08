import threading

# Task 1
# Make a class called Counter, and make it a subclass of the Thread class in
# the Threading module. Make the class have two global variables, one called
# counter set to 0, and another called rounds set to 100.000. Now implement
# the run() method, let it include a simple for-loop that iterates through
# rounds (e.i. 100.000 times) and for each time increments the value of the
# counter by 1. Create 2 instances of the thread and start them, then join them
# and check the result of the counter, it should be 200.000, right? Run it a
# couple of times and consider some different reasons why you get the answer
# that you get.


counter = 0
rounds = 100000


class Counter(threading.Thread):

    def run(self):
        global counter
        for _ in range(rounds):
            counter += 1
        return counter


def main():
    count_1 = Counter()
    count_2 = Counter()

    count_1.start()
    count_2.start()

    count_1.join()
    count_2.join()

    print(counter)


if __name__ == '__main__':
    main()