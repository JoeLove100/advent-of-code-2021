import unittest
from solutions.day21 import play_game, get_total_wins


class TestDay21A(unittest.TestCase):

    def test_play_game(self):
        result = play_game(4, 8)
        self.assertEqual(1000, result[0])
        self.assertEqual(745, result[1])
        self.assertEqual(993, result[2])


class TestDay12B(unittest.TestCase):

    def test_get_total_wins(self):
        result = get_total_wins(4, 8, 0, 0, dict())
        self.assertEqual(result[0], 444356092776315 * 27)
        self.assertEqual(result[1], 341960390180808)
