import unittest
from collections import defaultdict
from solutions.day12 import read_input, count_paths_to_end, count_paths_to_end_2


class TestDay12A(unittest.TestCase):

    def test_read_input(self):

        with open("test_fixtures/day_12_input.txt") as input_file:
            data = input_file.read()
            data = data.split("\n")

        result = read_input(data)
        expected_result = {"start": ["A", "b"],
                           "A": ["start", "c", "b", "end"],
                           "c": ["A"],
                           "b": ["start", "A", "d", "end"],
                           "d": ["b"],
                           "end": ["A", "b"]}
        self.assertDictEqual(expected_result, result)

    def test_count_paths_to_end(self):
        test_adj_matrix = {"start": ["A", "b"],
                           "A": ["start", "c", "b", "end"],
                           "c": ["A"],
                           "b": ["start", "A", "d", "end"],
                           "d": ["b"],
                           "end": ["A", "b"]}
        result = count_paths_to_end(test_adj_matrix, "start", set())
        self.assertEqual(10, result)


class TestDay12B(unittest.TestCase):

    def test_count_paths_to_end_2(self):
        test_adj_matrix = {"start": ["A", "b"],
                           "A": ["start", "c", "b", "end"],
                           "c": ["A"],
                           "b": ["start", "A", "d", "end"],
                           "d": ["b"],
                           "end": ["A", "b"]}
        test_visited = defaultdict(lambda: 0)
        result = count_paths_to_end_2(test_adj_matrix, "start", test_visited)
        self.assertEqual(36, result)
