from typing import List, Dict, Optional
from collections import namedtuple

Instruction = namedtuple("Instruction", ["type", "var_1", "var_2", "val"])


class LogicUnit:

    def __init__(self,
                 digits: List[int],
                 variables: Optional[Dict[str, int]] = None,
                 debug: bool = False):

        if variables is None:
            variables = {"w": 0, "x": 0, "y": 0, "z": 0}
        self._variables = variables
        self._digits = iter(digits)
        self._debug = debug

    def _process_instruction(self,
                             instr: Instruction) -> None:
        """
        process a single instruction based on the given
        instruction type
        """

        if instr.type == "inp":
            if not self._digits:
                raise ValueError("No more digits to input!")
            n = next(self._digits)
            msg = f"Writing {n} to {instr.var_1}"
            self._variables[instr.var_1] = n
        elif instr.type == "add":
            if instr.var_2:
                msg = f"Adding {instr.var_2} to {instr.var_1} and writing to {instr.var_1}"
                self._variables[instr.var_1] += self._variables[instr.var_2]
            else:
                msg = f"Adding {instr.val} to {instr.var_1} and writing to {instr.var_1}"
                self._variables[instr.var_1] += instr.val
        elif instr.type == "mul":
            if instr.var_2:
                msg = f"Multiplying {instr.var_1} and {instr.var_2} and writing to {instr.var_1}"
                self._variables[instr.var_1] *= self._variables[instr.var_2]
            else:
                msg = f"Multiplying {instr.var_1} and {instr.val} and writing to {instr.var_1}"
                self._variables[instr.var_1] *= instr.val
        elif instr.type == "div":
            if instr.var_2:
                msg = f"Dividing {instr.var_1} by {instr.var_2} and writing to {instr.var_1}"
                self._variables[instr.var_1] //= self._variables[instr.var_2]
            else:
                msg = f"Dividing {instr.var_1} by {instr.val} and writing to {instr.var_1}"
                self._variables[instr.var_1] //= instr.val
        elif instr.type == "mod":
            if instr.var_2:
                msg = f"Taking {instr.var_1} modulo {instr.var_2} and writing to {instr.var_1}"
                self._variables[instr.var_1] = self._variables[instr.var_1] % self._variables[instr.var_2]
            else:
                msg = f"Taking {instr.var_1} modulo {instr.val} and writing to {instr.var_1}"
                self._variables[instr.var_1] = self._variables[instr.var_1] % instr.val
        elif instr.type == "eql":
            if instr.var_2:
                msg = f"Checking if {instr.var_1} equals {instr.var_2} and writing to {instr.var_1}"
                self._variables[instr.var_1] = int(self._variables[instr.var_1] == self._variables[instr.var_2])
            else:
                msg = f"Checking if {instr.var_1} equals {instr.val} and writing to {instr.var_1}"
                self._variables[instr.var_1] = int(self._variables[instr.var_1] == instr.val)
        else:
            raise ValueError(f"Could not recognise instruction of type {instr.type}")

        if self._debug:
            print(msg)
            print(f"Variables are now : {self._variables}")

    def process_instructions(self,
                             instructions: List[Instruction]) -> None:
        """
        process a set of instructions sequentially
        """

        for instr in instructions:
            self._process_instruction(instr)

        # print(f"Processed instructions and variables are now {self._variables}")

    @property
    def is_valid(self):
        return self._variables["z"] == 0


def parse_instruction(line: str) -> Instruction:
    """
    parse a single input line to an instruction
    """

    def parse_int(m: str) -> int:
        if m[0] == "-":
            return -int(m[1:])
        else:
            return int(m)

    instr = line.split(" ")
    if len(instr) == 2:
        if instr[0] != "inp":
            raise ValueError(f"Instruction {line} only has one variable but is not an input instruction")
        return Instruction(instr[0], instr[1], None, None)
    else:
        if instr[-1].isnumeric() or instr[-1][1:].isnumeric():
            return Instruction(instr[0], instr[1], None, parse_int(instr[2]))
        else:
            return Instruction(instr[0], instr[1], instr[2], None)


if __name__ == "__main__":

    """
    the above code is helpful to verify the answers, but 
    I didn't use to get the correct numbers. You can see
    that the instructions for each digit are largely the same
    and you can work out a functional form based on the 
    digits. This then defines a series of rules on the digits 
    that you can use to work out allowable values, and then make
    each digit as high/low as possible
    
    BIGGEST: 99598963999971
    SMALLEST: 93151411711211
    """

    with open("inputs/day24.txt") as input_file:
        data = input_file.readlines()

    set_of_instructions = [parse_instruction(line.replace("\n", "")) for line in data]
    alu = LogicUnit(digits=[9, 3, 1, 5, 1, 4, 1, 1, 7, 1, 1, 2, 1, 1])
    alu.process_instructions(set_of_instructions)
    print(alu._variables["z"])
