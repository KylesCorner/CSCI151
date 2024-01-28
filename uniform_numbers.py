"""
Kyle Krstulich
1/19/23
uniform_numbers.py


Uniform random numbers. Compose a program that writes five uniform random
floats between 0.0 and 1.0, their average value, and their minimum and maximum
values. Use the built-in min() and max() functions.
"""
from random import random
from stdio import writeln




five_random_numbers = [random() for x in range(5)]

def average(in_list):
    return sum(in_list) / len(in_list)

writeln(f"\nRandom numbers; {five_random_numbers}")
writeln(f"Average Value: {average(five_random_numbers)}")
writeln(f"Minimum Value: {min(five_random_numbers)}")
writeln(f"Maximum Value: {max(five_random_numbers)}")
