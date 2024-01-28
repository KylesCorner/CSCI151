"""
Kyle Krstulich
2/5/23
checkerboard.py

Complete exercise 1.5.18 in the textbook.

Compose a program that takes an integer command-line argument n
and plots an n-by-n checkerboard with red and black squares. Color
the lower left square red.
"""
import stddraw
from sys import argv


def gather_cmd_input():
    """
    gathers command line input and outputs it as an integer. 
    """
    if len(argv) > 1:
        return int(argv[1])


def main():
    n = gather_cmd_input()
    spacing = 0.5

    for x in range(n):

        for y in range(n):

            if (y+x) % 2 == 0:
                stddraw.filledSquare(x, y, spacing)
            else:
                stddraw.filledSquare(x, y, spacing)
    stddraw.show()


if __name__ == "__main__":
    main()
