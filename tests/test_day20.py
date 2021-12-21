import unittest
from solutions.day20 import pad_image, decode_image


class TestDay20A(unittest.TestCase):

    def test_pad_image(self):
        test_img = [[".", "#", "."], ["#", ".", "#"], [".", "#", "."]]
        result = pad_image(test_img, 2)
        expected_result = [[".", ".", ".", ".", ".", ".", "."],
                           [".", ".", ".", ".", ".", ".", "."],
                           [".", ".", ".", "#", ".", ".", "."],
                           [".", ".", "#", ".", "#", ".", "."],
                           [".", ".", ".", "#", ".", ".", "."],
                           [".", ".", ".", ".", ".", ".", "."],
                           [".", ".", ".", ".", ".", ".", "."]]
        self.assertEqual(expected_result, result)

    def test_decode_image(self):
        test_img = [[".", "#", ".", "."],
                    ["#", ".", ".", "#"],
                    [".", ".", ".", "."],
                    [".", ".", "#", "."]]
        decode_string = {160: ".", 264: "#", 66: ".", 257: "#"}  # mock as dictionary
        result_img, result_count = decode_image(test_img, decode_string)
        expected_result = [[".", "#"], ["#", "."]]
        self.assertEqual(expected_result, result_img)
        self.assertEqual(2, result_count)