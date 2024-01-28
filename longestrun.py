
"""
Kyle Krstulich
1/30/23
CSCI 151
longestrun.py

Input a series of integers. Outputs the longest continuous run and its value.
"""

from stdio import writeln
from stdio import readAllInts


def input_integers():
    """
    Stores series of integers from command line into an array and returns the
    array.
    """

    return readAllInts()


def longest_run(int_list):
    """
    Takes an array of integers. Finds the largest consecutive run of integers.
    Puts that info into a tuple with the repeated number.
    """

    longest_run = 0
    current_run = 1
    comparison = 0
    longest_number = 0

    for number in int_list:

        if comparison == number:
            current_run += 1

            if current_run > longest_run:
                longest_run = current_run
                longest_number = number

        else:
            current_run = 1
            comparison = number

    return (longest_run, longest_number)


def format_output(longest_run, longest_number):
    """
    Takes the output from longest_run and outputs it to the command line.
    """

    writeln(f"Longest run: {longest_run:3d} consecutive {longest_number:2d}'s")


def main():
    """
    Reads in an array of integers from the command line. Outputs the longest
    consecutive run of integers and its value.
    """

    answer_tuple = longest_run(input_integers())
    format_output(answer_tuple[0], answer_tuple[1])


if __name__ == "__main__":
    main()
