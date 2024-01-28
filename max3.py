"""
Kyle Krstulich
2/13/23
CSCI151
max3.py

finds the max largest number from 3 standard input numbers
"""
from sys import argv


def max3():
    if len(argv) >= 3:
        list_of_ints = [int(number) for number in argv[1::]]
        return max(list_of_ints)
    else:
        return False


def odd():
    if len(argv) >= 3:
        list_of_ints = [int(number) for number in argv[1::]]

    test_case = [number for number in list_of_ints if number % 2 == 0]
    return test_case


def main():
    print(max3())
    print(odd())


if __name__ == "__main__":
    main()
