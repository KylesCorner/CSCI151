"""
Kyle Krstulich
2/14/23
CSCI151
gaus.py


"""
from stdio import writeln
from stdarray import create1D
from sys import argv
import stddraw
import random
import math

# TODO Fix normal distribution function


class Screen():

    # -------------------------------------------------------------------------------
    # Screen object default values and settings
    # -------------------------------------------------------------------------------

    def __init__(self, input_array, screen_x=1, screen_y=1,
                 down_time=0, print_points=False):

        self.screen_x = screen_x
        self.screen_y = screen_y
        self.down_time = down_time
        self.point_array = create1D(length=20, value=())
        self.print_points = print_points
        self.input_array = input_array

        stddraw.clear(stddraw.GRAY)
        stddraw.setXscale(min=0, max=self.screen_x)
        stddraw.setYscale(min=0, max=self.screen_y)

    # -------------------------------------------------------------------------------
    # Private methods
    # -------------------------------------------------------------------------------

    def __generate_points(self):
        """
        Given the values of a normal distrobtion. Creates a
        list of tuples containing point coordinates.
        """

        for index, value in enumerate(self.input_array):
            self.point_array[index] = (index, value)

        writeln(f"Point array: {self.point_array}")

    # -------------------------------------------------------------------------------
    # Public methods
    # -------------------------------------------------------------------------------

    def flip_display(self):
        """
        Flips the screen and animates to the time of down_time.
        """

        stddraw.show(self.down_time)

    def plot_points(self):
        """
        With an array of points graph them to the screen. Supports
        animation. Sets the screen scale according to data.
        """

        self.__generate_points()

        stddraw.setXscale(min=-2, max=len(self.input_array)+2)
        stddraw.setYscale(min=min(self.input_array)-2,
                          max=max(self.input_array)+2)

        text_pos = (max(self.input_array)+2)/10

        for x, y in self.point_array:
            stddraw.point(x, y)

            if self.print_points:
                stddraw.text(x-1, y+text_pos,
                             f"({round(x,2)},{round(y,2)})")

            self.flip_display()

    def draw_lines(self):
        """
        Draws lines between all the points.
        """

        for index, point in enumerate(self.point_array[:len(self.point_array) - 1:]):
            x1, y1 = point[0], point[1]
            x2, y2 = self.point_array[index+1][0], self.point_array[index+1][1]
            stddraw.line(x1, y1, x2, y2)
            self.flip_display()

# -------------------------------------------------------------------------------
# Global functions
# -------------------------------------------------------------------------------


def gaussian():
    # This may be broken. Do more research.
    r = 0.0
    while (r >= 1.0) or (r == 0.0):
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(-1.0, 1.0)
        r = x*x + y*y
    return x * math.sqrt(-2.0 * math.log(r) / r)


def get_array():
    """
    If command line arguments are inputed then return a
    list of random floats to the limit of the argument.
    """

    if len(argv) > 1:
        array_limit = int(argv[1])
    else:
        writeln("Enter a number")
        exit()

    float_array = create1D(length=array_limit, value=0.0)

    for x in range(len(float_array)):
        float_array[x] = gaussian()

    return float_array


def normal_distribution(input_array):
    """
    Input an array of floats, tracks the numbers that follow
    a normal distribtion.
    """

    distribution_array = create1D(length=20, value=0)

    for index in range(20):

        low = index * 0.05
        high = (index + 1) * 0.05

        for value in input_array:

            if low <= value <= high:
                distribution_array[index] += 1

    writeln(f"distribtion array: {distribution_array}")

    return distribution_array


def display_loop():

    normal_dist_array = normal_distribution(get_array())

    io = Screen(input_array=normal_dist_array,
                down_time=50, print_points=False)
    io.plot_points()
    io.draw_lines()

    while True:

        io.flip_display()


if __name__ == "__main__":
    display_loop()
