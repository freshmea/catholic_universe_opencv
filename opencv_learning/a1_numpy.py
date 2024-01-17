import numpy


def show(m: str, o: numpy.ndarray):
    print("--" * 20)
    print(m, f"shape: {o.shape}, dtype: {o.dtype}")
    print("--" * 20)
    print(o)
    print("--" * 20)


def main():
    array1 = numpy.array([1, 2, 3], dtype=numpy.int8)
    show("array1", array1)


if __name__ == "__main__":
    main()
