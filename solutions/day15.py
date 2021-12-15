from typing import List, Tuple, Union
import math
import heapq
import itertools
from dataclasses import dataclass

Coordinate = Tuple[int, int]


@dataclass
class Node:

    distance: Union[int, float]
    coordinate: Coordinate
    risk_level: int
    valid: bool

    def __le__(self,
               other: "Node"):
        return self.distance < other.distance

    def __eq__(self,
               other: "Node"):
        return self.distance == other.distance

    def __gt__(self,
               other):
        return self.distance > other.distance


def get_neighbours(arr: List[List[int]],
                   current: Coordinate) -> List[Coordinate]:
    """
    get neigbouring nodes for our current
    coordinate
    """

    neighbours = []
    n, m = len(arr), len(arr[0])
    i, j = current
    if i > 0:
        neighbours.append((i - 1, j))
    if i < n - 1:
        neighbours.append((i + 1, j))
    if j > 0:
        neighbours.append((i, j - 1))
    if j < m - 1:
        neighbours.append((i, j + 1))
    return neighbours


def dijkstra(arr: List[List[int]],
             start: Coordinate,
             end: Coordinate) -> int:
    """
    implementation of Dijkstra's algorithm to
    get shortest path between start and end based
    on connections in our array
    """

    n, m = len(arr), len(arr[0])
    nodes = [Node(0, (i, j), arr[i][j], True) if (i, j) == start else Node(math.inf, (i, j), arr[i][j], True)
             for i, j in itertools.product(range(n), range(m))]
    heapq.heapify(nodes)
    nodes_by_coordinate = {node.coordinate: node for node in nodes}

    while nodes_by_coordinate:
        while not nodes[0].valid:
            # skip invalid nodes
            heapq.heappop(nodes)
        current = heapq.heappop(nodes)
        if current.coordinate == end:
            return current.distance
        nodes_by_coordinate.pop(current.coordinate)
        all_neighbours = get_neighbours(arr, current.coordinate)
        for neighbour in all_neighbours:
            if neighbour not in nodes_by_coordinate:
                continue
            neighbour_node = nodes_by_coordinate[neighbour]
            if current.distance + neighbour_node.risk_level < neighbour_node.distance:
                new_distance = current.distance + neighbour_node.risk_level
                new_node = Node(new_distance, neighbour, neighbour_node.risk_level, True)
                nodes_by_coordinate[neighbour].valid = False
                nodes_by_coordinate[neighbour] = new_node
                heapq.heappush(nodes, new_node)

    raise ValueError("Algorithm terminated without finding minimum path")


def create_larger_array(arr: List[List[int]],
                        k: int = 5) -> List[List[int]]:
    """
    TBC
    """

    n, m = len(arr), len(arr[0])
    large_arr = [[0 for _ in range(k * n)] for _ in range(k * m)]
    for i in range(k * n):
        for j in range(k * m):
            if i < n and j < m:
                large_arr[i][j] = arr[i][j]
            elif i < n:
                large_arr[i][j] = large_arr[i][j - m] + 1
            else:
                large_arr[i][j] = large_arr[i - n][j] + 1
            if large_arr[i][j] > 9:
                large_arr[i][j] = 1
    return large_arr


if __name__ == "__main__":

    with open("inputs/day15.txt") as input_file:
        data = input_file.readlines()
        data = [list(map(int, row.replace("\n", ""))) for row in data]

    # do for small array
    start_coordinate = (0, 0)
    end_coordinate = (len(data) - 1, len(data[0]) - 1)
    print(dijkstra(data, start_coordinate, end_coordinate))

    # now get large array and do it for that
    larger_array = create_larger_array(data)
    start_coordinate = (0, 0)
    end_coordinate = (len(larger_array) - 1, len(larger_array[0]) - 1)
    print(dijkstra(larger_array, start_coordinate, end_coordinate))
