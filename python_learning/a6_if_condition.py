# import a3_type
# import a5_input_type_casting
import datetime


def main():
    # a5_input_type_casting.a5_function()
    # aa = a3_type.MyObject()
    # print(type(aa))
    ptime = datetime.datetime.now()
    print(ptime)

    print(int(str(ptime)[5:7]))
    print(ptime.month)

    if ptime.month < 3:
        print(f"this month is {ptime.month} and It's winter")
    elif ptime.month < 6:
        print(f"this month is {ptime.month} and It's spring")
    elif ptime.month < 9:
        print(f"this month is {ptime.month} and It's summer")
    elif ptime.month < 12:
        print(f"this month is {ptime.month} and It's fall")
    else:
        print(f"this month is {ptime.month} and It's winter")


if __name__ == "__main__":
    main()
