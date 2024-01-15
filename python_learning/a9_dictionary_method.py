def main():
    dict_a = dict()
    dict_a["a"] = 100
    dict_a["b"] = 200
    dict_a["c"] = 300

    print(dict_a)

    # error raise
    # print(dict_a["d"])

    # get method
    print(dict_a.get("d"))

    for k in dict_a:
        print(k, dict_a[k])

    # item method
    for k, v in dict_a.items():
        print(k, v)


if __name__ == "__main__":
    main()
