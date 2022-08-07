import pytest
import HomeWork_21


@pytest.fixture
def opener():
    with HomeWork_21.MyOpen('sample.txt', 'r+') as f:
        res = HomeWork_21.reader(f)
    return res


def test_reader(opener):
    assert opener == 'something'


if __name__ == '__main__':
    pytest.main()
