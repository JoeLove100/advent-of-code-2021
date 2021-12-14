import unittest
from solutions.day14 import read_input


class TestDay14(unittest.TestCase):

    def test_read_input(self):

        with open("test_fixtures/day_14_input.txt") as input_file:
            data = input_file.readlines()

        polymer_result, map_result = read_input(data)
        self.assertEqual("ABCDE", polymer_result)
        expected_map = {"AB": "G", "HY": "P", "AG": "D"}
        self.assertDictEqual(expected_map, map_result)

    # TODO: write more tests here...
