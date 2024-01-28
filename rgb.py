"""
Kyle Krstulich
2023-03-27
CSCI151
rgb.py

Description
"""
import stdio
import stddraw
from color import Color
from sys import argv


# -------------------------------------------------------------------------------
# Private Functions
# -------------------------------------------------------------------------------


def __gather_input():
    """
    Returns command-line input. Else return false.
    """
    if len(argv) >= 4:
        return [int(arg) for arg in argv[1::]]
    else:
        return False

# -------------------------------------------------------------------------------
# Public Functions
# -------------------------------------------------------------------------------


def return_color(rgb: list) -> Color:

    return Color(rgb[0], rgb[1], rgb[2])


# -------------------------------------------------------------------------------
# Unit Tests
# -------------------------------------------------------------------------------

def main():
    user_in = __gather_input()
    colors = return_color(user_in)
    stdio.writeln(colors)


if __name__ == "__main__":
    main()
