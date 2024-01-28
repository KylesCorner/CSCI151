"""
Kyle Krstulich
2/28/23
CSCI151
birthday.py


1.4.36 Birthday problem. Suppose that people continue to enter an empty room
until a pair of people share a birthday. On average, how many people will have
to enter before there is a match? Run experiments to estimate the value of this
quantity. Assume birthdays to be uniform random integers between 0 and 364.
"""

import random
from sys import argv


def birtdays():
    """
    Runs simulations too see how many people it takes to have two people share
    a birthday. Returns the number of people in the party.
    """

    party_list = []
    num_simulations = 0
    new_person = random.randint(0, 364)

    while new_person not in party_list:

        party_list.append(new_person)
        new_person = random.randint(0, 364)
        num_simulations += 1

    return num_simulations


def average_birthdays(limit=10):
    """
    Runs the birthdays() simulation to the limit amount. Returns the average
    amount of people needed in a party ino roder for at least two people to
    share a birthday.
    """

    simulation_list = [birtdays() for x in range(limit)]
    return (sum(simulation_list) / limit)


def main():

    if len(argv) > 1:
        limit = int(argv[1])
    else:
        limit = 1000

    print(f"Average of {limit} simulations: {average_birthdays(limit)}")


if __name__ == "__main__":
    main()
