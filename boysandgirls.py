
"""
Kyle Krstulich
1/25/23
CSCI 151
boysandgirls.py

This program runs a simulation. A couple wants to have a family with children
of both sexes. This program simulates, for a desired amount of trials, how many
kids they need to have so that they can have a family with boys and girls.
"""

from stdio import writeln
import stdarray as array
from random import choice
from sys import argv

number_of_sims = int(argv[1])
child_frequency_array = array.create1D(4, 0)
total_amount_of_children = 0


def new_birth():

    choices = ["Boy", "Girl"]  # Returns Boy or Girl randomly
    return choice(choices)


def Simulation():
    """
     Simulates a family having children till they have at least 1 of each sex.
     Simulates for as many times as stated from the command line
    """

    boys, girls = 0, 0
    global total_amount_of_children

    for x in range(number_of_sims):

        while True:

            child = new_birth()

            if child == "Boy":
                boys += 1
            else:
                girls += 1

            if boys > 0 and girls > 0:

                children = boys + girls

                if children > 4:
                    child_frequency_array[3] += 1
                else:
                    child_frequency_array[boys + girls - 2] += 1

                boys, girls = 0, 0
                total_amount_of_children += children
                break


def Average():

    # Computes and returns the average number of children

    return round(total_amount_of_children / number_of_sims)


def Output():

    # Formats the output

    writeln(f"Average number of children: {Average()}")
    writeln(f"Trials with 2 children: {child_frequency_array[0]}")
    writeln(f"Trials with 3 children: {child_frequency_array[1]}")
    writeln(f"Trials with 4 children: {child_frequency_array[2]}")
    writeln(f"Trials with 5 or more children: {child_frequency_array[3]}")


def main():

    # Main function. Runs simulation then outputs the results.

    Simulation()
    Output()


if __name__ == "__main__":
    main()
