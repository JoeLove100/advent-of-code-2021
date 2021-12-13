from typing import Set, Tuple, List
from collections import namedtuple
import itertools

Instruction = namedtuple("Instruction", ["direction", "value"])
Coordinates = Set[Tuple[int, int]]


def fold_vertical(coords: Coordinates,
                  x: int) -> Coordinates:
    """
    get new set of coordinates after performing a
    fold around the vertical line defined by x - note
    that we fold LEFT
    """

    new_coords = set()
    for i, j in coords:
        if i > x:
            # to the right of the fold so no change
            new_coords.add((i - (x + 1), j))
        else:
            # to the left so we need to fold over
            new_coords.add((x - (i + 1), j))

    return new_coords


def fold_horizontal(coords: Coordinates,
                    y: int) -> Coordinates:
    """
    get new set of coordinates after performing a
    fold around the horizontal line defined by y - note
    that we fold UP
    """

    new_coords = set()
    for i, j in coords:
        if j < y:
            # above the fold line so no change
            new_coords.add((i, j))
        else:
            # below so we need to fold over
            new_coords.add((i, 2 * y - j))

    return new_coords


def read_inputs(lines: List[str]) -> Tuple[Coordinates, List[Instruction]]:
    """
    parse the given input to our set of coordinates
    and a list of folding instructions
    """

    coords = set()
    instructions = []

    # 1) first do the instructions
    while lines[-1] not in ("\n", ""):
        direction, val = lines.pop().split("=")
        instruction = Instruction(direction[-1], int(val))
        instructions.append(instruction)

    lines.pop()

    # 2) now get our coordinates
    while lines:
        i, j = lines.pop().split(",")
        coords.add((int(i), int(j)))
    return coords, list(reversed(instructions))


def get_display(coords: Coordinates) -> List[str]:
    """
    convert a set of coordinates of points to a
    printable array that will reveal our code
    """

    # get min and max of our current coordinates
    min_x = min([c[0] for c in coords])
    max_x = max([c[0] for c in coords])
    min_y = min([c[1] for c in coords])
    max_y = max([c[1] for c in coords])

    # shift back to origin at (0, 0)
    display_coords = set()
    for i, j in coords:
        display_coords.add((i - min_x, j - min_y))

    # create our display grid
    max_x -= min_x
    max_y -= min_y
    display = [["." for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # fill in required points on the display grid
    for i, j in itertools.product(range(max_x + 1), range(max_y + 1)):
        if (i, j) in display_coords:
            display[j][i] = "#"

    display = ["".join(line) for line in display]
    return display


if __name__ == "__main__":

    with open("inputs/day13.txt") as input_file:
        data = input_file.read()
        data = data.split("\n")

    point_coordinates, all_instructions = read_inputs(data)

    for instr in all_instructions:
        if instr.direction == "x":
            new_coordinates = fold_vertical(point_coordinates, instr.value)
        else:
            new_coordinates = fold_horizontal(point_coordinates, instr.value)
        print(len(new_coordinates))
        point_coordinates = new_coordinates

    disp = get_display(point_coordinates)
    for line in disp:
        # TODO: I appear to need to reverse each line, but I am not sure why...
        print("".join(reversed(line)))
