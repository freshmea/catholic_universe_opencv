class MyObject:
    pass


def main():
    print(type("hello, world"))
    print(type(123))
    print(type(3.141592))
    print(type(True))
    myObject = MyObject()
    print(type(myObject))
    # type checking
    print(isinstance("hello, world", str))
    print(isinstance(123, int))
    print(isinstance(3.141592, int))
    # identify checking
    print(123 is 124)


if __name__ == "__main__":
    main()
