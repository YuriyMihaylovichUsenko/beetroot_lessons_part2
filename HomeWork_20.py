import unittest as unt
import HomeWork_19 as hw
import phone_book_without_ZIPER as book
from unittest.mock import patch, call


class TestEnumerate(unt.TestCase):

    def test_enum(self):
        res = next(hw.with_index('asd'))
        self.assertNotEqual(res[0], 2)
        self.assertEqual(res, (1, 'a'))

    def test_all_value_in_range(self):
        range_ = hw.in_range(0, 5)
        for my_val, right_val in zip(range_, [0, 1, 2, 3, 4]):
            self.assertEqual(my_val, right_val)

    def test_enum_type(self):
        self.assertRaises(TypeError, hw.with_index(1))


class TestPhonBook(unt.TestCase):

    def setUp(self) -> None:
        self.data = [{'first_name': 'Yuriy', 'last_name': 'Usenko',
                    'town': 'Kremenchuk', 'number': '0980111121'},
                    {'first_name': 'Vasiliy', 'last_name': 'Bondarenko',
                    'town': 'Kuiv', 'number': '0980020202'}]

    @patch('builtins.input', lambda _: 'Yuriy')
    def test_search_by_first_name(self):
        name = 'Yuriy'
        call_ = book.search_by_first_name(self.data)
        expect = [i for i in self.data if i['first_name'] == name]
        self.assertEqual(call_, expect)

    @patch.object(book, 'function_choice')
    @patch('phone_book_without_ZIPER.start_and_open')
    def test_phone_book_overall(self, mock_start, mock_function):
        mock_start.return_value = self.data

        book.phone_book('phone_book_.json')

        mock_start.assert_has_calls([call('phone_book_.json')])
        mock_function.assert_has_calls([call(self.data)])
        mock_start.assert_called_once()
        self.assertEqual(mock_function.call_count, 1)


def main():
    unt.main()


if __name__ == '__main__':
    main()
