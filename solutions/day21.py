import itertools
from typing import Tuple, Dict


def play_game(start_1: int,
              start_2: int) -> Tuple[int, int, int]:
    """
    play a game til one player hits
    1000 and then return both scores
    """

    positions = [start_1, start_2]
    scores = [0, 0]
    points = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    turn = 0
    dice = 1
    roll_count = 0
    while max(scores) < 1000:
        positions[turn] += dice % 100
        positions[turn] += (dice + 1) % 100
        positions[turn] += (dice + 2) % 100
        positions[turn] = positions[turn] % 10
        scores[turn] += points[positions[turn]]
        dice = (dice + 3) % 100
        turn = int(not turn)
        roll_count += 3
    return scores[0], scores[1], roll_count


def get_total_wins(start_1: int,
                   start_2: int,
                   score_1: int,
                   score_2: int,
                   memo: Dict[Tuple[int, int, int, int], Tuple[int, int]]) -> Tuple[int, int]:
    """
    get the total number of universes that each player wins in
    based on the scores and starting positions
    """

    multiples = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
    points = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    if score_1 >= 21:
        return 1, 0
    elif score_2 >= 21:
        return 0, 1
    elif (start_1, start_2, score_1, score_2) not in memo:
        total_wins_1 = total_wins_2 = 0
        for i, j in itertools.product(range(3, 10), range(3, 10)):
            next_position_1 = (start_1 + i) % 10
            next_score_1 = score_1 + points[next_position_1]
            next_position_2 = (start_2 + j) % 10
            next_score_2 = score_2 + points[next_position_2]
            wins_1, wins_2 = get_total_wins(next_position_1,
                                            next_position_2,
                                            next_score_1,
                                            next_score_2,
                                            memo)
            total_wins_1 += wins_1 * multiples[i] * multiples[j]
            total_wins_2 += wins_2 * multiples[i] * multiples[j]
        memo[(start_1, start_2, score_1, score_2)] = [total_wins_1, total_wins_2]

    return memo[(start_1, start_2, score_1, score_2)]


if __name__ == "__main__":

    s_1, s_2, rc = play_game(3, 5)
    if s_1 > s_2:
        print(f"Player 1 wins with {s_1} vs {s_2} in {rc} rolls")
    else:
        print(f"Player 2 wins with {s_2} vs {s_1} in {rc} rolls")
    print(min(s_1, s_2) * rc)

    w_1, w_2 = get_total_wins(3, 5, 0, 0, dict())
    w_1 = w_1 // 27  # total over-counts by 27 as we consider all possible combinations for
                     # player 2's rolls even those these would not occur once player 1 wins
    print(f"Player 1 wins {w_1}")
    print(f"Player 2 wins {w_2}")
    print(max(w_1, w_2))
