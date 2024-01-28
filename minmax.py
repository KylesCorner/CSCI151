"""
Kyle Krstulich
1/30/23
CSCI 151
minmax.py

From a list of integers, given by a standard input stream, output the min and max.
"""

from stdio import writeln
from stdio import readAllInts

def format_input():

    """
    Gathers the standard input stream into a list and returns it.
    """

    return [number for number in readAllInts()]


def find_min_max(integer_list):

    """
    Given an integer list returns a tuple for the min and max value in list.
    """

    return (min(integer_list), max(integer_list))


def format_output(min_max):

    """
    Given a tuple for min and max values. Outputs them to the command line.
    """

    writeln(f"Minimum Value: {min_max[0]}")
    writeln(f"Maximum Value: {min_max[1]}")


def main():

    """
    Main function
    """

    format_output(find_min_max(format_input()))


if __name__ == "__main__":
    main()
