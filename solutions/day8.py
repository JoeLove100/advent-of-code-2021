from typing import List, Dict
from collections import namedtuple


Display = namedtuple("Display", ["signals", "outputs"])


def read_input(lines: List[str]) -> List[Display]:
    """
    parse raw input to a list of display objects
    """

    displays = []
    for line in lines:
        signals, outputs = line.split("|")
        signals = signals.strip().split(" ")
        outputs = outputs.strip().split(" ")
        displays.append(Display(signals, outputs))

    return displays


def count_easy_integers(arr: List[Display]) -> int:
    """
    count the number of 1/4/7/8 appearing in the
    display outputs
    """

    count = 0
    for display in arr:
        for o in display.outputs:
            if len(o) in {2, 3, 4, 7}:
                count += 1
    return count


def map_letters(display: List[str]) -> Dict[str, str]:
    """
    get correct mapping for letters based on the
    10 display numbers
    """

    by_length = dict()
    for s in display:
        if len(s) in by_length:
            by_length[len(s)] += [s]
        else:
            by_length[len(s)] = [s]

    decode_map = {letter: None for letter in "abcdefg"}

    # 1) work out A based on 1 and 7
    one = set(by_length[2][0])
    seven = set(by_length[3][0])
    decode_map["a"] = next(iter(one ^ seven))

    # 2) get number of times letter each appears in length 5 codes
    n_appearances_fives = {letter: 0 for letter in "abcdefg"}
    for s in by_length[5]:
        for c in n_appearances_fives:
            if c in s:
                n_appearances_fives[c] += 1
    appears_once_in_fives = {c for c in n_appearances_fives if n_appearances_fives[c] == 1}
    appears_twice_in_fives = {c for c in n_appearances_fives if n_appearances_fives[c] == 2}

    # 3) get number of times each letter appears in length 6 codes
    n_appearances_sixes = {letter: 0 for letter in "abcdefg"}
    for s in by_length[6]:
        for c in n_appearances_sixes:
            if c in s:
                n_appearances_sixes[c] += 1
    appears_twice_in_sixes = {c for c in n_appearances_fives if n_appearances_sixes[c] == 2}

    # 4) once in 5s but not twice in 6s is B
    B = next(iter(appears_once_in_fives - appears_twice_in_sixes))
    decode_map["b"] = B

    # 5) other once in 5s must be E
    appears_once_in_fives.remove(B)
    decode_map["e"] = next(iter(appears_once_in_fives))

    # 6) twice in 5s but not twice in 6s is F
    F = next(iter(appears_twice_in_fives - appears_twice_in_sixes))
    decode_map["f"] = F

    # 7) as we have F, we can now work out C from 1
    one.remove(F)
    C = next(iter(one))
    decode_map["c"] = C

    # 8) now we can use 4 to work out D
    four = set(by_length[4][0])
    decode_map["d"] = next(iter(four ^ {B, C, F}))

    # 9) finally, last one remaining must be G
    decode_map["g"] = next(iter(set("abcdefg") - set(decode_map.values())))

    return decode_map


def get_decoded_numbers(decode_map: Dict[str, str]) -> Dict[str, int]:
    """
    map the original number encodings to their
    new decoded counterparts
    """

    originals = {"abcefg": 0,
                 "cf": 1,
                 "acdeg": 2,
                 "acdfg": 3,
                 "bcdf": 4,
                 "abdfg": 5,
                 "abdefg": 6,
                 "acf": 7,
                 "abcdefg": 8,
                 "abcdfg": 9}
    decoded = dict()
    for letters, number in originals.items():
        decoded_letters = map(lambda x: decode_map[x], letters)
        decoded["".join(sorted(decoded_letters))] = number
    return decoded


def decode_outputs(outputs: List[str],
                   decoded_numbers: Dict[str, int]) -> int:
    """
    decode the output strings to a number
    """

    number = 0
    for output in outputs:
        decoded_output = decoded_numbers["".join(sorted(output))]
        number = 10 * number + decoded_output
    return number


if __name__ == "__main__":

    with open("inputs/day8.txt") as input_file:
        data = input_file.read()
        data = data.split("\n")

    all_displays = read_input(data)
    print(count_easy_integers(all_displays))

    total = 0
    for display in all_displays:
        letter_mapping = map_letters(display.signals)
        number_decoding = get_decoded_numbers(letter_mapping)
        decoded_number = decode_outputs(display.outputs, number_decoding)
        total += decoded_number
    print(total)
