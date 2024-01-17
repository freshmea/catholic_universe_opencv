import numpy as np
from a1_numpy import show


def main():
    array1 = np.arange(1, 4, 1, dtype=np.int8)
    array2 = np.arange(1, 11, 0.1)
    array3 = np.linspace(1, 10, 10)
    array4 = np.linspace(1, 30, 50)
    show("array1", array1)
    show("array2", array2)
    show("array3", array3)
    show("array4", array4)


if __name__ == "__main__":
    main()
