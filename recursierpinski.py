"""
Kyle Krstulich
3/14/23
CSCI151
recursierpinski.py

Explanation:

The sierpinski() function is responsible for recursively drawing a Sierpinski
triangle on the screen, using the specified parameters.

The function takes four parameters: limit, x, y, and side_length.

limit is an integer value that specifies the number of times the triangle
should be subdivided. This value is gathered from a command-line argument.

y is an optional float value that specifies the y coordinate of the triangles
left vertex. If no value is provided, the default value is 0.0.

x is an optional float value that specifies the x coordinate of the triangles
left vertex. If no value is provided, the default value is 0.0.

side_length is an optional float value that specifies the length of each side
of the triangle. If no value is provided, the default value is 1.0.

Within the function, the coordinates of the triangle's three vertices are
calculated based on the input parameters, using the formula for a Sierpinski
triangle.

The __triangle() function is then called with these calculated coordinates to
draw the triangle on the screen.

The limit and side_length values are then updated to prepare for the recursive
calls.

The function then recursively calls itself three times, each time passing in
the updated limit and side_length values, and a different set of x and y values
to specify the position of the triangle. This results in the original triangle
being subdivided into three smaller triangles, which are then themselves
recursively subdivided in the same way, until the specified limit is reached.
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
        writeln("Enter a command-line argument as an integer")
        exit()


def __triangle(x1: float, y1: float, side_length: float) -> None:
    """
    Draw a triangle on the screen using the given coordinates.

    Parameters:
    -----------
    x1: float
        The x-coordinate of the left vertex of the triangle.
    y1: float
        The y-coordinate of the left vertex of the triangle.
    x2: float
        The x-coordinate of the top vertex of the triangle.
    y2: float
        The y-coordinate of the top vertex of the triangle.
    x3: float
        The x-coordinate of the right vertex of the triangle.
    y3: float
        The y-coordinate of the right vertex of the triangle.

    Returns:
    --------
    None
    """
    x2, y2 = x1 + side_length / 2, y1 + side_length  # top vertex
    x3, y3 = x1 + side_length, y1  # right vertex

    triX = [x1, x2, x3]
    triY = [y1, y2, y3]

    stddraw.polygon(triX, triY)
    stddraw.show(DOWN_TIME)


# -------------------------------------------------------------------------------
# Public Functions
# -------------------------------------------------------------------------------


def sierpinski(limit: int, x: float = 0, y: float = 0,
               side_length: float = 1.0) -> None:
    """
    Recursively draws a Sierpinski triangle on the screen, using the specified
    parameters.

    Args:
        limit (int): The number of times the triangle should be subdivided.
        x (float, optional): The x-coordinate of the triangle's left vertex.
        Defaults to 0.
        y (float, optional): The y-coordinate of the triangle's left vertex.
        Defaults to 0.
        side_length (float, optional): The length of each side of the triangle.
        Defaults to 1.0.

    Returns:
        None.
    """

    __triangle(x, y, side_length)  # draws triangle

    limit -= 1  # decrement limit
    side_length /= 2  # subdivide triangle

    if limit > 0:
        sierpinski(limit, x, y, side_length)  # left triangle
        sierpinski(limit, x + side_length, y, side_length)  # right triangle
        sierpinski(limit, x + (side_length / 2), y +
                   side_length, side_length)  # top triangle


def screen_loop() -> None:
    """
    Displays a Sierpinski triangle on the screen and enters an infinite loop
    that updates the display with a certain delay.

    Returns:
        None.
    """

    # stddraw configuration
    stddraw.setPenRadius(.001)
    stddraw.setXscale(0, 1)
    stddraw.setYscale(0, 1)

    limit = __gather_input()  # recursion limit
    sierpinski(limit)  # initialize recursion on point (0,0)

    while True:  # keeps screen alive

        stddraw.show(DOWN_TIME)


# -------------------------------------------------------------------------------
# Unit Tests
# -------------------------------------------------------------------------------


def main():
    screen_loop()


def loop_test(loops):

    stddraw.setPenRadius(.001)
    stddraw.setXscale(0, 1)
    stddraw.setYscale(0, 1)

    for i in range(loops):
        sierpinski(i)
        stddraw.clear()

    sierpinski(loops)

    while True:
        stddraw.show(DOWN_TIME)


if __name__ == "__main__":
    if len(argv) > 1:
        main()
    else:
        loop_test(8)
