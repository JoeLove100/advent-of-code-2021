from typing import List
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
Line = namedtuple("Line", ["start", "end"])


def read_input(lines: List[str]) -> List[Line]:
    """
    parse raw input to a list of lines
    """

    all_lines = []
    for line in lines:
        start, end = line.split(" -> ")
        start_x, start_y = start.split(",")
        start_point = Point(int(start_x), int(start_y))
        end_x, end_y = end.split(",")
        end_point = Point(int(end_x), int(end_y))
        all_lines.append(Line(start_point, end_point))
    return all_lines


def get_number_of_overlapping_points(lines: List[Line],
                                     include_diagonals: bool = False) -> int:
    """
    get the number of points at which two or more lines
    intersect (optionally using horizontal/vertical lines only)
    """

    all_points = set()
    intersections = set()
    for line in lines:

        if line.start.x == line.end.x:
            # is vertical
            start = min(line.start.y, line.end.y)
            end = max(line.start.y, line.end.y)
            for i in range(start, end + 1):
                point = Point(line.start.x, i)
                if point in all_points:
                    intersections.add(point)
                all_points.add(point)
        elif line.start.y == line.end.y:
            # is horizontal
            start = min(line.start.x, line.end.x)
            end = max(line.start.x, line.end.x)
            for i in range(start, end + 1):
                point = Point(i, line.start.y)
                if point in all_points:
                    intersections.add(point)
                all_points.add(point)
        elif include_diagonals:
            # line is diagonal and we want to include it
            grad = (line.end.y - line.start.y) // (line.end.x - line.start.x)
            left_point = line.start if line.start.x < line.end.x else line.end
            for i in range(abs(line.start.x - line.end.x) + 1):
                point = Point(left_point.x + i, left_point.y + i * grad)
                if point in all_points:
                    intersections.add(point)
                all_points.add(point)
    return len(intersections)


if __name__ == "__main__":

    with open("inputs/day5.txt") as input_file:
        data = input_file.read()
        data = data.split("\n")

    input_lines = read_input(data)
    print(get_number_of_overlapping_points(input_lines, False))
    print(get_number_of_overlapping_points(input_lines, True))
