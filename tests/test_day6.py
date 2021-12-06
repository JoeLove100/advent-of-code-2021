import unittest
from solutions.day6 import get_total_number_of_fish


class TestDay6A(unittest.TestCase):

    def test_day_zero(self):
        result = get_total_number_of_fish([1], 0)
        self.assertEqual(1, result)

    def test_fish_split(self):
        result = get_total_number_of_fish([1], 2)
        self.assertEqual(2, result)

    def test_multiple_fish(self):
        result = get_total_number_of_fish([4, 1], 2)
        self.assertEqual(3, result)