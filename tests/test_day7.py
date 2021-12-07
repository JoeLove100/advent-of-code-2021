import unittest
from solutions.day7 import get_min_distance, get_min_distance_2


class TestDay7A(unittest.TestCase):

    def test_get_min_distance_same_number(self):
        test_arr = [1, 1, 1, 1]
        result = get_min_distance(test_arr)
        self.assertEqual(0, result)

    def test_get_min_distance_unsorted(self):
        test_arr = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
        result = get_min_distance(test_arr)
        self.assertEqual(37, result)


class TestDay7B(unittest.TestCase):

    def test_get_min_distance_2(self):
        test_arr = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
        result = get_min_distance_2(test_arr)
        self.assertEqual(168, result)
