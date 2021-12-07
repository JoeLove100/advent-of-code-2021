from typing import List
from bisect import bisect_left
import math


def get_min_distance(arr: List[int]) -> int:
    """
    find the point which is the minimal total
    distance from all the points in arr
    """

    arr = sorted(arr)
    start, end = min(arr), max(arr) + 1
    total = sum(arr) - len(arr) * start
    min_distance = total
    for i in range(start + 1, end):
        left_entries = bisect_left(arr, i)
        right_entries = len(arr) - left_entries
        total += (left_entries - right_entries)
        min_distance = min(min_distance, total)
    return min_distance


def get_min_distance_2(arr: List[int]) -> int:
    """
    get the minimum distance where now each additional
    unit requires n rather than 1 unit of fuel
    """

    # TODO: runs fine, but surely there's a better solution?

    arr = sorted(arr)
    min_distance = math.inf
    start, end = min(arr), max(arr) + 1
    for i in range(start, end):
        distance = 0
        for n in arr:
            d = abs(n - i)
            distance += d * (d + 1) // 2
        min_distance = min(distance, min_distance)

    return min_distance


if __name__ == "__main__":

    with open("inputs/day7.txt") as input_file:
        data = input_file.read()
        data = list(map(int, data.split(",")))

    print(get_min_distance(data))
    print(get_min_distance_2(data))
