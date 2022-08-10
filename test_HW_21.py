import unittest
import HomeWork_21
from unittest.mock import patch


class TestHw21(unittest.TestCase):

    def test_counter(self):
        with patch('HomeWork_21.MyOpen.loger'):
            HomeWork_21.MyOpen.counter = 0
            with HomeWork_21.MyOpen('sample.log', 'r+') as my_open:
                ...
            with HomeWork_21.MyOpen('sample.log', 'r+') as my_open:
                ...
        self.assertEqual(HomeWork_21.MyOpen.counter, 2)

    def test_readable(self):
        with patch('HomeWork_21.MyOpen.loger'):
            with HomeWork_21.MyOpen('sample.txt', 'w') as my_open:
                my_open.write('something')
            with HomeWork_21.MyOpen('sample.txt', 'r') as my_open:
                self.assertEqual(my_open.read(), 'something')

    # I'm not sure if it is right approach, but it works
    def test_error_under_with(self):
        with patch('HomeWork_21.MyOpen.loger'):
            with HomeWork_21.MyOpen('sample.txt', 'r') as my_open:
                my_open.writererfdggdfgfgf('some')

    def test_error_in_with(self):
        with patch('HomeWork_21.MyOpen.loger'):
            with self.assertRaises(FileNotFoundError):
                with HomeWork_21.MyOpen('not_sample.txt', 'r') as my_open:
                    ...


if __name__ == '__main__':
    unittest.main()
