import unittest
from solutions.day18 import SnailfishNumber, parse_snailfish_number, convert_snailfish_to_raw, \
    add_snailfish_numbers, reduce_snailfish_number, add_and_reduce_numbers, get_magnitude


class TestDay18A(unittest.TestCase):

    def test_parse_snailfish_number(self):
        test_raw = "[[[9,2],[[2,9],0]],[1,[[2,3],0]]]"
        result = parse_snailfish_number(test_raw)
        expected_result = SnailfishNumber([3, 0, 2, 0, 0, 1, 2, 0, 0],
                                          [0, 0, 1, 0, 1, 2, 0, 0, 1],
                                          [9, 2, 2, 9, 0, 1, 2, 3, 0])
        self.assertEqual(expected_result, result)

    def test_convert_snailfish_to_raw(self):
        test_snailfish = SnailfishNumber([3, 0, 2, 0, 0, 1, 2, 0, 0],
                                         [0, 0, 1, 0, 1, 2, 0, 0, 1],
                                         [9, 2, 2, 9, 0, 1, 2, 3, 0])
        result = convert_snailfish_to_raw(test_snailfish)
        expected_result = "[[[9,2],[[2,9],0]],[1,[[2,3],0]]]"
        self.assertEqual(expected_result, result)

    def test_add_snailfish_numbers(self):
        test_snailfish_1 = SnailfishNumber([1, 0], [0, 0], [2, 3])
        test_snailfish_2 = SnailfishNumber([2, 0, 0], [0, 0, 1], [4, 6, 1])
        result = add_snailfish_numbers(test_snailfish_1, test_snailfish_2)
        expected_result = SnailfishNumber([2, 0, 2, 0, 0], [0, 0, 1, 0, 1], [2, 3, 4, 6, 1])
        self.assertEqual(expected_result, result)

    def test_handle_explode_at_start(self):
        test_snailfish = SnailfishNumber([5, 5, 0, 0, 0, 0],
                                         [0, 0, 1, 1, 1, 1],
                                         [9, 8, 1, 2, 3, 4])
        result = reduce_snailfish_number(test_snailfish)
        expected_result = SnailfishNumber([4, 0, 0, 0, 0],
                                          [0, 0, 1, 1, 1],
                                          [0, 9, 2, 3, 4])
        self.assertEqual(expected_result, result)

    def test_handle_explode_at_end(self):
        test_snailfish = SnailfishNumber([1, 1, 1, 1, 1, 0],
                                         [0, 0, 0, 0, 0, 0],
                                         [7, 6, 5, 4, 3, 2])
        result = reduce_snailfish_number(test_snailfish)
        expected_result = SnailfishNumber([1, 1, 1, 1, 0],
                                          [0, 0, 0, 0, 0],
                                          [7, 6, 5, 7, 0])
        self.assertEqual(expected_result, result)

    def test_handle_explode_in_middle(self):
        test_snailfish = SnailfishNumber([2, 1, 1, 1, 0, 0],
                                         [0, 0, 0, 0, 0, 4],
                                         [6, 5, 4, 3, 2, 1])
        result = reduce_snailfish_number(test_snailfish)
        expected_result = SnailfishNumber([2, 1, 1, 0, 0],
                                          [0, 0, 0, 0, 3],
                                          [6, 5, 7, 0, 3])
        self.assertEqual(expected_result, result)

    def test_handle_split(self):
        test_snailfish = SnailfishNumber([1, 1, 0], [0, 0, 0], [1, 11, 2])
        result = reduce_snailfish_number(test_snailfish)
        expected_result = SnailfishNumber([1, 2, 0, 0], [0, 0, 0, 1], [1, 5, 6, 2])
        self.assertEqual(expected_result, result)

    def test_multiple_operations(self):
        test_snailfish = SnailfishNumber([5, 5, 0, 0, 1, 2, 0, 0, 1, 0],
                                         [0, 0, 1, 1, 1, 0, 0, 1, 3, 0],
                                         [4, 3, 4, 4, 7, 8, 4, 8, 1, 1])
        result = reduce_snailfish_number(test_snailfish)
        expected_result = SnailfishNumber([4, 0, 0, 2, 0, 1, 0, 1, 0],
                                          [0, 0, 1, 1, 0, 1, 0, 3, 0],
                                          [0, 7, 4, 7, 8, 6, 0, 7, 1])
        self.assertEqual(result, expected_result)

    def test_multiple_additions(self):
        test_numbers = [SnailfishNumber([1, 0], [0, 0], [1, 1]),
                        SnailfishNumber([1, 0], [0, 0], [2, 2]),
                        SnailfishNumber([1, 0], [0, 0], [3, 3]),
                        SnailfishNumber([1, 0], [0, 0], [4, 4])]
        result = add_and_reduce_numbers(test_numbers)
        expected_result = SnailfishNumber([4, 0, 1, 0, 1, 0, 1, 0],
                                          [0, 0, 1, 0, 2, 0, 2, 0],
                                          [1, 1, 2, 2, 3, 3, 4, 4])
        self.assertEqual(expected_result, result)

    def test_get_magnitude_integers(self):
        self.assertEqual(19, get_magnitude([5, 2]))

    def test_get_magnitude_lists(self):
        test_arr = [[[[5, 0], [7, 4]], [5, 5]], [6, 6]]
        result = get_magnitude(test_arr)
        self.assertEqual(1137, result)
