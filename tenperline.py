
"""
Kyle Krstulich
1/30/23
CSCI 151
tenperline.py

Reads a sequence of integers between 0 and 99 and writes 10 integers per line, with columns aligned.
"""

from stdio import writeln
from stdio import writef
from stdio import readAllInts


def integer_list():
    """
    Reads in a list of integers that are below 100 and returns them.
    """

    return [number for number in readAllInts() if 0 <= number < 100]


def format_output(integer_list):
    """
    Takes a list of integers and outputes them 10 per line with collumns aligned.
    """

    writeln()

    for index, number in enumerate(integer_list):

        writef("%3.0f", number)

        if (index + 1) % 10 == 0:
            writeln()

    writeln()


def main():
    """
    Main function
    """

    format_output(integer_list())


if __name__ == "__main__":
    main()
