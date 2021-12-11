import itertools
import math
from copy import deepcopy
from typing import List, Tuple, Optional


def get_neighbours(arr: List[List[int]],
                   i: int,
                   j: int) -> List[Tuple[int, int]]:

    neighbours = []
    n, m = len(arr), len(arr[0])
    if i > 0:
        neighbours.append((i - 1, j))
        if j > 0:
            neighbours.append((i - 1, j - 1))
        if j < n - 1:
            neighbours.append((i - 1, j + 1))
    if i < m - 1:
        neighbours.append((i + 1, j))
        if j > 0:
            neighbours.append((i + 1, j - 1))
        if j < n - 1:
            neighbours.append((i + 1, j + 1))
    if j > 0:
        neighbours.append((i, j - 1))
    if j < n - 1:
        neighbours.append((i, j + 1))
    return neighbours


def count_flashes(arr: List[List[int]],
                  n_steps: Optional[int] = None,
                  print_freq: int = 0) -> int:
    """
    if n_steps is defined the count the number of octopus
    flashes. If not, then return the first step on which
    all octopuses flash
    """

    flash_count = 0
    n, m = len(arr), len(arr[0])
    k = 0
    steps_to_run = n_steps if n_steps else math.inf
    while k < steps_to_run:
        has_flashed = set()
        will_flash = []
        flashes_in_step = 0

        # 1) first increase each number by 1
        for i, j in itertools.product(range(n), range(m)):
            arr[i][j] += 1
            if arr[i][j] > 9:
                will_flash.append((i, j))

        # 2) now handle flashes
        while will_flash:
            i, j = will_flash.pop()
            flashes_in_step += 1
            has_flashed.add((i, j))
            for i_n, j_n in get_neighbours(arr, i, j):
                if (i_n, j_n) not in has_flashed:
                    arr[i_n][j_n] += 1
                    if arr[i_n][j_n] == 10:
                        will_flash.append((i_n, j_n))

        # 3) ensure all flashed set to zero
        for i, j in has_flashed:
            arr[i][j] = 0

        # 4) optionally, print our array (for debugging)
        if print_freq and k % print_freq == 0:
            print("------")
            print(f"After {k + 1} steps")
            for row in arr:
                print(row)
            print("------")

        # 5) next step
        if n_steps is None and flashes_in_step == n * m:
            return k + 1
        else:
            flash_count += flashes_in_step
            k += 1

    return flash_count


if __name__ == "__main__":

    with open("inputs/day11.txt") as input_file:
        data = input_file.read()
        data = data.split("\n")
        data = [list(map(int, line)) for line in data]

    print(count_flashes(deepcopy(data), 100))
    print(count_flashes(data))
