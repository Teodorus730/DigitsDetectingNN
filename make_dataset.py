from data.fake import make_fake
from data.digits import DIGITS
from config import OUT_DIM, RANDOM_AMOUNT
from data_funcs import save_data
from data.fakes import FAKES


def make():
    real_inp = FAKES
    real_out = [[0]*OUT_DIM for _ in range(len(FAKES))]
    for i, o in zip(DIGITS, range(OUT_DIM)):
        print(o)
        for j in DIGITS[i]:
            real_inp.append(j)
            kek = [0]*OUT_DIM
            kek[o] = 1
            real_out.append(kek)

    fake_inp = []
    fake_out = []
    for i in make_fake(RANDOM_AMOUNT):
        fake_inp.append(i)
        fake_out.append([0]*OUT_DIM)

    return {"real": {"inp": real_inp, "out": real_out},
            "fake": {"inp": fake_inp, "out": fake_out}}


if __name__ == "__main__":
    save_data(make())
