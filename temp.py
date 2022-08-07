class CustomError(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        with open('a.txt', 'a') as f:
            f.write(msg + '\n')


raise CustomError('sdfsg')


