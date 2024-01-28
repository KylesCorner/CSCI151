"""
Kyle Krstulich
3/14/23
countdown.py
"""

from sys import argv
from stdio import writeln


def count_down(n):
    if n == 0:
        writeln("Go!")
    else:
        writeln(n)
        count_down(n-1)


def main():
    start_number = int(argv[1])
    count_down(start_number)


if __name__ == "__main__":
    main()
