import datetime


def main():
    list_a = []
    list_b = list()
    ptime = datetime.datetime.now()
    print(type(list_a), type(list_b))
    list_c = [123, 3.14, "choi", True, ptime]
    print(list_c)
    print(f"list_c's second element is {list_c[1]}.")

    list_d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print(f"list_d[1][1] is {list_d[1][1]}.")
    for i in range(10):
        list_a.append(i * 2)
    list_a.pop(5)
    list_a.insert(5, 10.5)
    print(list_a)
    print(len(list_a))


if __name__ == "__main__":
    main()
