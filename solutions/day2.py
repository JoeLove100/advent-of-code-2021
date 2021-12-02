from typing import List, Optional


class Submarine:

    def __init__(self,
                 start_x: int = 0,
                 start_y: int = 0,
                 start_aim: int = 0,
                 use_aim: bool = False) -> None:

        self.x = start_x
        self.y = start_y
        self.aim = start_aim
        self._use_aim = use_aim

    def move(self,
             instructions: List[str]) -> None:
        """
        update the submarine's x and y coordinates
        based on the given instructions
        """

        for instruction in instructions:
            d, m = instruction.split(" ")
            try:
                m = int(m)
            except TypeError:
                raise TypeError(f"Invalid instruction - magnitude was {m} ")

            if d == "forward":
                self.x += m
                if self._use_aim:
                    self.y += m * self.aim
            elif d == "up":
                if self._use_aim:
                    self.aim -= m
                else:
                    self.y -= m  # depth so other way round
            elif d == "down":
                if self._use_aim:
                    self.aim += m
                else:
                    self.y += m  # depth so other way round
            else:
                raise ValueError(f"Did not recognize direction: {d}")


if __name__ == "__main__":

    with open("inputs/day2.txt") as input_file:
        data = input_file.read()
        data = data.split("\n")

    sub_no_aim = Submarine()
    sub_no_aim.move(data)
    print(sub_no_aim.x * sub_no_aim.y)
    sub_with_aim = Submarine(use_aim=True)
    sub_with_aim.move(data)
    print(sub_with_aim.x * sub_with_aim.y)
