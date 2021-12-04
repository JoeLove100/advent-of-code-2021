import unittest
from solutions.day3 import get_gamma_and_epsilon, get_life_support_rating


class TestDay3A(unittest.TestCase):

    def test_get_gamma_and_epsilon(self):
        numbers = ["1001", "1010", "1100"]
        g, e = get_gamma_and_epsilon(numbers)
        self.assertEqual(int("0b1000", 2), g)
        self.assertEqual(int("0b0111", 2), e)


class TestDay3B(unittest.TestCase):

    def test_get_life_support_rating_most_common(self):
        test_numbers = ["111", "101", "010", "001"]
        rating = get_life_support_rating(test_numbers, True)
        self.assertEqual(7, rating)

    def test_get_life_support_rating_least_common(self):
        test_numbers = ["0110", "1010", "0101", "0001", "1100"]
        rating = get_life_support_rating(test_numbers, False)
        self.assertEqual(10, rating)
