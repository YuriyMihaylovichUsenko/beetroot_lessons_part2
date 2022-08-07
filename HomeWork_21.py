import logging


class MyOpen:
    counter = 0

    def __init__(self, file, mode):
        self.file = file
        self.mode = mode

    @staticmethod
    def loger():
        return logging.basicConfig(
            level=logging.INFO, format='%(name)s - %(message)s')

    def __enter__(self):
        self.loger()
        logging.info('func enter() is evoked')
        self.data = open(self.file, self.mode)
        MyOpen.counter += 1
        return self.data

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.loger()
        logging.info('func exit() is evoked')
        self.data.close()
        return True


def reader(file_obj):
    res = file_obj.readline()
    return res


def main():
    with MyOpen('sample.log', 'r+') as my_open:
        print(my_open.readline())
        print(MyOpen.counter)

    with MyOpen('sample.log', 'r+') as my_open:
        print(my_open.readline())
        print(MyOpen.counter)


if __name__ == '__main__':
    main()
