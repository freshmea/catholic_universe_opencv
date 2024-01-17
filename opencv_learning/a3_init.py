import numpy as np
from a1_numpy import show


def main():
    array1 = np.zeros((10, 12), dtype=np.int8)
    array2 = np.ones((10, 12), dtype=np.int8)
    array3 = np.full((10, 12), 125, dtype=np.int8)
    show("array1", array1)
    show("array2", array2)
    show("array3", array3)


if __name__ == "__main__":
    main()
