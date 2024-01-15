def main():
    # int a;
    # a = 10;
    a = 10
    b = 3.141592
    print(123456)
    print("hi my name is choi", end="ENDSTRING")
    print(3.141592)
    print("this is", "python", "class", sep="\t")

    print("variable a is =", a)
    print("variable a is {0:00}, b is {1:.2}".format(a, b))
    # f-string
    print(f"variable a is {a}, b is {b:.2}")


if __name__ == "__main__":
    main()
