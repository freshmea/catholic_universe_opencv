import numpy as np
from a1_numpy import show


def main():
    a = np.arange(20).reshape(4, 5)
    show("a", a)
    b = a
    c = a.view()
    print(id(a))
    print(id(b))
    print(id(c))

    print(c is a, c.flags.owndata)

    d = c.reshape(2, 10)
    show("d", d)
    show("a", a)
    s = a[:1:3]
    s[:] = -1
    show("a", a)
    e = a.copy()
    print(e is a)
    d[1, 2] = 2_000_000
    show("e", e)
    show("a", a)
    m = np.arange(1_000_000)
    n = m[:100].copy()
    del m
    show("n", n)


if __name__ == "__main__":
    main()
