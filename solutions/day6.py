from typing import List


def get_total_number_of_fish(start_fish: List[int],
                             days: int) -> int:
    """
    get the total number of fish at the end of the period
    based on the initial timer for each fish
    """

    dp = [[0 for _ in range(9)] for _ in range(days + 1)]

    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if i == 0:
                dp[i][j] = 1
            elif j == 0:
                dp[i][j] = dp[i - 1][6] + dp[i - 1][8]
            else:
                dp[i][j] = dp[i - 1][j - 1]

    total = 0
    for n in start_fish:
        total += dp[-1][n]
    return total


if __name__ == "__main__":

    with open("inputs/day6.txt") as input_file:
        data = input_file.read()
        data = list(map(int, data.split(",")))

    print(get_total_number_of_fish(data, 80))
    print(get_total_number_of_fish(data, 256))
