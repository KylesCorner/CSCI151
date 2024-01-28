"""
Kyle Krstulich
2/28/23
CSCI151
harmonic.py

2.1.24 Harmonic numbers. Create a program harmonic.py that defines three
functions harmonic(), harmonicSmall(), and harmonicLarge() for computing
the harmonic numbers. The harmonicSmall() function should just compute
the sum (as in PROGRAM 2.1.1), the harmonicLarge() function should use the
approximation Hn = loge(n) + γ + 1/(2n) – 1/(12n2) + 1/(120n4)
(the number γ = 0.577215664901532... is known as Euler’s constant), and the
harmonic() function should call harmonicSmall() for n < 100 and harmonicLarge()
otherwise.
"""

import math
from sys import argv
from stdio import writeln

# ------------------------------------------------------------------------------
# Private Functions
# ------------------------------------------------------------------------------


def __gather_input(index=1):
    if len(argv) > 1:
        return int(argv[index])
    else:
        writeln("Enter a number from the command line.")


# ------------------------------------------------------------------------------
# Public Functions
# ------------------------------------------------------------------------------


def harmonicSmall(n):
    """
    Computes and returns nth harmonic number
    """

    total = 0.0
    for i in range(1, n+1):
        total += 1.0/i

    return total


def harmonicLarge(n):
    """

    """
    EULER_CONST = 0.577215664901532
    Hn = math.log(n, math.e) + EULER_CONST + (1/(2*n)) - (1/(12*(n**2))) +\
        (1/(120*(n**4)))
    return Hn


def multiple_harmonics():
    """
    Goes through each command line argument and appends its harmonic number
    to a list. Returns the list.
    """
    harmonic_values = []
    for i in range(1, len(argv)):
        arg = __gather_input(i)

        if arg > 100:
            value = harmonicLarge(arg)
        else:
            value = harmonicSmall(arg)

        harmonic_values.append(value)

    return harmonic_values


def main():
    writeln(multiple_harmonics())


if __name__ == "__main__":
    main()
