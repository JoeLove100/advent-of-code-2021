import unittest
from solutions.day24 import parse_instruction, LogicUnit, Instruction


class TestDay24A(unittest.TestCase):

    def test_parse_instruction_inp(self):
        test_instr = "inp x"
        result = parse_instruction(test_instr)
        self.assertEqual(Instruction("inp", "x", None, None), result)

    def test_parse_instruction_value(self):
        test_instr = "add y -1"
        result = parse_instruction(test_instr)
        self.assertEqual(Instruction("add", "y", None, -1), result)

    def test_parse_instruction_variable(self):
        test_instr = "eql x y"
        result = parse_instruction(test_instr)
        self.assertEqual(Instruction("eql", "x", "y", None), result)

    def test_process_instructions(self):
        alu = LogicUnit(digits=[8, 3])
        test_instructions = [Instruction("inp", "w", None, 8),
                             Instruction("div", "w", None, 4),
                             Instruction("add", "z", "w", None),
                             Instruction("add", "y", "w", None),
                             Instruction("inp", "x", None, 3),
                             Instruction("mod", "x", None, 2)]
        alu.process_instructions(test_instructions)
        expected_result = {"w": 2, "x": 1, "y": 2, "z": 2}
        self.assertDictEqual(expected_result, alu._variables)
