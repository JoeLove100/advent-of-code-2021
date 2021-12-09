import unittest
from solutions.day9 import is_low_point, get_sum_of_risk_values_for_low_points, read_input, \
    get_neighbours, get_sorted_basin_sizes, get_basin_size


class TestDay9A(unittest.TestCase):

    def test_read_input(self):

        with open("test_fixtures/day_9_input.txt") as input_file:
            data = input_file.read()
            data = data.split("\n")

        result = read_input(data)
        expected_result = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertSequenceEqual(expected_result, result)

    def test_is_low_point_top_left(self):

        test_arr = [[1, 2], [3, 4]]
        result = is_low_point(test_arr, 0, 0)
        self.assertTrue(result)

    def test_not_low_point_top_left(self):

        test_arr = [[1, 2], [0, 4]]
        result = is_low_point(test_arr, 0, 0)
        self.assertFalse(result)

    def test_is_low_point_top_right(self):

        test_arr = [[2, 1], [4, 3]]
        result = is_low_point(test_arr, 0, 1)
        self.assertTrue(result)

    def test_not_low_point_top_right(self):

        test_arr = [[1, 2], [3, 4]]
        result = is_low_point(test_arr, 0, 1)
        self.assertFalse(result)

    def test_is_low_point_bottom_left(self):

        test_arr = [[3, 4], [1, 2]]
        result = is_low_point(test_arr, 1, 0)
        self.assertTrue(result)

    def test_not_low_point_bottom_left(self):

        test_arr = [[1, 2], [3, 4]]
        result = is_low_point(test_arr, 1, 0)
        self.assertFalse(result)

    def test_is_low_point_bottom_right(self):

        test_arr = [[4, 3], [2, 1]]
        result = is_low_point(test_arr, 1, 1)
        self.assertTrue(result)

    def test_not_low_point_bottom_right(self):

        test_arr = [[1, 2], [3, 4]]
        result = is_low_point(test_arr, 1, 1)
        self.assertFalse(result)

    def test_is_low_point_middle(self):

        test_arr = [[1, 2, 3], [4, 1, 6], [6, 6, 6]]
        result = is_low_point(test_arr, 1, 1)
        self.assertTrue(result)

    def test_not_low_point_middle(self):
        test_arr = [[1, 2, 3], [4, 10, 6], [6, 6, 6]]
        result = is_low_point(test_arr, 1, 1)
        self.assertFalse(result)

    def test_get_sum_of_risk_values_for_low_points(self):
        test_arr = [[1, 4, 6], [2, 3, 2], [5, 5, 5]]
        result = get_sum_of_risk_values_for_low_points(test_arr)
        self.assertEqual(5, result)


class TestDay9B(unittest.TestCase):

    def test_get_neighbours(self):
        test_arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        test_coord = (1, 1)
        result = get_neighbours(test_arr, test_coord)
        expected_result = [(0, 1), (2, 1), (1, 0), (1, 2)]
        self.assertSequenceEqual(expected_result, result)

    def test_get_basin_size(self):
        test_arr = [[1, 9, 2, 3], [9, 9, 1, 4], [2, 3, 7, 9], [8, 9, 9, 0]]
        test_coord = (2, 2)
        visited = set()
        result = get_basin_size(test_arr, visited, test_coord)
        self.assertEqual(8, result)

    def test_get_sorted_basin_sizes(self):
        test_arr = [[1, 9, 2, 3], [9, 9, 1, 4], [2, 3, 7, 9], [8, 9, 9, 0]]
        result = get_sorted_basin_sizes(test_arr)
        expected_result = [1, 1, 8]
        self.assertSequenceEqual(expected_result, result)