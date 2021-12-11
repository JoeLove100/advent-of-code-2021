import unittest
from solutions.day11 import get_neighbours, count_flashes


class TestDay11A(unittest.TestCase):

    def test_get_neighbours_middle(self):
        test_arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = get_neighbours(test_arr, 1, 1)
        expected_result = [(1, 0), (0, 0), (2, 0), (1, 2), (0, 2), (2, 2),
                           (0, 1), (2, 1)]
        self.assertCountEqual(expected_result, result)  # check same elements regardless of order

    def test_get_neighbours_top_left(self):
        test_arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = get_neighbours(test_arr, 0, 0)
        expected_result = [(0, 1), (1, 0), (1, 1)]
        self.assertCountEqual(expected_result, result)

    def test_get_neighbours_top_right(self):
        test_arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = get_neighbours(test_arr, 2, 2)
        expected_result = [(1, 2), (2, 1), (1, 1)]
        self.assertCountEqual(expected_result, result)

    def test_get_flash_count(self):
        test_arr = [[1, 1, 1, 1, 1],
                    [1, 9, 9, 9, 1],
                    [1, 9, 1, 9, 1],
                    [1, 9, 9, 9, 1],
                    [1, 1, 1, 1, 1]]
        result = count_flashes(test_arr, 1)
        self.assertEqual(9, result)
