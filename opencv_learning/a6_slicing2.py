import numpy as np
from a1_numpy import show


def main():
    a1 = np.fromfunction(lambda x, y, z: x + y + z, (2, 5, 4), dtype=int)
    a2 = a1[:, 1::2, :3] * 10

    a2[1, ...] = -1
    show("a1", a1)
    show("a2", a2)


if __name__ == "__main__":
    main()
