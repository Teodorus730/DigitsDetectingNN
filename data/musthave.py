from itertools import chain


def main(a):
    n = cut(a)
    while n != a:
        a = n
        n = cut(a)

    a = []
    h = len(n)
    w = len(n[0])
    for i in range(5-h+1):
        temp = [[0]*w for _ in range(i)] + n + [[0]*w for _ in range(5-h-i)]
        for j in range(5-w+1):
            lal = [[0]*5 for _ in range(j)] + [list(z) for z in zip(*temp)] + [[0]*5 for _ in range(5-w-j)]
            a.append(list(chain(*[list(z) for z in zip(*lal)])))
            # a.append([list(z) for z in zip(*lal)])
    return a


def cut(a):
    b = [list(i) for i in zip(*a)]
    kek1 = len(b)
    kek2 = len(a)
    if a[0] == [0]*kek1:
        return a[1:]
    if a[-1] == [0]*kek1:
        return a[:-1]
    if b[0] == [0]*kek2:
        return [list(i) for i in zip(*b[1:])]
    if b[-1] == [0]*kek2:
        return [list(i) for i in zip(*b[:-1])]
    return a


def mem(a):
    lal = []
    for i in range(5):
        temp = []
        for j in range(5):
            temp.append(a[i*5+j])
        lal.append(temp)
    return lal

