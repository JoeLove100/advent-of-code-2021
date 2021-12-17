from typing import Tuple, List
from functools import reduce


def get_packet_value_from_subvalues(version: int,
                                    sub_values: List[int]) -> int:
    """
    apply the required function to the sub values
    to get our operator packet value based on its version
    """

    if version == 0:
        # sum packet
        value = sum(sub_values)
    elif version == 1:
        # product packet
        value = reduce(lambda x, y: x * y, sub_values)
    elif version == 2:
        # min packet
        value = min(sub_values)
    elif version == 3:
        # max packet
        value = max(sub_values)
    elif version == 5:
        # greater than packet
        assert len(sub_values) == 2
        value = 1 if sub_values[0] > sub_values[1] else 0
    elif version == 6:
        # less than packet
        assert len(sub_values) == 2
        value = 1 if sub_values[1] > sub_values[0] else 0
    elif version == 7:
        # equals packet
        assert len(sub_values) == 2
        value = 1 if sub_values[0] == sub_values[1] else 0
    else:
        # something has gone wrong
        raise ValueError(f"Packet version {version} is not recognized!")
    return value


def parse_packet_literal(packet: str,
                         pos: int) -> Tuple[int, int]:
    """
    parse a packet with type id 4 by processing
    each 5-character block til we hit the end
    """

    parsed_binary = ""

    while True:
        is_last_digit = packet[pos] == "0"
        parsed_binary += packet[pos + 1: pos + 5]
        pos += 5
        if is_last_digit:
            break

    return int(parsed_binary, 2), pos


def parse_packet_operator(packet: str,
                          pos: int,
                          type_id: int) -> Tuple[int, int, int]:
    """
    parse packet with operator type
    """
    version_sum = 0
    sub_values = []
    if packet[pos] == "0":
        total_length = int(packet[pos + 1: pos + 16], 2)
        pos += 16
        final_position = pos + total_length
        while pos < final_position:
            v, pos, ve = parse_packet(packet, pos)
            version_sum += ve
            sub_values.append(v)
    else:
        total_packets = int(packet[pos + 1: pos + 12], 2)
        pos += 12
        for _ in range(total_packets):
            v, pos, ve = parse_packet(packet, pos)
            version_sum += ve
            sub_values.append(v)

    value = get_packet_value_from_subvalues(type_id, sub_values)
    return value, pos, version_sum


def parse_packet(packet: str,
                 pos: int) -> Tuple[int, int, int]:
    """
    parse packet to integer based on
    the convoluted rules given in the
    problem statement
    """

    version = int(packet[pos: pos + 3], 2)
    type_id = int(packet[pos + 3: pos + 6], 2)

    if type_id == 4:
        # literal packet
        value, pos = parse_packet_literal(packet, pos + 6)
        return value, pos, version
    else:
        # operator packet
        value, pos, version_sum = parse_packet_operator(packet, pos + 6, type_id)
        return value, pos, version + version_sum


def hex_to_binary(hexadecimal: str) -> str:
    """
    stolen from Aaron Hall's answer
    on stack overflow question 1425493
    """

    out = ""
    for c in hexadecimal:
        numeric = int(c, 16)
        as_binary = format(numeric, "04b")
        out += as_binary
    return out


if __name__ == "__main__":

    with open("inputs/day16.txt") as input_file:
        data = input_file.read()

    data_binary = hex_to_binary(data)
    value, _, v_sum = parse_packet(data_binary, 0)
    print(f"Version sum is {v_sum}")
    print(f"Final value is {value}")
