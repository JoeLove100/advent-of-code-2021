from typing import List, Set, Tuple
import itertools

Coordinate = Tuple[int, int]


def print_board(n: int, m: int,
                east: Set[Coordinate],
                south: Set[Coordinate]) -> None:
    """
    print board for debugging purpose
    """

    arr = [["." for _ in range(m)] for _ in range(n)]
    for i, j in east:
        arr[i][j] = ">"
    for i, j in south:
        arr[i][j] = "v"

    for row in arr:
        print("".join(row))


def get_days_til_stationary(arr: List[List[str]],
                            debug: bool = False) -> int:
    """
    get the number of days until no sea
    cucumber can move
    """

    n, m =  len(arr), len(arr[0])
    east, south = set(), set()
    for i, j in itertools.product(range(n), range(m)):
        if arr[i][j] == ">":
            east.add((i, j))
        elif arr[i][j] == "v":
            south.add((i, j))

    days = 0
    while True:
        moves = 0
        # do east facing herd first
        east_new = set()
        for i, j in east:
            j_next = (j + 1) % m
            if (i, j_next) not in east and (i, j_next) not in south:
                east_new.add((i, j_next))
                moves += 1
            else:
                east_new.add((i, j))
        east = east_new

        # now do south facing herd
        south_new = set()
        for i, j in south:
            i_next = (i + 1) % n
            if (i_next, j) not in south and (i_next, j) not in east:
                south_new.add((i_next, j))
                moves += 1
            else:
                south_new.add((i, j))
        south = south_new

        days += 1
        if moves == 0:
            return days

        if debug:
            print(f"Board after {days} steps ({moves} move(s)):")
            print_board(n, m, east, south)
            print(" ")


if __name__ == "__main__":

    with open("inputs/day25.txt") as input_file:
        data = input_file.readlines()
        data = [list(line.replace("\n", "")) for line in data]

    print(get_days_til_stationary(data, False))
