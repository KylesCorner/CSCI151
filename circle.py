"""
Kyle Krstulich
2/8/23
CSCI 151
circle.py


Problem Statement

Compose a program that takes as command-line arguments an integer n and a float
p (between 0 and 1),plots n equally spaced points of size on the circumference
of a circle, and then, with probability pfor each pair of points, draws a gray
line connecting them.

**You must use the booksite modules if possible (stdio, stddraw, stdarray)
"""
import stdio
from sys import argv
import math
import stddraw
import stdarray
import random

DT = 50  # Animation delay


def get_command_args():
    """
    Returns (n,p) if you enter command-line arguments.
    """

    if len(argv) >= 3:  # checking for command line arguments
        num_points = int(argv[1])
        point_prob = float(argv[2])

    else:
        stdio.writeln("Enter command-line arguments")
        exit()

    return (num_points, point_prob)


def init_background():
    """
    Sets scale and window parameters.
    """

    stddraw.setXscale(-1, 1)
    stddraw.setYscale(-1, 1)
    stddraw.clear(stddraw.LIGHT_GRAY)


def get_points(num_points):
    """
    Given the number of points this function plots a circle of points evenly
    distributed. Returns an array of points.
    """

    theta = 360/num_points
    point_array = stdarray.create1D(num_points, ())
    point_spacing = 0
    radius = .5

    for points_calculated in range(num_points):

        point_x = radius * math.cos(math.radians(point_spacing))
        point_y = radius * math.sin(math.radians(point_spacing))
        point_array[points_calculated] = (point_x, point_y)
        point_spacing += theta

    return point_array


def get_lines(point_array, point_prob):
    """
    Using an array of points and a probability. Calculates which pair of points
    a line can be drawn to. Returns an array of those point pairs.
    """

    line_array = []

    for index, point in enumerate(point_array):

        for second_point in point_array[index::]:
            comp_number = random.uniform(0.00, 1.00)

            if (second_point != point) and (comp_number <= point_prob):
                line_array.append((point, second_point))

    return line_array


def draw_points(point_list, point_color=stddraw.BLACK):
    """
    Using an array of points, plots out all the points with an animation.
    """

    stddraw.setPenColor(point_color)
    stddraw.setPenRadius(0.01)

    for point in point_list:
        x, y = point[0], point[1]
        stddraw.point(x, y)
        stddraw.show(DT)


def draw_lines(line_array, line_color=stddraw.DARK_GRAY):
    """
    Using an array of point pairs, draws lines between the pairs with
    an animation
    """

    stddraw.setPenColor(line_color)
    stddraw.setPenRadius(0.001)

    for line in line_array:
        x1, y1 = line[0][0], line[0][1]
        x2, y2 = line[1][0], line[1][1]
        stddraw.line(x1, y1, x2, y2)
        stddraw.show(DT)


def main():
    """
    With all given functions, plots points in a circle evenly spaced.
    Then draws lines between the points if it fits within the probability.
    Then does the same thing, but in reverse.
    """

    num_points, prob = get_command_args()
    points = get_points(num_points)
    lines = get_lines(points, prob)

    init_background()
    draw_points(points)
    draw_lines(lines)
    stddraw.show(DT*10)

    # reverse direction
    draw_points(points[::-1], point_color=stddraw.LIGHT_GRAY)
    draw_lines(lines[::-1], line_color=stddraw.LIGHT_GRAY)
    stddraw.show(DT)


if __name__ == "__main__":
    main()
