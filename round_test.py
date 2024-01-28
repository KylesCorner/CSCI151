"""
Kyle Krstulich
5/5/23
round_test.py

I believe that the round() function in python no only rounds the float/integer but stops calculation
from that point. To test this hypothesis I will implement the classic gamblers ruin problem again but
run the tests with varying degrees of precision.

COMMAND-LINE INPUT: python3 round_test.py STAKE GOAL PRECISION_DEPTH

"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from gambler import *
from sys import argv


def __gather_input() -> (int, int, int) or False:
    """
    Returns (stake, goal, number of trials). Else return false.
    """
    if len(argv) > 4:
        return map(int, argv[1::])
        # return int(argv[1]), int(argv[2]), int(argv[3], int(argv[4]))
    else:
        print("python3 gamber.py STAKE GOAL TRIALS PRECISION_DEPTH")
        exit()


def precision_test():
    """
    The precision_test function takes user input for stake, goal, and precision.
    It then calls the double_stake function with a trials parameter set to 100 
    and precision starting at 4 and increasing up to the user-specified precision.

    For each simulation, it extracts the stake, time, and number of wins data from
    the output of double_stake and creates a scatter plot of the time versus the
    stake. It then performs a linear regression on the log-transformed data and plots
    the fitted line on the scatter plot.

    Finally, it displays a table of the data and the scatter plot for each degree of precision.
    """
    stake, goal, trials, precision = __gather_input()
    answer = [double_stake(start_stake=stake, start_goal=goal,
                           trials=trials, precision=t) for t in range(4, precision+1)]
    marker = 4

    for sim in answer:
        lx, ly = [], []

        for item in sim[1::]:

            lx.append(item[-2])
            ly.append(item[-1])

        lx = np.array(lx)
        ly = np.array(ly)
        A = np.vstack([lx, np.ones(len(lx))]).T
        m, c = np.linalg.lstsq(A, ly, rcond=None)[0]
        x = np.linspace(0, 10000)

        table_output(sim)
        plt.plot(x, 2**c * x**m, linewidth=2,
                 label=f"{marker} degrees of precision")
        plt.xlabel("Stake")
        plt.ylabel("Time(Seconds)")
        plt.grid()
        plt.legend()

        marker += 1

    plt.show()


def single_test():
    stake, goal, trials, precision = __gather_input()
    answer = double_stake(stake, goal, precision=precision, trials=trials)
    fig, ax = plt.subplots()
    title = answer[0]
    data = answer[1::]
    lx, ly = [], []

    for item in data:
        lx.append(item[-2])
        ly.append(item[-1])

    data_frame = pd.DataFrame(np.array(data), columns=title)
    lx = np.array(lx)
    ly = np.array(ly)
    A = np.vstack([lx, np.ones(len(lx))]).T
    m, c = np.linalg.lstsq(A, ly, rcond=None)[0]
    x = np.linspace(0, 100000)

    plt.table(cellText=data_frame.values,
              colLabels=data_frame.columns,
              loc='top')
    plt.plot(x, 2**c * x**m, label=f"Estimated computation time", linewidth=4)
    plt.xlabel("Stake")
    plt.ylabel("Time(Seconds)")
    fig.tight_layout()
    plt.grid()
    plt.legend()


def main():
    single_test()
    plt.show()


if __name__ == '__main__':
    main()
