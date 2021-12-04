import unittest
from solutions.day4 import read_input, Board, get_winning_score, get_final_winning_score


class TestDay4A(unittest.TestCase):

    @classmethod
    def get_board(cls):
        grid = [[1, 2], [3, 4]]
        return Board(grid)

    def test_can_read_input(self):

        with open("test_fixtures/day_4_input.txt") as test_input:
            test_data = test_input.read().split("\n")

        result = read_input(test_data)
        self.assertSequenceEqual([1, 2, 3], result[0])
        self.assertEqual(2, len(result[1]))

    def test_can_build_board_correctly(self):

        result = self.get_board()
        self.assertSequenceEqual([0, 0], result.row_sums)
        self.assertEqual([0, 0], result.col_sums)
        self.assertFalse(result.has_won)
        self.assertDictEqual({1: (0, 0), 2: (0, 1),
                              3: (1, 0), 4: (1, 1)}, result.entries)

    def test_full_row_wins(self):
        result = self.get_board()
        result.update(1)
        result.update(2)
        self.assertDictEqual({3: (1, 0), 4: (1, 1)}, result.entries)
        self.assertTrue(result.has_won)

    def test_full_column_wins(self):
        result = self.get_board()
        result.update(2)
        result.update(4)
        self.assertDictEqual({1: (0, 0), 3: (1, 0)}, result.entries)
        self.assertTrue(result.has_won)

    def test_get_winning_score(self):
        board_1 = Board([[1, 2], [3, 4]])
        board_2 = Board([[5, 6], [7, 8]])
        board_3 = Board([[5, 6], [7, 10]])
        boards = [board_1, board_2, board_3]
        numbers = [1, 5, 4, 7, 2]
        result = get_winning_score(numbers, boards)
        self.assertEqual(14 * 7, result)


class TestDay4B(unittest.TestCase):

    def test_get_final_winning_score(self):
        board_1 = Board([[1, 2], [3, 4]])
        board_2 = Board([[5, 6], [7, 8]])
        board_3 = Board([[5, 6], [7, 10]])
        boards = [board_1, board_2, board_3]
        numbers = [1, 5, 4, 7, 2]
        result = get_final_winning_score(numbers, boards)
        self.assertEqual(6, result)
