"""
Kyle Krstulich
3/15/23
CSCI151
towers.py

Towers of Hanoi

No discussion of recursion would be complete without the ancient Towers of
Hanoi problem. We have three poles and n discs that fit onto the poles. The
discs differ in size and are initially arranged on one of the poles, in order
from largest (disc n) at the bottom to smallest (disc 1) at the top. The task
is to move the stack of discs to another pole, while obeying the following
rules:

Move only one disc at a time.
Never place a disc on a smaller one.


Explanation:

The towerOfHanoi() function is a recursive algorithm that solves the classic
Tower of Hanoi puzzle for a given number of discs and a specified starting peg.

The function takes two arguments: n, the number of discs to be moved, and left,
a boolean value indicating whether the discs should be moved to the leftmost
peg (True) or the rightmost peg (False).

The function does not return any value and simply prints the sequence of moves
required to solve the puzzle.

Within the function, the base case is checked to see if n is less than or equal
to 0. If so, the function immediately returns None.

The recursive portion of the algorithm consists of calling towerOfHanoi() with
n-1 discs and the opposite starting peg, moving the top disc to the desired
peg, and then calling towerOfHanoi() with n-1 discs and the destination peg.

The sequence of moves required to solve the puzzle is printed to the console
using the writeln()
"""
from sys import argv
from stdio import writeln
import stddraw

DOWN_TIME = 1  # animation down time

# -------------------------------------------------------------------------------
# Private Functions
# -------------------------------------------------------------------------------


def __gather_input() -> int:
    """
    Gathers command-line arguments and returns them as integer. Else
    prompt user for command-line arguments.

    Returns:
        int: The integer value input by the user.
    """
    if len(argv) > 1 and argv[1].isdigit():
        return int(argv[1])
    else:
        writeln("Enter a command-line argument!")
        exit()


def __draw_bars(x: int = 0, y: int = 1, n: int = 3) -> None:
    """

    """
    line_length = 1

    stddraw.line(x, y, x+line_length, y)
    stddraw.line(x + (line_length/2), y, x + (line_length/2), y + line_length)
    stddraw.show(DOWN_TIME)

    n -= 1

    if n > 0:
        __draw_bars(x + line_length, y, n)


def __draw_discs(num_discs: int) -> None:
    """

    """
    for i in range(num_discs):
        i += 1
        writeln(i)
        stddraw.rectangle(0, 3/4 + (i/4), i/4, .25)
        stddraw.show(100)


def __move_disc(disc: int, left: bool) -> None:
    """

    """
    pass


# -------------------------------------------------------------------------------
# Public Functions
# -------------------------------------------------------------------------------


def towerOfHanoi(n: int, left: bool) -> None:
    """
    Recursively solves the Tower of Hanoi puzzle for a given number of discs.

    Args:
        n (int): The number of discs to be moved.
        left (bool): A boolean value indicating whether the discs should be
        moved to the leftmost peg (`True`) or the rightmost peg (`False`).

    Returns:
        None
    """

    if n <= 0:
        return None

    # Recursively move the top n-1 discs to the opposite peg
    towerOfHanoi(n-1, not left)

    # Move the top disc to the desired peg
    if left:
        writeln(f"{n} left")
    else:
        writeln(f"{n} right")

    # Recursively move the n-1 discs from the opposite peg to the destination
    # peg
    towerOfHanoi(n-1, not left)


def screen_loop():
    """

    """
    limit = __gather_input()

    # stddraw configuration
    stddraw.setXscale(0, 3)
    stddraw.setYscale(0, 3)

    while True:
        stddraw.show(DOWN_TIME)

# -------------------------------------------------------------------------------
# Unit Tests
# -------------------------------------------------------------------------------


def main():
    limit = __gather_input()
    stddraw.setXscale(0, 3)
    stddraw.setYscale(0, 3)
    __draw_bars()
    __draw_discs(limit)
    screen_loop()


if __name__ == "__main__":
    main()
