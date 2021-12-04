from typing import List, Tuple


def get_gamma_and_epsilon(numbers: List[str]) -> Tuple[int, int]:
    """
    get the gamma and epsilon (as decimals) from the
    given list of binary numbers
    """

    if not numbers:
        raise ValueError("At least one number must be provided")
    n = len(numbers[0])
    counts = [0 for _ in range(n)]
    for number in numbers:
        for i, digit in enumerate(number):
            counts[i] += int(digit)
    gamma = "0b" + "".join(["1" if counts[m] > (len(numbers) + 1) // 2
                            else "0" for m in range(n)])
    epsilon = "0b" + "".join(["0" if counts[m] > (len(numbers) + 1) // 2
                              else "1" for m in range(n)])
    return int(gamma, 2), int(epsilon, 2)


def get_life_support_rating(numbers: List[str],
                            most_common: bool) -> int:
    """
    get the life support rating based on either the
    most or least common bit in each position
    """

    prev = None
    i = 0
    valid = [True for _ in range(len(numbers))]
    valid_count = len(numbers)
    while i < len(numbers[0]):
        count = 0
        for j, n in enumerate(numbers):
            if not valid[j]:
                # skip invalid number
                continue
            elif valid_count == 1:
                # last valid number so return
                return int("0b" + n, 2)
            elif i == 0 or n[i - 1] == prev:
                # either first pass or number is valid
                count += int(n[i])
            else:
                # number is newly invalid
                valid[j] = False
                valid_count -= 1

        i += 1
        if most_common:
            prev = "1" if count >= (valid_count + 1) // 2 else "0"
        else:
            prev = "0" if count >= (valid_count + 1) // 2 else "1"

    if valid_count != 1:
        raise ValueError("Failed to find a solution")
    else:
        # one number left after final pass through
        last_valid_number = numbers[valid.index(True)]
        return int("0b" + last_valid_number, 2)


if __name__ == "__main__":

    with open("inputs/day3.txt") as input_file:
        data = input_file.read()
        data = data.split("\n")

    g, e = get_gamma_and_epsilon(data)
    print(g * e)
    gen_rating = get_life_support_rating(data, True)
    scrub_rating = get_life_support_rating(data, False)
    print(gen_rating * scrub_rating)