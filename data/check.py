from digits import DIGITS


def check():
    for i in DIGITS:
        temp = []
        for j in DIGITS[i]:
            if j in temp:
                return [i, j]
            temp.append(j)
    return None


def check1(l):
    for i in DIGITS:
        for j in DIGITS[i]:
            if j == l:
                return True
    return False


def drop_rep():
    out = {}
    for i in DIGITS:
        temp = []
        for j in DIGITS[i]:
            if j in temp:
                pass
            else:
                temp.append(j)
        out[i] = temp
    return out


if __name__ == "__main__":
    print(check())
    # kek = drop_rep()
    # for i in kek:
    #     print(f"'{i}': [")
    #     for j in kek[i]:
    #         print(j, ",", sep='')
    #     print("],")
