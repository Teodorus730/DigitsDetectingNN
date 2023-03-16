from digits import DIGITS
from fakes import FAKES


def in_data(a):
    for i in DIGITS:
        if a in DIGITS[i]:
            return i
    for i in FAKES:
        if i == a:
            return "FAKE"
    return "NEW"


if __name__ == "__main__":
    print(in_data([1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0]))
