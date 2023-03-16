from digits import DIGITS
import math


def count():
    c = {}
    for i in DIGITS:
        c[i] = len(DIGITS[i])
    return c


if __name__ == "__main__":
    print(count())
    print(*count().values())
    print(sum(count().values()))
    print(math.lcm(*count().values()))
