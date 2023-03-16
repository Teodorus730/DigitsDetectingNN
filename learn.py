import time
import numpy as np

from sigmoid import sigmoid
from config import *

from data_funcs import *

import warnings

# убрать runtime предупреждения
warnings.filterwarnings('ignore')

data = load_data()

np.random.seed(1)

# обучение с нуля
W1 = 2 * np.random.random((INP_DIM, HID_DIM)) - 1
W2 = 2 * np.random.random((HID_DIM, OUT_DIM)) - 1

# обучение с импортом весов из файла (обучение после обучения)
# kek = load_data("output.json")
# W1 = np.array(kek["w1"])
# W2 = np.array(kek["w2"])

all_time = time.time()

for j in range(GENERATIONS):
    ae = []
    last = time.time()
    for i in range(len(data["fake"]["inp"]) // RANDOM_SIZE):
        x = np.array(data["real"]["inp"] + data["fake"]["inp"][i*RANDOM_SIZE:(i+1)*RANDOM_SIZE])
        y = np.array(data["real"]["out"] + data["fake"]["out"][i*RANDOM_SIZE:(i+1)*RANDOM_SIZE])

        np.random.seed(j)
        np.random.shuffle(x)
        np.random.seed(j)
        np.random.shuffle(y)

        # Прямое расспространение
        h1 = sigmoid(np.dot(x, W1))
        h2 = sigmoid(np.dot(h1, W2))

        # Обратное распространение (back propagation)
        de_dh2 = y - h2
        de_dt2 = de_dh2 * sigmoid(h2, derivative=True)
        de_dh1 = np.dot(de_dt2, W2.T)
        de_dt1 = de_dh1 * sigmoid(h1, derivative=True)

        # Градинт ошибки
        de_dw2 = h1.T.dot(de_dt2)
        de_dw1 = x.T.dot(de_dt1)

        # Обновление обучаемых параметров (весов)
        W2 += de_dw2
        W1 += de_dw1
        lal = list(map(max, de_dh2))
        ae.append(sum(lal) / len(lal))

    print(j, sum(ae) / len(ae), time.time() - last)
    temp = {
        "w1": list(map(lambda e: list(e), W1)),
        "w2": list(map(lambda e: list(e), W2)),
    }
    save_data(temp, name="output.json")

print(time.time() - all_time)



