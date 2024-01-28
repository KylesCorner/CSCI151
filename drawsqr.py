"""
Kyle Krstulich
2/5/23
drawsqr.py


"""

import stddraw

stddraw.setCanvasSize(100, 100)
stddraw.setXscale(-1, 2)
stddraw.setYscale(-1, 2)

stddraw.setPenRadius(0.01)
stddraw.line(0.0, 0.0, 1.0, 0.0)
stddraw.line(1.0, 0.0, 1.0, 1.0)
stddraw.line(1.0, 1.0, 0.0, 1.0)
stddraw.line(0.0, 1.0, 0.0, 0.0)
stddraw.text(0.5, 0.5, "Hello World!")
stddraw.show()
