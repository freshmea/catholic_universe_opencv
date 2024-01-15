def print_n_time(s1, s2, *s, n=5, abc=123, xyz=456, **kwargs):
    print(abc)
    print(xyz)
    if isinstance(n, int):
        print(s1)
        print(s2)
        for _ in range(n):
            for c in s:
                print(c, end=" ")
            print()
    else:
        pass
    for key, value in kwargs.items():
        print(f"{key} is {value}")


def main():
    print_n_time(
        "hello,", "world.", "this", "is", "a", "test", abc=789, bdf=245, ury=583
    )


if __name__ == "__main__":
    main()
