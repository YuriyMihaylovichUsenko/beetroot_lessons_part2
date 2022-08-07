from unittest.mock import patch

import pytest

import HomeWork_21


def test_closed():
    with patch('HomeWork_21.MyOpen.loger'):
        with HomeWork_21.MyOpen('sample.txt', 'r') as my_open:
            pass
        assert my_open.closed == True


if __name__ == '__main__':
    pytest.main()
