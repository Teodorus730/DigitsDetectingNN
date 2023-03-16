from sigmoid import *
from data_funcs import load_data
from config import *


def predict(x, idk=False):
    data = load_data("output.json")
    W1 = np.array(data["w1"])
    W2 = np.array(data["w2"])

    h1 = sigmoid(np.dot(x, W1))
    h2 = sigmoid(np.dot(h1, W2))

    color = "green"

    if idk:
        a = []
        for i in range(OUT_DIM):
            if round(h2[i]) == 1:
                a.append(i)
        if len(a) > 1:
            return [30, color, ' '.join(map(str, a))]
        elif len(a) == 1:
            return [35, color, f"IT'S {a[0]}"]
        else:
            return [35, "red", "I DON'T KNOW"]
    else:
        m = max(h2)
        for i in range(OUT_DIM):
            if h2[i] == m:
                return [35, color, f"IT'S {i}"]

