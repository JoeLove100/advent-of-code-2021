import itertools
from typing import List, Tuple, Optional, Set
from dataclasses import dataclass


@dataclass
class Cube:
    turn_on: bool
    x_range: Tuple[int, int]
    y_range: Tuple[int, int]
    z_range: Tuple[int, int]


def read_input(lines: List[str]) -> List[Cube]:
    """
    parse raw input to a list of cubes to be turned
    on or off
    """

    def to_int(n: str):
        if n[0] == "-":
            return -int(n[1:])
        else:
            return int(n)

    cubes = []
    for line in lines:
        on_or_off, ranges = line.split(" ")
        ranges = ranges.split(",")
        x_range = tuple([to_int(n) for n in ranges[0][2:].split("..")])
        y_range = tuple([to_int(n) for n in ranges[1][2:].split("..")])
        z_range = tuple([to_int(n) for n in ranges[2][2:].split("..")])
        cube = Cube(on_or_off == "on", x_range, y_range, z_range)
        cubes.append(cube)
    return cubes


def get_on_cubes(cubes: List[Cube],
                 valid_range: Optional[Tuple[int, int, int]] = None) \
        -> Set[Tuple[int, int, int]]:
    """
    get the cubes that are turned on after we have
    processed all the cube on/off instructions - can
    specify and optional valid range
    """

    on_cubes = set()
    for cube in cubes:
        x_0, x_1 = cube.x_range
        y_0, y_1 = cube.y_range
        z_0, z_1 = cube.z_range

        if valid_range:
            x_0 = max(x_0, -valid_range[0])
            x_1 = min(x_1, valid_range[0])
            y_0 = max(y_0, -valid_range[1])
            y_1 = min(y_1, valid_range[1])
            z_0 = max(z_0, -valid_range[2])
            z_1 = min(z_1, valid_range[2])

        for i, j, k in itertools.product(range(x_0, x_1 + 1),
                                         range(y_0, y_1 + 1),
                                         range(z_0, z_1 + 1)):
            if cube.turn_on:
                on_cubes.add((i, j, k))
            else:
                on_cubes.discard((i, j, k))

    return on_cubes


if __name__ == "__main__":

    with open("inputs/day22.txt") as input_file:
        data = input_file.readlines()

    all_cubes = read_input(data)
    all_on_cubes = get_on_cubes(all_cubes, (50, 50, 50))
    print(len(all_on_cubes))
