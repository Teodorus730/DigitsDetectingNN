import numpy as np
from data.digits import DIGITS


np.random.seed(0)


def gen_new():
    k = [np.random.randint(0, 2) for _ in range(25)]
    while True:
        lal = True
        for i in DIGITS:
            if k in DIGITS[i]:
                lal = False
                k = [np.random.randint(0, 2) for _ in range(25)]
                break
        if lal:
            return k


def make_fake(n):
    out = []
    for z in range(n):
        k = gen_new()
        while k in out:
            k = gen_new()
        out.append(k)
        print(z)
    return out


if __name__ == "__main__":
    print(gen_new())
