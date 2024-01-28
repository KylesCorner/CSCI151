"""
Kyle Krstulich
04/05/2023
CSCI151
triangle.py

Description
"""
from stdio import writeln

# -------------------------------------------------------------------------------
# Classes
# -------------------------------------------------------------------------------


class Triangle:

    def __init__(self, side_1, side_2, side_3):
        self._side_1 = side_1
        self._side_2 = side_2
        self._side_3 = side_3

    def __str__(self):
        return f"Triangle with sides: {self._side_1}, {self._side_2},"\
            f" {self._side_3}"

    def perimeter(self):
        return sum([self._side_1, self._side_2, self._side_3])


# -------------------------------------------------------------------------------
# Unit Tests
# -------------------------------------------------------------------------------


def main():
    trianle = Triangle(2, 2, 2)
    writeln(trianle)
    writeln(trianle.perimeter())


if __name__ == "__main__":
    main()
