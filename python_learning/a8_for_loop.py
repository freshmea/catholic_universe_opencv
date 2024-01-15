def main():
    # for i in range(2, 10, 3):
    #     print(i)
    list_a = [321, 232, 123, 34, 133]
    for i, v in enumerate(list_a):
        print(f"index: {i}, value: {v}")
    # tuple
    tuple_a = (1, 2, 3)
    tuple_b = 1, 2, 3
    tuple_c = 1, 2
    tuple_d = (1,)
    # set
    set_a = {1, 2, 3}
    set_b = {1, 2, 3, 3, 3, 3, 3}
    # dictionary - key:value
    dict_a = {"name": "choi", "age": 20}
    print(dict_a["name"])
    print(dict_a["age"])


if __name__ == "__main__":
    main()
