import unittest
from solutions.day8 import Display, read_input, count_easy_integers, map_letters, \
    get_decoded_numbers, decode_outputs


class TestDay8A(unittest.TestCase):

    def test_read_input(self):
        with open("test_fixtures/day_8_input.txt") as input_file:
            test_input = input_file.read()
            test_input = test_input.split("\n")

        result = read_input(test_input)
        expected_result = [Display(["abd", "ac", "abdg"], ["ag", "agc"]),
                           Display(["gca", "bdca", "ef"], ["ef", "agc"])]
        self.assertEqual(expected_result, result)

    def test_count_easy_integers(self):
        test_displays = [Display(["abc"], ["ad", "efgc", "efd"]),
                         Display(["efda", "gc"], ["abcdefg", "abcdef"])]
        result = count_easy_integers(test_displays)
        self.assertEqual(4, result)


class TestDay8B(unittest.TestCase):

    def test_map_letters(self):
        test_input = ["acedgfb", "cdfbe", "gcdfa", "fbcad", "dab", "cefabd",
                      "cdfgeb", "eafb", "cagedb", "ab"]
        result = map_letters(test_input)
        expected_result = {"a": "d",
                           "b": "e",
                           "c": "a",
                           "d": "f",
                           "e": "g",
                           "f": "b",
                           "g": "c"}
        self.assertDictEqual(result, expected_result)

    def test_get_decoded_numbers(self):
        test_decode_map = {"a": "d", "b": "e", "c": "a", "d": "f",
                           "e": "g", "f": "b", "g": "c"}
        result = get_decoded_numbers(test_decode_map)
        expected_result = {"abcdeg": 0,
                           "ab": 1,
                           "acdfg": 2,
                           "abcdf": 3,
                           "abef": 4,
                           "bcdef": 5,
                           "bcdefg": 6,
                           "abd": 7,
                           "abcdefg": 8,
                           "abcdef": 9}
        self.assertDictEqual(expected_result, result)

    def test_decode_output(self):
        test_output = ["cdfeb", "fcadb", "cdfeb", "cdbaf"]
        test_decoded_numbers = {"abcdeg": 0, "ab": 1, "acdfg": 2, "abcdf": 3, "abef": 4,
                                "bcdef": 5, "bcdefg": 6, "abd": 7, "abcdefg": 8, "abcdef": 9}
        result = decode_outputs(test_output, test_decoded_numbers)
        self.assertEqual(5353, result)
