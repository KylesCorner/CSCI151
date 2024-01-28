"""
Kyle Krstulich
2/8/23
CSCI151
banner.py


"""
import stddraw
from sys import argv

s = argv[1]

stddraw.setXscale(-1, 1)
stddraw.setYscale(-1, 1)
stddraw.setFontSize(30)
stddraw.setPenColor(stddraw.RED)


def move_text(text):

    DT = 10.0
    rx = -1
    vx = .01

    while True:

        if abs(rx + vx) > 1:
            rx = -1

        rx = rx + vx

        stddraw.clear()
        stddraw.text(rx, 0, text)
        stddraw.show(DT)


move_text(s)
