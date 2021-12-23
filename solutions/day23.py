from typing import List, Union, Dict, Tuple
from copy import deepcopy
import math

MX_SIZE = 2


cost_by_letter = {"A": 1, "B": 10, "C": 100, "D": 1000}
destinations = {"A": 2, "B": 4, "C": 6, "D": 8}
completed = [None,  None, ["A"] * MX_SIZE, None, ["B"] * MX_SIZE, None,
             ["C"] * MX_SIZE, None, ["D"] * MX_SIZE, None, None]


def get_min_cost(arr: List[List[Union[str, None]]],
                 unoccupied: List[bool],
                 memo: Dict[str, Tuple[int, List[str]]]) -> Tuple[int, List[str]]:

    board_as_string = board_to_string(arr)
    if board_as_string in memo:
        return memo[board_as_string]

    costs = [(math.inf, ["NO SOLUTION"])]
    # are we done?
    if arr == completed:
        return 0, ["FINISHED"]

    # first look at destinations:
    for i in [2, 4, 6, 8]:
        if arr[i] == completed[i]:
            # already filled with correct letter
            continue
        elif len(set(arr[i])) == 1 and arr[i][0] == completed[i][0]:
            # only contains correct elements, so don't move
            continue
        elif len(arr[i]) == 0:
            # empty so can't do anything
            continue
        else:
            # lets move the first available element somewhere else
            letter = arr[i][-1]
            # first see if we can move to the destination
            dstn = destinations[letter]
            if (arr[dstn] == [] or set(arr[dstn]) == {letter}) and all(unoccupied[min(i, dstn): max(i, dstn) + 1]):
                # valid to move to destination so create next array
                next_arr = deepcopy(arr)
                next_arr[i].pop()
                next_arr[dstn].append(letter)
                steps = abs(dstn - i) + (MX_SIZE + 1 - len(next_arr[dstn])) + (MX_SIZE - len(next_arr[i]))
                move_cost = steps * cost_by_letter[letter]
                additional_cost, additional_moves = get_min_cost(next_arr, unoccupied, memo)
                instruction = f"Move {letter} from {i} to destination for cost {move_cost}"
                costs.append((move_cost + additional_cost, [instruction] + additional_moves))

            # now lets see if we can move to any of the other spaces
            for j in [0, 1, 3, 5, 7, 9, 10]:
                if arr[j] is None and all(unoccupied[min(i, j): max(i, j) + 1]):
                    # valid to move to this space
                    next_arr = deepcopy(arr)
                    next_arr[j] = next_arr[i].pop()
                    steps = abs(i - j) + (MX_SIZE - len(next_arr[i]))
                    next_unoccupied = deepcopy(unoccupied)
                    next_unoccupied[j] = False
                    move_cost = steps * cost_by_letter[letter]
                    additional_cost, additional_moves = get_min_cost(next_arr, next_unoccupied, memo)
                    instruction = f"Move {letter} from {i} to space {j} for cost {move_cost}"
                    costs.append((move_cost + additional_cost, [instruction] + additional_moves))

    # finished checking destinations, move now look at non-destination positions
    for i in [0, 1, 3, 5, 7, 9, 10]:
        if arr[i] is not None:
            letter = arr[i]
            # only option is to move to its destination
            dstn = destinations[letter]
            if (len(arr[dstn]) == 0 or set(arr[dstn]) == {letter}) and all(unoccupied[min(i, dstn) + 1: max(i, dstn)]):
                # can move to bottom position of destination

                # move letter from i to dstn on the board
                next_arr = deepcopy(arr)
                next_arr[i] = None
                next_arr[dstn].append(letter)

                # mark the current spot as unoccupied again
                next_unoccupied = deepcopy(unoccupied)
                next_unoccupied[i] = True

                steps_along = abs(i - dstn)
                steps_down = (MX_SIZE + 1 - len(next_arr[dstn]))
                steps = steps_along + steps_down
                move_cost = steps * cost_by_letter[letter]
                additional_cost, additional_moves = get_min_cost(next_arr, next_unoccupied, memo)
                instruction = f"Move {letter} from space {i} to destination for cost {move_cost} " \
                              f"({steps_along} along and {steps_down} down, destination is now {next_arr[dstn]})"
                costs.append((move_cost + additional_cost, [instruction] + additional_moves))

    memo[board_as_string] = min(costs)
    return memo[board_as_string]


def board_to_string(board: List[List[Union[str, None]]]):

    as_string = "|"
    for i, c in enumerate(board):
        if i in [2, 4, 6, 8]:
            as_string += "*"
        if c is None:
            as_string += "_"
        elif type(c) == list:
            as_string += "".join(c)
        else:
            as_string += c
        if i in [2, 4, 6, 8]:
            as_string += "*"
        as_string += "|"
    return as_string


if __name__ == "__main__":

    # change mx_size for parts 1/2

    start_board = [None,
                   None,
                   ["C", "D", "D", "A"],
                   None,
                   ["C", "B", "C", "D"],
                   None,
                   ["D", "A", "B", "A"],
                   None,
                   ["B", "C", "A", "B"],
                   None,
                   None]
    start_unoccupied = [True for _ in range(len(start_board))]
    total_cost, total_moves = get_min_cost(start_board, start_unoccupied, dict())
    print(total_cost)