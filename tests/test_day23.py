import unittest
from solutions.day23 import get_min_cost


class TestDay23A(unittest.TestCase):

    def test_finished_board_has_cost_zero(self):
        test_board = [None, None, ["A", "A"], None, ["B", "B"], None,
                      ["C", "C"], None, ["D", "D"], None, None]
        result, _ = get_min_cost(test_board, [True for _ in range(len(test_board))], dict())
        self.assertEqual(0, result)

    def test_one_move_to_go_from_end(self):
        test_board = [None, "C", ["A", "A"], None, ["B", "B"], None,
                      ["C"], None, ["D", "D"], None, None]
        result, _ = get_min_cost(test_board, [True for _ in range(len(test_board))], dict())
        self.assertEqual(600, result)

    def test_two_moves_to_go(self):
        test_board = [None, "C", ["A"], None, ["B", "B"], None,
                      ["C", "A"], None, ["D", "D"], None, None]
        result, _ = get_min_cost(test_board, [True for _ in range(len(test_board))], dict())
        self.assertEqual(606, result)
