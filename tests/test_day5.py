import unittest
from solutions.day5 import Point, Line, read_input, get_number_of_overlapping_points


class TestDay5A(unittest.TestCase):

    def test_read_input(self):
        test_input = ["0,1 -> 5,10", "3,3 -> 3,8", "11,5 -> 1,5"]
        result = read_input(test_input)
        expected_result = [Line(Point(0, 1), Point(5, 10)),
                           Line(Point(3, 3), Point(3, 8)),
                           Line(Point(11, 5), Point(1, 5))]
        self.assertSequenceEqual(expected_result, result)

    def test_horizontal_line_intersections(self):
        test_lines = [Line(Point(2, 4), Point(10, 4)),
                      Line(Point(7, 4), Point(5, 4))]
        result = get_number_of_overlapping_points(test_lines)
        self.assertEqual(3, result)

    def test_vertical_line_intersection(self):
        test_lines = [Line(Point(5, 8), Point(5, 3)),
                      Line(Point(5, 4), Point(5, 5))]
        result = get_number_of_overlapping_points(test_lines)
        self.assertEqual(2, result)

    def test_multiple_intersections_at_point(self):
        test_lines = [Line(Point(5, 8), Point(5, 3)),
                      Line(Point(5, 4), Point(5, 5)),
                      Line(Point(4, 5), Point(6, 5))]
        result = get_number_of_overlapping_points(test_lines)
        self.assertEqual(2, result)


class TestDay5B(unittest.TestCase):

    def test_can_ignore_diagonals(self):
        test_lines = [Line(Point(0, 0), Point(3, 3)),
                      Line(Point(3, 0), Point(3, 3))]
        result = get_number_of_overlapping_points(test_lines)
        self.assertEqual(0, result)

    def test_can_include_diagonals(self):
        test_lines = [Line(Point(0, 0), Point(3, 3)),
                      Line(Point(0, 4), Point(4, 0))]
        result = get_number_of_overlapping_points(test_lines, True)
        self.assertEqual(1, result)