import unittest
from solutions.day1 import get_number_of_increases, get_moving_triplet_sum_increases


class TestDay1A(unittest.TestCase):

    def test_empty_list(self):
        test_arr = []
        result = get_number_of_increases(test_arr)
        self.assertEqual(0, result)

    def test_monotonic_increases(self):
        test_arr = [1, 2, 3, 4]
        result = get_number_of_increases(test_arr)
        self.assertEqual(3, result)

    def test_monotonic_decreases(self):
        test_arr = [4, 3, 2, 1]
        result = get_number_of_increases(test_arr)
        self.assertEqual(0, result)

    def test_repeated_number(self):
        test_arr = [1, 1, 1]
        result = get_number_of_increases(test_arr)
        self.assertEqual(0, result)


class TestDay1B(unittest.TestCase):

    def test_less_than_three(self):
        test_arr = [1, 2]
        with self.assertRaises(ValueError):
            get_moving_triplet_sum_increases(test_arr)

    def test_exactly_three(self):
        test_arr = [1, 2, 3]
        result = get_moving_triplet_sum_increases(test_arr)
        self.assertEqual(0, result)

    def test_monotonically_increasing(self):
        test_arr = [1, 2, 3, 4, 5, 6]
        result = get_moving_triplet_sum_increases(test_arr)
        self.assertEqual(3, result)

    def test_monotonically_decreasing(self):
        test_arr = [6, 5, 4, 3, 2, 1]
        result = get_moving_triplet_sum_increases(test_arr)
        self.assertEqual(0, result)

    def test_increases_then_decreases(self):
        test_arr = [1, 2, 3, 2, 2, 1, 1, 2, 3]
        result = get_moving_triplet_sum_increases(test_arr)
        self.assertEqual(2, result)
