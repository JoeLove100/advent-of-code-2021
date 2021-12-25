import unittest
from solutions.day25 import get_days_til_stationary


class TestDay25A(unittest.TestCase):

    def test_already_cannot_move(self):
        test_arr = [[">", ">"], ["v", "."]]
        result = get_days_til_stationary(test_arr)
        self.assertEqual(1, result)

    def test_full_example(self):

        with open("test_fixtures/day_25_input.txt") as input_file:
            data = input_file.readlines()
            data = [list(line.replace("\n", "")) for line in data]

        result = get_days_til_stationary(data)
        self.assertEqual(58, result)