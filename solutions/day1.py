from typing import List


def get_number_of_increases(arr: List[int]) -> int:
    """
    return the number of times the seris defined by
    arr increases
    """

    increase = 0
    for i, n in enumerate(arr[1:]):
        if n > arr[i]:
            increase += 1
    return increase


def get_moving_triplet_sum_increases(arr: List[int]) -> int:
    """
    get the number of instances wherein the sum of n, n+1, n+2
    in the sequence arr is less than that of n+1, n+2, n+3
    """

    if len(arr) < 3:
        raise ValueError("Need at least three numbers")

    increase = 0
    i, j = 0, 3
    while j < len(arr):
        if arr[j] > arr[i]:
            increase += 1
        i, j = i + 1, j + 1
    return increase


if __name__ == "__main__":

    with open("inputs/day1.txt") as input_file:
        data = input_file.read().split("\n")
        data = [int(n) for n in data]

    print(get_number_of_increases(data))
    print(get_moving_triplet_sum_increases(data))
