"""
Kyle Krstulich
04/24/2023
CSCI151
gambler.py


Assignment #14
Gambler

Problem Statement
See the implementation of gambler.py  .  How long will it take to compute the
chance of doubling 1 million dollars one dollar at a time?

Use the stopwatch  module to estimate how long your program runs.

stake - initial amount you start with

goal - the amount you want to end with (you will either lose it all or make
                                        your goal)

trials - the number of times you want to run the experiment - run the
experiment 100 times to get a more accurate estimate of the probability.

Do any empirical analysis using the doubling method.  Start with the stake =
500 and goal 1000 and continue to double until the stake = 1000000.
"""
from stdio import writeln
from sys import argv
from math import log
from time import time
from random import random

values = {
    "Stake,n": [],
    "Goal": [],
    "Tn": [],
    "Tn/T(n/2)": [],
    "log n": [],
    "log Tn": []
}
# -------------------------------------------------------------------------------
# Classes
# -------------------------------------------------------------------------------


class Stopwatch:

    # Construct self and start it running.
    def __init__(self):
        self._creationTime = time()  # Creation time

    # Return the elapsed time since creation of self, in seconds.
    def elapsedTime(self):
        return time() - self._creationTime


# -------------------------------------------------------------------------------
# Private Functions
# -------------------------------------------------------------------------------


def __gather_input() -> tuple:
    """
    Returns (stake, goal, number of trials). Else return false.
    """
    if len(argv) > 3:
        return int(argv[1]), int(argv[2]), int(argv[3])
    else:
        writeln(f"python3 gamber.py STAKE GOAL TRIALS")
        exit()

# -------------------------------------------------------------------------------
# Public Functions
# -------------------------------------------------------------------------------


def table_output(values: list):
    """
    Generates a formatted table of values.

    Args:
        values (list): A list of tuples where each nested list represents a row
            in the table.

    Example:
        >>> table_output([(1, 2, 3), (4, 5, 6)])
            |      |  Column 1       |  Column 2       |  Column 3
            |------|----------------|----------------|--------
            |      |  1             |  2             |  3
            |      |  4             |  5             |  6

    """
    length = len(values[0]) + 1
    format_str = "{:<15}" * length
    output_str = ""

    for item in values:
        output_str += format_str.format("", *item) + "\n"

    writeln(output_str)


def gambler(stake: int, goal: int) -> int:
    """
    This function simulates a gambler who starts with a certain amount of
    cash (stake) and a goal amount of cash. The gambler repeatedly bets on
    a fair coin toss, winning if it comes up heads and losing if it comes
    up tails. If the gambler reaches their goal or runs out of cash, the
    function stops and returns the number of times the gambler reached
    their goal.
    """
    wins = 0
    cash = stake

    while (cash > 0) and (cash < goal):

        if (random() < 0.5):
            cash += 1
        else:
            cash -= 1

        if cash == goal:
            wins += 1

    return wins

# -------------------------------------------------------------------------------
# Unit Tests
# -------------------------------------------------------------------------------


def double_stake(start_stake: int, start_goal: int, num_doubles: int = 4, precision: int = 5, trials: int = 100) -> list:
    """
    Calculate the time to simulate the Gambler's problem while doubling the
    number of trials at each iteration until reaching the itteration limit,
    num_doubles.
    """

    values = [("Stake", "Goal", "Trials", "Tn",
               "Tn/T(n/2)", "log(Stake)", "log(Tn)")]
    wins = 0
    goal, stake = start_goal, start_stake

    for d in range(num_doubles):
        watch = Stopwatch()
        for t in range(0, trials):
            wins += gambler(stake, goal)
        time = round(watch.elapsedTime(), precision)

        if d > 0:
            time2 = round(time / values[d][2], precision)

        else:
            time2 = 0

        log_stake = round(log(stake, 2), precision)
        log_time = round(log(time, 2), precision)

        values.append((stake, goal, trials, time, time2, log_stake, log_time))
        goal *= 2
        stake *= 2

    return values


def half_time():
    """
    Simulates the Gambler's Problem with varying number of trials.
    The trials are halved after each iteration.
    """
    stake, goal, max_trials = __gather_input()
    values = [("Trials", "Wins", "Time")]

    trials = max_trials
    while trials > 1:
        wins = 0

        watch = Stopwatch()
        for t in range(0, trials):
            wins += gambler(stake, goal)
        time = round(watch.elapsedTime(), 5)

        values.append((trials, wins, time))
        trials //= 2

    return values


def single_sim():
    """
    Runs a simulation of the gambler's ruin problem and outputs the results
    in a table. The user is prompted to input the initial stake, the goal
    amount, and the number of trials to be run. The function then runs the
    specified number of trials of the gambler's ruin problem with the given
    parameters, and outputs the results in a table showing the number of
    trials, number of wins, and the time taken to complete the simulation.
    """
    stake, goal, trials = __gather_input()
    wins = 0
    watch = Stopwatch()

    for t in range(0, trials):
        wins += gambler(stake, goal)
    time1 = watch.elapsedTime()

    values = [("Trials", "Wins", "Time")]
    values.append((trials, wins, time1))
    return values


def main():
    stake, goal, trials = __gather_input()
    table_output(double_stake(start_stake=stake,
                 start_goal=goal, trials=trials))
    pass


if __name__ == "__main__":
    main()
