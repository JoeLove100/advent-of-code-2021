import ast
import itertools
from typing import List, Union
from dataclasses import dataclass


@dataclass
class SnailfishNumber:

    open: List[int]  # number of open brackets directly before ith number
    close: List[int]  # number of close brackets directly before ith number
    values: List[int]  # actual values for our Snailfish number


def parse_snailfish_number(raw: str) -> SnailfishNumber:
    """
    parse raw representation to a
    snailfish number
    """

    open_count = 0
    close_count = 0
    number = SnailfishNumber([], [], [])
    for c in raw:
        if c.isnumeric():
            number.close.append(close_count)
            close_count = 0
            number.open.append(open_count)
            open_count = 0
            number.values.append(int(c))
        elif c == "[":
            open_count += 1
        elif c == "]":
            close_count += 1

    return number


def convert_snailfish_to_raw(number: SnailfishNumber) -> str:
    """
    convert snailfish number back to raw string
    for debug
    """

    as_string = ""
    for o, c, v in zip(number.open, number.close, number.values):

        if as_string and as_string[-1].isnumeric() and c == 0:
            as_string += ","
        as_string += "]" * c
        if c > 0:
            as_string += ","
        as_string += "[" * o
        as_string += str(v)

    final = sum(number.open) - sum(number.close)
    as_string += "]" * final
    return as_string


def add_snailfish_numbers(num_1: SnailfishNumber,
                          num_2: SnailfishNumber) -> SnailfishNumber:
    """
    add together two snailfish numbers
    """

    new_number = SnailfishNumber([], [], [])
    new_number.open = num_1.open + num_2.open
    new_number.open[0] += 1
    new_number.close = num_1.close + num_2.close
    new_number.close[len(num_1.close)] += sum(num_1.open) - sum(num_1.close)
    new_number.values = num_1.values + num_2.values
    return new_number


def reduce_snailfish_number(number: SnailfishNumber,
                            debug: bool = False) -> SnailfishNumber:
    """
    reduce Snailfish  number using split and explode
    operations
    """

    i = j = 0
    if debug:
        print(f"Reducing snailfish number: {convert_snailfish_to_raw(number)}")
    while i < len(number.values) or j < len(number.values):
        if i < len(number.values):
            cumulative_open = sum(number.open[:i + 1]) - sum(number.close[:i + 1])
            if cumulative_open == 5:
                # need to do an EXPLODE
                if i > 0:
                    number.values[i - 1] += number.values[i]
                if i + 2 < len(number.values):
                    number.values[i + 2] += number.values[i + 1]
                    number.close[i + 2] -= 1

                number.values[i] = 0
                number.open[i] -= 1
                del number.values[i + 1]
                del number.open[i + 1]
                del number.close[i + 1]

                if debug:
                    print(f"Explode at point {i}")
                    print(f"Number is now {convert_snailfish_to_raw(number)}")
                i = j = 0
            else:
                i += 1

        if i == len(number.values):
            if number.values[j] > 9:
                # need to do a SPLIT
                number.open[j] += 1
                val = number.values[j]
                number.values[j] = val // 2
                number.open.insert(j + 1, 0)
                number.close.insert(j + 1, 0)
                number.values.insert(j + 1, number.values[j] + (val % 2))
                if j + 2 < len(number.values):
                    number.close[j + 2] += 1
                if debug:
                    print(f"Split at point {j}")
                    print(f"Number is now {convert_snailfish_to_raw(number)}")
                i = j = 0
            else:
                # no operation required
                j += 1

    return number


def add_and_reduce_numbers(numbers: List[SnailfishNumber],
                           debug: bool = False) -> SnailfishNumber:
    """
    successively add and reduce our snailfish numbers
    """

    current = numbers[0]
    for number in numbers[1:]:
        current = add_snailfish_numbers(current, number)
        current = reduce_snailfish_number(current, debug)
    return current


def get_magnitude(number: Union[int, List]) -> int:
    """
    recursively calculate magnitude of the given
    list representation of our Snailfish number
    """

    if type(number) == list:
        x, y = number
        return 3 * get_magnitude(x) + 2 * get_magnitude(y)
    else:
        return number


def get_largest_sum(numbers: List[SnailfishNumber]) -> int:
    """
    return the largest achievable sum of any two
    numbers in our list
    """
    # TODO: can you do better than brute force?
    max_sum = 0
    for i, j in itertools.product(range(len(numbers)), range(len(numbers))):
        if i != j:
            candidates = [numbers[i], numbers[j]]
            reduced_sum = add_and_reduce_numbers(candidates)
            reduced_sum = ast.literal_eval(convert_snailfish_to_raw(reduced_sum))
            max_sum = max(max_sum, get_magnitude(reduced_sum))
    return max_sum


if __name__ == "__main__":

    with open("inputs/day18.txt") as input_file:
        data = input_file.readlines()
        data = [parse_snailfish_number(line) for line in data]

    answer = add_and_reduce_numbers(data)
    print(get_magnitude(ast.literal_eval(convert_snailfish_to_raw(answer))))
    print(get_largest_sum(data))
