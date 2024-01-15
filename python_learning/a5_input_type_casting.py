def a5_function():
    print("this is a5_input_type_casting.py's function")


def main():
    input_var = str()
    while not input_var.isdigit():
        input_var = input("input a number: ")

    print(type(input_var), input_var)
    # print(input_var * 5)
    print(int(input_var) * 5)


if __name__ == "__main__":
    main()
