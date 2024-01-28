"""
Kyle Krstulich
3/1/23
CSCI151
my_module.py

In class coding activity
"""

import math


def mean(a):
    return sum(a)/len(a)


def stddev(a):
    ave = mean(a)
    stddev = 0
    for i in a:
        stddev += (i - ave)**2

    stddev = stddev/len(a)
    return math.sqrt(stddev)


def main():
    import stdrandom

    random_list = [stdrandom.gaussian() for i in range(50)]
    print(stddev(random_list))
    pass


if __name__ == "__main__":
    main()
