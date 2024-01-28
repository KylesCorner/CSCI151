"""
Kyle Krstulich
2/8/23
bouncingball.py
CSCI150

draws a bouncing ball to standard draw

"""
import stddraw

RADIUS = .05
DT = 20.0

stddraw.setXscale(-1.0, 1.0)
stddraw.setYscale(-1.0, 1.0)

rx = .48
ry = .86
vx = .03
vy = .046

while True:

    if abs(rx + vx) + RADIUS > 1.0:
        vx = -vx
    if abs(ry + vy) + RADIUS > 1.0:
        vy = -vy

    rx = rx + vx
    ry = ry + vy

    stddraw.clear(stddraw.GRAY)
    stddraw.filledCircle(rx, ry, RADIUS)
    stddraw.show(DT)
