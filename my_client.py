"""
Kyle Krstulich
3/1/23
CSCI151
my_client.py

In class coding activity
"""
import stdrandom
import my_module
from sys import argv
from stdio import writeln
import stdarray

if len(argv) > 1:
    test_num = int(argv[1])
else:
    test_num = 50

gaussian_array = stdarray.create1D(test_num, stdrandom.gaussian())

stddev = my_module.stddev(gaussian_array)
writeln(stddev)
