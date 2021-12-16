import unittest
from solutions.day16 import parse_packet, parse_packet_operator, parse_packet_literal, hex_to_binary, \
    get_packet_value_from_subvalues


class TestDay16A(unittest.TestCase):

    def test_hex_to_binary_no_leading_zero(self):
        test_hex = "D2FE28"
        result = hex_to_binary(test_hex)
        expected_result = "110100101111111000101000"
        self.assertEqual(expected_result, result)

    def test_hex_to_binary_leading_zero(self):
        test_hex = "38006F45291200"
        result = hex_to_binary(test_hex)
        expected_result = "00111000000000000110111101000101001010010001001000000000"
        self.assertEqual(expected_result, result)

    def test_parse_packet_literal(self):
        test_packet = "110100101111111000101000111"
        result_val, result_pos = parse_packet_literal(test_packet, 6)
        self.assertEqual(result_val, 2021)
        self.assertEqual(result_pos, 21)

    def test_parse_full_packet_if_literal(self):
        test_packet = "110100101111111000101000111"
        _, result_pos, result_version_sum = parse_packet(test_packet, 0)
        self.assertEqual(result_pos, 21)
        self.assertEqual(result_version_sum, 6)

    def test_parse_operator_packet(self):
        test_packet = "00111000000000000110111101000101001010010001001000000000"
        _, result_pos, result_version_sum = parse_packet_operator(test_packet, 6, 1)
        self.assertEqual(49, result_pos)
        self.assertEqual(8, result_version_sum)

    def test_parse_full_packet_if_operator(self):
        test_packet = "11101110000000001101010000001100100000100011000001100000"
        _, result_pos, result_version_sum = parse_packet(test_packet, 0)
        self.assertEqual(51, result_pos)
        self.assertEqual(14, result_version_sum)


class TestDay16B(unittest.TestCase):

    def test_packet_value_sum(self):
        test_sub_values = [1, 5, 2, 3]
        result = get_packet_value_from_subvalues(0, test_sub_values)
        self.assertEqual(11, result)

    def test_packet_value_product(self):
        test_sub_values = [1, 5, 2, 3]
        result = get_packet_value_from_subvalues(1, test_sub_values)
        self.assertEqual(30, result)

    def test_packet_value_min(self):
        test_sub_values = [1, 5, 2, 3]
        result = get_packet_value_from_subvalues(2, test_sub_values)
        self.assertEqual(1, result)

    def test_packet_value_max(self):
        test_sub_values = [1, 5, 2, 3]
        result = get_packet_value_from_subvalues(3, test_sub_values)
        self.assertEqual(5, result)

    def test_packet_value_greater_than(self):
        test_sub_values = [10, 2]
        result = get_packet_value_from_subvalues(5, test_sub_values)
        self.assertEqual(1, result)

    def test_packet_value_less_than(self):
        test_sub_values = [10, 2]
        result = get_packet_value_from_subvalues(6, test_sub_values)
        self.assertEqual(0, result)

    def test_packet_value_equal(self):
        test_sub_values = [5, 5]
        result = get_packet_value_from_subvalues(7, test_sub_values)
        self.assertEqual(1, result)
