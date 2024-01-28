"""
Kyle Krstulich
2/5/23
drawtri.py


"""

import math
import stddraw

c = math.sqrt(3.0) / 2.0

stddraw.setPenRadius(0.01)
stddraw.line(0.0, 0.0, 1.0, 0.0)
stddraw.line(1.0, 0.0, 0.5, c)
stddraw.line(0.5, c, 0.0, 0.0)
stddraw.point(.5, c/3.0)
stddraw.text(0.5, 0.5, "Hello World!")
stddraw.show()
