"""
Kyle Krstulich
04/05/2023
CSCI151
point.py

Description
"""
from stdio import writeln
from sys import argv

# -------------------------------------------------------------------------------
# Classes
# -------------------------------------------------------------------------------


class Point:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return f"Point at: ({self._x}, {self._y})"

    def distance(self, point: object):
        x, y = self.get_coord()
        x2, y2 = point.get_coord()

        distance = ((x2-x)**2 + (y2-y))**(1/2)
        return distance

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_coord(self):
        return (self._x, self._y)

# -------------------------------------------------------------------------------
# Private Functions
# -------------------------------------------------------------------------------


def __gather_input():
    """
    Returns command-line input. Else return false.
    """
    if len(argv) > 1:
        return argv[1]
    else:
        return False

# -------------------------------------------------------------------------------
# Public Functions
# -------------------------------------------------------------------------------


def pub_fn(self, arg):
    """
    """
    pass

# -------------------------------------------------------------------------------
# Unit Tests
# -------------------------------------------------------------------------------


def main():
    point1 = Point(1, 1)
    point2 = Point(4, 4)
    writeln(point1.distance(point2))
    writeln(point1)
    writeln(point2)


if __name__ == "__main__":
    main()
