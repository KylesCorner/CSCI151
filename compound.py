"""
Kyle Krstulich
1/19/23
compound.py

Calculates continuously compund interest given the number of years, principal, and annual interest rate.
"""

import stdio
from sys import argv
from math import e

comp_interest_values = [float(argv[x]) for x in range(1,4)] #Number of years, Principal, annual interest rate

def cont_comp_interest():

    return round(comp_interest_values[1] * e ** (comp_interest_values[2]*comp_interest_values[0]), 2)

stdio.writeln(cont_comp_interest())
