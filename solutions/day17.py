import math


def simulate(x_vel: int,
             y_vel: int,
             x_0: int,
             x_1: int,
             y_0: int,
             y_1: int) -> bool:
    """
    simulate a path starting with (x_vel, y_vel)
    and return true if it lands in the target zone
    defined by x_0, x_1, y_0, y_1 or false if it
    goes past this
    """

    x, y = 0, 0
    while True:
        x, y = x + x_vel, y + y_vel
        if x > x_1 or y < y_1:
            # irreversibly overshot - return false
            return False
        if x_0 <= x <= x_1 and y_1 <= y <= y_0:
            # in the zone - return true
            return True
        x_vel = max(0, x_vel - 1)
        y_vel = y_vel - 1


def get_valid_pair_count(x_0: int,
                         x_1: int,
                         y_0: int,
                         y_1: int) -> int:
    """
    get the count of velocity pairs (x, y) such
    that a projectile launched at velocity (x, y)
    will be in the zone defined by x_0, x_1, y_0, y_1
    at some time step
    """

    x_start = math.ceil(0.5 * (math.sqrt(1 + 8 * x_0)) -1)
    x_end = x_1 + 1
    y_start = y_1
    y_end = -y_1

    count = 0
    for i in range(x_start, x_end):
        for j in range(y_start, y_end):
            if simulate(i, j, x_0, x_1, y_0, y_1):
                count += 1
    return count


if __name__ == "__main__":

    # first bit doesn't really require any code
    x_0, x_1, y_0, y_1 = 94, 151, -103, -156
    print(get_valid_pair_count(x_0, x_1, y_0, y_1))
