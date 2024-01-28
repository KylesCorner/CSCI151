
"""
Kyle Krstulich
1/25/23
CSCI 151
dice.py

When you input command line arguments this program calculates and outputs dice
rolls exact probabilty, empirical results, and the difference between them.
When ran without command line arguments this program runs a simulation trying
to find where the exact probabilty matches the empirical results.

I simulated rolling dice until the rolls matched toe exact probabilty. I put
the first 1,000 'perfect' rolls into an array and found the average, which were
around 1,250,000 rolls. From my results I conclude that in order for the empirical
results to match the exact probabilty you need to roll more than 100,000 times.
However you have a much higher chance past 1,000,000 rolls.

In order for the emperical results to match the exact probabilty then
N > 1,000,000.
"""

from stdio import writeln
from sys import argv
import stdarray
from random import randint


def Exact_Probability():
    """
    Returns a 1D array for the exact probabilities of rolling two dice.
    """

    probabilities = stdarray.create1D(13, 0.0)

    for i in range(1, 7):
        for j in range(1, 7):
            probabilities[i+j] += 1.0

    for k in range(2, 13):
        probabilities[k] /= 36.0

    return probabilities


def Dice_Roll_Probability(dice_throws, number_of_rolls=1):
    """
    Returns a 1D array for all the dice roll probabilities
    """

    if len(argv) >= 2:
        number_of_rolls = int(argv[1])

    probabilities = stdarray.create1D(13, 0.0)

    for die, rolls in enumerate(dice_throws):
        probabilities[die] = rolls / (number_of_rolls)

    return probabilities


def Difference(exact_probability, emperical_results):
    """
    Returns the difference between the exact_probability
    and the emperical_results
    """

    difference = stdarray.create1D(13, 0.0)

    for die, prob in enumerate(exact_probability):
        difference[die] = round(prob, 3) - round(emperical_results[die], 3)

    return difference


def Roll_Dice(number_of_rolls=1):
    """
    Returns a 1D array of all the dice rolls.
    """

    if len(argv) >= 2:
        number_of_rolls = int(argv[1])

    dice_sum = stdarray.create1D(13, 0)

    for x in range(number_of_rolls):
        dice = randint(1, 6) + randint(1, 6)
        dice_sum[dice] += 1

    return dice_sum


def Print_Exact_Results(exact_probability=Exact_Probability()):
    """
    Outputs the exact results of rolling two dice to the command line
    """

    writeln("\nExact results")
    writeln("-"*40)

    for roll, result in enumerate(exact_probability[2::]):
        writeln(f"Probability the sum of die is {roll+2}: {round(result,3)}")


def Print_Empirical_Results(emperical_results):
    """
    Outputs the empirical results of rolling two dice many times
    to the command line
    """

    writeln("\nEmperical results")
    writeln("-"*40)

    for roll, result in enumerate(emperical_results[2::]):
        writeln(f"Results the sum of die is {roll+2}: {round(result,3)}")


def Print_Difference(difference):
    """
    Outputs the difference between exact and empirical results
    to the command line
    """

    writeln("\nDifference")
    writeln("-"*40)

    for roll, result in enumerate(difference[2::]):
        writeln(f"Difference when sum is {roll+2}: {round(result,3)}")


def Equal_Exact_Empirical_Results(start_number=100, increment=100):
    """
    Returns the roll number where the exact probability matches the
    emperical results to the third degree, and its array
    """

    exact_probability = Exact_Probability()

    while True:

        dice_rolls = Roll_Dice(start_number)
        emperical_results = Dice_Roll_Probability(dice_rolls, start_number)

        number_of_zeros = 0
        for die, result in enumerate(emperical_results):
            if round(result, 3) == round(exact_probability[die], 3):
                number_of_zeros += 1

        if number_of_zeros == 13:
            return start_number, emperical_results
        else:
            start_number += increment


def Zero_Difference(start_number, increment):
    """
    Returns the roll number where the difference between the exact probability
    and the empirical results are zero to the third degree, and its array
    """

    exact_probability = Exact_Probability()

    while True:

        dice_rolls = Roll_Dice(start_number)
        emperical_results = Dice_Roll_Probability(dice_rolls, start_number)
        difference = Difference(exact_probability, emperical_results)

        number_of_zeros = 0
        for die, diff in enumerate(difference):
            if round(diff, 3) == 0.0:
                number_of_zeros += 1

        if number_of_zeros == 13:
            return start_number, difference
        else:
            start_number += increment


def Zero_Difference_Simulation(number_of_sims_passed=10, start_number=100,
                               increment=100):
    """
    This function does a set amount of simulations. where the results are the average
    amount of dice rolls it takes to reach a zero difference.
    """

    writeln(f"\nGathering {number_of_sims_passed} zero differences...\n")

    zero_differences_array = stdarray.create1D(number_of_sims_passed, 0)

    for x in range(len(zero_differences_array)):
        zero_difference = Zero_Difference(start_number, increment)
        zero_differences_array[x] = zero_difference[0]
        start_number = zero_difference[0]
        writeln(f"Found zero difference {x+1} at {zero_difference[0]}")

    writeln("\nCalculating average...\n")

    average_zero_difference = round(
        sum(zero_differences_array) / len(zero_differences_array))
    writeln(f"The average zero difference is: {average_zero_difference}")

    Print_Difference(zero_difference[1])

    writeln("\nPositive tests.")
    writeln("-" * 40)

    for diff in zero_differences_array:
        writeln(diff)


def Equal_Exact_Empirical_Results_Simulation(number_of_sims_passed=10,
                                             start_number=100, increment=100,
                                             verbose=True):
    """
    This function does a set a mount of simulations. Where the results are the
    average amount of dice rolls it takes to have the empirical results equal
    the exact probability.
    """
    writeln(
        f"\nGathering {number_of_sims_passed} equal exact empirical results...\n")

    equal_results_array = stdarray.create1D(number_of_sims_passed, 0)

    for x in range(len(equal_results_array)):
        equal_result = Equal_Exact_Empirical_Results(start_number)
        equal_results_array[x] = equal_result[0]
        start_number = equal_result[0]

        if verbose:
            writeln(f"Found equal result {x+1} at {equal_result[0]}")

    writeln("\nCalculating average...\n")
    average_equal_result = round(
        sum(equal_results_array) / len(equal_results_array))
    writeln(f"The average equal result is: {average_equal_result}")

    Print_Empirical_Results(equal_result[1])
    Print_Exact_Results()

    if verbose:
        writeln("\nPositive tests.")
        writeln("-" * 40)
        for result in equal_results_array:
            writeln(result)


def test():
    """
    This function runs when you give the program no command line arguments.  It
    runs a simulation where it gathers dice rolls that have an exact
    probability. I start at 100,000 because past testing concluded that getting
    a roll with exact probabilty that is below 100,000 is not likely.
    """

    Equal_Exact_Empirical_Results_Simulation(
        start_number=100000, increment=100, number_of_sims_passed=1000,
        verbose=False)


def main():
    """
    Main function. This function runs when you input variables from the
    command line.
    """
    exact_probability = Exact_Probability()
    emperical_results = Dice_Roll_Probability(Roll_Dice())
    difference = Difference(exact_probability, emperical_results)

    Print_Exact_Results(exact_probability)
    Print_Empirical_Results(emperical_results)
    Print_Difference(difference)


if __name__ == "__main__":

    if len(argv) >= 2:
        main()
    else:
        test()
