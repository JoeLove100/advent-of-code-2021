import unittest
from solutions.day2 import Submarine


class TestDay2A(unittest.TestCase):

    def test_can_create_submarine(self):
        sub = Submarine()
        self.assertEqual(0, sub.x)
        self.assertEqual(0, sub.y)

    def test_move_up(self):
        sub = Submarine()
        sub.move(["up 2"])
        self.assertEqual(-2, sub.y)
        self.assertEqual(0, sub.x)

    def test_move_down(self):
        sub = Submarine()
        sub.move(["down 4"])
        self.assertEqual(4, sub.y)
        self.assertEqual(0, sub.x)

    def test_move_forward(self):
        sub = Submarine()
        sub.move(["forward 6"])
        self.assertEqual(0, sub.y)
        self.assertEqual(6, sub.x)

    def test_unknown_magnitude(self):
        sub = Submarine()
        with self.assertRaises(ValueError):
            sub.move(["forward a"])

    def test_unknown_direction(self):
        sub = Submarine()
        with self.assertRaises(ValueError):
            sub.move(["sideways 6"])

    def test_multiple_moves(self):
        sub = Submarine()
        test_moves = ["forward 4", "down 2", "forward 1", "up 7"]
        sub.move(test_moves)
        self.assertEqual(-5, sub.y)
        self.assertEqual(5, sub.x)


class TestDay2B(unittest.TestCase):

    def test_aim_updates_on_move_up(self):
        sub = Submarine(use_aim=True)
        sub.move(["up 4"])
        self.assertEqual(-4, sub.aim)

    def test_aim_updates_on_move_down(self):
        sub = Submarine(use_aim=True)
        sub.move(["down 5"])
        self.assertEqual(5, sub.aim)

    def test_forward_uses_aim(self):
        sub = Submarine(start_aim=4, use_aim=True)
        sub.move(["forward 3"])
        self.assertEqual(12, sub.y)

    def test_multiple_moves_with_aim(self):
        sub = Submarine(use_aim=True)
        test_moves = ["forward 5", "down 5", "forward 8", "up 3",
                      "down 8", "forward 2"]
        sub.move(test_moves)
        self.assertEqual(15, sub.x)
        self.assertEqual(60, sub.y)
