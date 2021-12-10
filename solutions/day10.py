from typing import List, Optional


def get_illegal_character(line: str) -> Optional[str]:
    """
    return the first illegal character encountered, or
    None if there is not one
    """

    open_close_map = {")": "(", "]": "[", "}": "{", ">": "<"}
    stack = []
    for b in line:
        if b in open_close_map.values():
            # is an opening bracket
            stack.append(b)
        else:
            # is a closing bracket
            required_bracket = open_close_map[b]
            if stack and stack[-1] == required_bracket:
                stack.pop()
            else:
                return b

    return None


def get_illegal_bracket_score(illegal_brackets: List[str]):
    """
    get the total score for the list of illegal brackets
    """

    score_map = {")": 3, "]": 57, "}": 1197, ">": 25137}
    total_score = 0
    for b in illegal_brackets:
        if b is None:
            continue
        total_score += score_map[b]
    return total_score


def get_completion_brackets(line: str) -> List[str]:
    """
    get list of brackets to complete a valid but incomplete
    line, or return an empty list if invalid
    """

    open_close_map = {")": "(", "]": "[", "}": "{", ">": "<"}
    close_open_map = {v: k for k, v in open_close_map.items()}
    stack = []
    for b in line:
        if b in open_close_map.values():
            # is an opening bracket
            stack.append(b)
        else:
            # is a closing bracket
            required_bracket = open_close_map[b]
            if stack and stack[-1] == required_bracket:
                stack.pop()
            else:
                return []

    return [close_open_map[b] for b in reversed(stack)]


def get_completion_string_score(completion_string: List[str]) -> int:
    """
    calculate the score for our completion string
    """

    total = 0
    score_map = {")": 1, "]": 2, "}": 3, ">": 4}
    for b in completion_string:
        total = 5 * total + score_map[b]
    return total


if __name__ == "__main__":

    with open("inputs/day10.txt") as input_file:
        data = input_file.read()
        data = data.split("\n")

    brackets = [get_illegal_character(line) for line in data]
    print(get_illegal_bracket_score(brackets))

    completion_strings = [get_completion_brackets(line) for line in data]
    all_completion_scores = [get_completion_string_score(c_string) for c_string in completion_strings]
    non_zero_scores = [score for score in all_completion_scores if score > 0]
    mid = len(non_zero_scores) // 2
    print(sorted(non_zero_scores)[mid])
