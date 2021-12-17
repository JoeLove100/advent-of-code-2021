from typing import List, Tuple


class Board:

    def __init__(self,
                 grid: List[List[int]]):

        self.entries = dict()
        self._populate_entries(grid)

        self.row_sums = [0 for _ in range(len(grid))]
        self.col_sums = [0 for _ in range(len(grid))]
        self.has_won = False

    def _populate_entries(self,
                          grid: List[List[int]]) -> None:

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.entries[grid[i][j]] = (i, j)

    def update(self,
              number: int) -> None:

        if number not in self.entries:
            return
        row, col = self.entries.pop(number)
        self.row_sums[row] += 1
        self.col_sums[col] += 1
        if self.row_sums[row] == len(self.row_sums):
            # full row
            self.has_won = True
        if self.col_sums[col] == len(self.col_sums):
            # full column
            self.has_won = True


def read_input(lines: List[str]) -> Tuple[List[int], List["Board"]]:

    numbers = lines[0].strip().split(",")
    numbers = [int(n) for n in numbers]

    boards = []
    grid = []
    for line in lines[2:]:
        if line == "" or line == " ":
            boards.append(Board(grid))
            grid = []
        else:
            row = [int(n) for n in line.strip().split(" ") if n != ""]
            grid.append(row)

    boards.append(Board(grid))
    return numbers, boards


def get_winning_score(numbers: List[int],
                      boards: List[Board]) -> int:
    """
    iterate over our boards until we find a winner,
    and return the related score
    """

    for n in numbers:
        for board in boards:
            board.update(n)
            if board.has_won:
                return sum(board.entries) * n

    raise ValueError(f"No winning board detected")


def get_final_winning_score(numbers: List[int],
                            boards: List[Board]) -> int:
    """
    iterate over the boards and get the score for the last
    board to win
    """

    valid_count = len(boards)
    is_valid = [True for _ in range(len(boards))]
    for n in numbers:
        for i, board in enumerate(boards):
            if not is_valid[i]:
                continue

            board.update(n)
            if board.has_won:
                valid_count -= 1
                is_valid[i] = False
                if valid_count == 0:
                    # last board
                    return sum(board.entries) * n

    raise ValueError("No final winning board detected")


if __name__ == "__main__":

    with open("inputs/day4.txt") as input_file:
        data = input_file.read()
        data = data.split("\n")

    all_numbers, all_boards = read_input(data)
    print(get_winning_score(all_numbers, all_boards))
    print(get_final_winning_score(all_numbers, all_boards))

