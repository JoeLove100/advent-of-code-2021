from typing import Dict, List, Set, DefaultDict
from collections import defaultdict
from copy import copy


def read_input(lines: List[str]) -> Dict[str, List[str]]:
    """
    build adjacency map for the given input
    """

    adj_map = defaultdict(lambda: [])
    for line in lines:
        start, end = line.split("-")
        adj_map[start] += [end]
        adj_map[end] += [start]
    return adj_map


def count_paths_to_end(adj_map: Dict[str, List[str]],
                       current: str,
                       visited: Set[str]) -> int:
    """
    return number of valid paths to the
    final node
    """

    if current in visited:
        return 0
    if current == "end":
        return 1
    next_nodes = adj_map[current]
    total = 0
    for node in next_nodes:
        if current.islower():
            total += count_paths_to_end(adj_map, node, visited | {current})
        else:
            total += count_paths_to_end(adj_map, node, visited)
    return total


def count_paths_to_end_2(adj_map: Dict[str, List[str]],
                         current: str,
                         visit_counts: DefaultDict[str, int]) -> int:
    """
    return number of valid paths to the
    final node - here we can visit one small cave
    which is NOT the start/end twice
    """

    if current == "start" and "start" in visit_counts:
        # cannot revisit start, so not valid
        return 0
    if current in visit_counts and max(visit_counts.values()) == 2:
        # already visited a cave multiple times so not valid
        return 0
    if current == "end":
        # at the end so exactly one valid path
        return 1
    next_nodes = adj_map[current]
    total = 0
    for node in next_nodes:
        if current.islower():
            new_visit_count = copy(visit_counts)
            new_visit_count[current] += 1
            total += count_paths_to_end_2(adj_map, node, new_visit_count)
        else:
            total += count_paths_to_end_2(adj_map, node, visit_counts)
    return total


if __name__ == "__main__":
    with open("inputs/day12.txt") as input_file:
        data = input_file.read()
        data = data.split("\n")

    adjacency_map = read_input(data)
    print(count_paths_to_end(adjacency_map, "start", set()))
    print(count_paths_to_end_2(adjacency_map, "start", defaultdict(lambda: 0)))
