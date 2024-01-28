
"""
Kyle Krstulich
1/30/23
CSCI 151
randomintseq.py

Takes two command-line arguments m and n and writes
n random integers between 0 and m-1.
"""

from stdio import writeln
from sys import argv
from random import randint


if len(argv) < 3:  # check for command line arguments. Exit on fail.
    writeln("python3 randomintseq.py LIMIT LENGTH")
    exit()


def random_integers(limit, length):
    """
    Writes random (length) random integers between 0 and (limit-1)
    """

    for x in range(length):
        writeln(randint(0, limit-1))


def main():
    """
    Main function
    """

    limit, length = int(argv[1]), int(argv[2])
    random_integers(limit, length)


if __name__ == "__main__":
    main()
