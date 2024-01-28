"""
Kyle Krstulich
1/19/23
usethree.py
"""
from sys import argv
import stdio


names = [argv[x] for x in range(1,len(argv))]

stdio.write(f"Hi, ")

for x in reversed(names):
    stdio.write(f"{x} ")

stdio.writeln()
