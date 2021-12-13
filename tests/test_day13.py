import unittest
from solutions.day13 import Instruction, read_inputs, fold_vertical, fold_horizontal, get_display


class TestDay13A(unittest.TestCase):

    def test_read_inputs(self):

        with open("test_fixtures/day_13_input.txt") as input_file:
            data = input_file.readlines()

        coord_results, instruction_results = read_inputs(data)
        expected_coords = {(1, 3), (4, 7), (10, 12)}
        self.assertSetEqual(expected_coords, coord_results)
        expected_instructions = [Instruction("y", 4), Instruction("x", 2)]
        self.assertSequenceEqual(expected_instructions, instruction_results)

    def test_fold_on_vertical(self):

        test_coords = {(0, 0), (1, 0), (5, 0), (2, 2), (4, 3)}
        result = fold_vertical(test_coords, 3)
        expected_coords = {(1, 0), (2, 0), (0, 2), (0, 3)}
        self.assertSetEqual(expected_coords, result)

    def test_fold_on_horizontal(self):

        test_coords = {(1, 0), (2, 0), (1, 2), (2, 2), (2, 3)}
        result = fold_horizontal(test_coords, 1)
        expected_coords = {(1, 0), (2, 0), (2, -1)}
        self.assertSetEqual(expected_coords, result)


class TestDay13B(unittest.TestCase):

    def test_display_grid(self):
        test_coords = {(1, 0), (2, 0), (2, -1)}
        result = get_display(test_coords)
        expected_result = [".#", "##"]
        self.assertEqual(expected_result, result)

    def test_display_figure(self):
        test_coords = {(1, -2), (3, -2), (1, -1), (3, -1), (1, 0), (2, 0), (3, 0),
                       (3, 1), (3, 2)}
        result = get_display(test_coords)
        expected_result = ["#.#", "#.#", "###", "..#", "..#"]
        self.assertEqual(expected_result, result)
