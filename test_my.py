import unittest
from unittest.mock import Mock
import HomeWork_26


class TestMy(unittest.TestCase):
    @staticmethod
    def s_e(a):
        d = {2: 4,
             3: 9,
             4: 16}
        return d.get(a)

    def test_my(self):
        some.foo = Mock(side_effect=self.s_e)
        self.assertEqual(some.my(2, 3, 4), 29)
