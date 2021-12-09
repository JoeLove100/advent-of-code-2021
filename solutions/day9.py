from typing import List, Tuple, Set


def read_input(lines: List[str]) -> List[List[int]]:
    """
    parse input to grid of integers
    """

    arr = []
    for line in lines:
        arr.append(list(map(int, line)))

    return arr


def is_low_point(arr: List[List[int]],
                 i: int,
                 j: int) -> bool:
    """
    check if the value at i, j is a low point
    """
    if i > 0 and arr[i - 1][j] <= arr[i][j]:
        # check value above
        return False
    elif i < len(arr) - 1 and arr[i + 1][j] <= arr[i][j]:
        # check value below
        return False
    elif j > 0 and arr[i][j - 1] <= arr[i][j]:
        # check value to left
        return False
    elif j < len(arr[0]) - 1 and arr[i][j + 1] <= arr[i][j]:
        return False

    return True


def get_sum_of_risk_values_for_low_points(arr: List[List[int]]) -> int:
    """
    A low point is a point at which the values above/below and to the left/right
    are higher than it. The risk value of such a point is its height + 1
    """

    total = 0

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if is_low_point(arr, i, j):
                total += arr[i][j] + 1

    return total


def get_neighbours(arr: List[List[int]],
                   coord: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
    get coordinates of neighbours
    """

    n, m = len(arr), len(arr[0])
    i, j = coord
    neighbours = []
    if i > 0:
        neighbours.append((i - 1, j))
    if i < n - 1:
        neighbours.append((i + 1, j))
    if j > 0:
        neighbours.append((i, j - 1))
    if j < len(arr) - 1:
        neighbours.append((i, j + 1))
    return neighbours


def get_basin_size(arr: List[List[int]],
                   visited: Set[Tuple[int, int]],
                   coord: Tuple[int, int]) -> int:
    """
    get the size of the basin containing point (i, j)
    and mark as visited all co-ordinates in this basin
    """

    size = 0
    stack = [coord]

    while stack:
        current = stack.pop()
        if current in visited:
            continue
        else:
            visited.add(current)
            size += 1

        for neighbour in get_neighbours(arr, current):
            i, j = neighbour
            if arr[i][j] < 9:
                stack.append(neighbour)

    return size


def get_sorted_basin_sizes(arr: List[List[int]]):
    """
    return a sorted list of the basin sizes in
    our array arr
    """

    sizes = []
    visited = set()
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 9 or (i, j) in visited:
                continue
            sizes.append(get_basin_size(arr, visited, (i, j)))

    return sorted(sizes)


if __name__ == "__main__":

    with open("inputs/day9.txt") as input_file:
        data = input_file.read()
        data = data.split()

    height_map = read_input(data)
    print(get_sum_of_risk_values_for_low_points(height_map))
    all_basin_sizes = get_sorted_basin_sizes(height_map)
    print(all_basin_sizes[-1] * all_basin_sizes[-2] * all_basin_sizes[-3])
