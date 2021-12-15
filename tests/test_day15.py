import unittest
from solutions.day15 import Node, dijkstra, create_larger_array


class TestDay15A(unittest.TestCase):

    def test_node_less_than(self):
        node_1 = Node(5, (0, 0), 4, True)
        node_2 = Node(2, (1, 1), 4, True)
        self.assertTrue(node_2 < node_1)

    def test_node_greater_than(self):
        node_1 = Node(5, (0, 0), 4, True)
        node_2 = Node(2, (1, 1), 4, True)
        self.assertTrue(node_1 > node_2)

    def test_dijkstra_simple_path(self):
        test_arr = [[1, 2, 3], [6, 5, 4], [9, 7, 8]]
        result = dijkstra(test_arr, (0, 0), (2, 2))
        self.assertEqual(17, result)

    def test_dijkstra_harder_path(self):
        test_arr = [[1, 1, 1, 1, 9],
                    [9, 9, 9, 1, 9],
                    [9, 1, 1, 1, 9],
                    [9, 1, 9, 9, 9],
                    [9, 1, 1, 1, 2]]
        result = dijkstra(test_arr, (0, 0), (4, 4))
        self.assertEqual(13, result)


class TestDay15B(unittest.TestCase):

    def test_create_larger_array(self):
        test_arr = [[2, 4], [1, 9]]
        result = create_larger_array(test_arr, 3)
        expected_result = [[2, 4, 3, 5, 4, 6],
                           [1, 9, 2, 1, 3, 2],
                           [3, 5, 4, 6, 5, 7],
                           [2, 1, 3, 2, 4, 3],
                           [4, 6, 5, 7, 6, 8],
                           [3, 2, 4, 3, 5, 4]]
        self.assertSequenceEqual(expected_result, result)
