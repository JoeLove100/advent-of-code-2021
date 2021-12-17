import unittest
from solutions.day17 import get_valid_pair_count


class TestDay17B(unittest.TestCase):

    def test_get_valid_pair_count(self):
        x_0, x_1, y_0, y_1 = 20, 30, -5, -10
        result = get_valid_pair_count(x_0, x_1, y_0, y_1)
        self.assertEqual(112, result)
