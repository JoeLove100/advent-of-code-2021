import unittest
from solutions.day10 import get_illegal_character, get_illegal_bracket_score, get_completion_brackets, \
    get_completion_string_score


class TestDay10A(unittest.TestCase):

    def test_valid_returns_none(self):
        test_brackets = "([])<<>(())"
        self.assertIsNone(get_illegal_character(test_brackets))

    def test_gets_first_invalid_bracket(self):
        test_brackets = "(([])}>"
        self.assertEqual("}", get_illegal_character(test_brackets))

    def test_get_bracket_score(self):
        test_brackets = [")", None, "]", "}", ">", ")"]
        self.assertEqual(26397, get_illegal_bracket_score(test_brackets))


class TestDay10B(unittest.TestCase):

    def test_invalid_is_empty(self):
        test_brackets = "(])"
        result = get_completion_brackets(test_brackets)
        self.assertSequenceEqual([], result)

    def test_returns_completion_brackets_if_valid(self):
        test_brackets = "(()[<>{"
        result = get_completion_brackets(test_brackets)
        self.assertSequenceEqual(["}", "]", ")"], result)

    def test_get_completion_score(self):
        test_completion_string = list(")>}]")
        result = get_completion_string_score(test_completion_string)
        self.assertEqual(242, result)
