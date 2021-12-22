import unittest
from solutions.day22 import read_input, Cube, get_on_cubes


class TestDay22A(unittest.TestCase):

    def test_read_input(self):
        with open("test_fixtures/day_22_input.txt") as input_file:
            test_data = input_file.readlines()

        result = read_input(test_data)
        expected_result = [Cube(True, (-1, 2), (2, 4), (0, 6)),
                           Cube(False, (10, 10), (-5, -5), (0, 4))]
        self.assertSequenceEqual(expected_result, result)

    def test_get_on_cubes_multiple_on(self):
        test_cubes = [Cube(True, (1, 1), (-2, -2), (3, 3)),
                      Cube(True, (1, 2), (-2, -2), (3, 3))]
        result = get_on_cubes(test_cubes)
        expected_result = {(1, -2, 3), (2, -2, 3)}
        self.assertSetEqual(expected_result, result)

    def test_get_on_cubes_on_off(self):
        test_cubes = [Cube(True, (0, 1), (0, 1), (0, 1)),
                      Cube(False, (0, 0), (0, 0), (0, 0)),
                      Cube(False, (1, 1), (1, 1), (1, 1))]
        result = get_on_cubes(test_cubes)
        expected_result = {(1, 0, 0), (0, 1, 0), (0, 0, 1),
                           (1, 1, 0), (1, 0, 1), (0, 1, 1)}
        self.assertSetEqual(expected_result, result)

    def test_get_on_cubes_valid_range(self):
        test_cubes = [Cube(True, (-5, 4), (-10, 10), (-3, 4))]
        result = get_on_cubes(test_cubes, (1, 1, 1))
        self.assertEqual(27, len(result))


