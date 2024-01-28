"""
Kyle Krstulich
1/19/23
three-sort.py

Three-sort. Compose a program that takes three integers from the command line
and writes them in ascending order. Use the built-in min() and max() functions.
"""
import stdio
import sys

three_ints_from_cmd = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])]

sorted_ints = []

for x in range(len(three_ints_from_cmd)):
    sorted_ints.append(max(three_ints_from_cmd))
    three_ints_from_cmd.remove(max(three_ints_from_cmd))

stdio.writeln(sorted_ints)

