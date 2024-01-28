"""
Kyle Krstulich
04/05/2023
CSCI151
rectangle.py


Rectangles
3.2.1. 3.2.2 and 3.2.3 in the textbook

Problem Statement

Consider the data-type implementation for (axis-aligned) rectangles shown
below, which represents each rectangle with the coordinates of its center point
and its width and height. Compose an API for this data type, and fill in the
code for perimeter(), intersects(), contains(), and  draw().

Note: Treat coincident lines as intersecting, so that, for example,
a.intersects(a) is True and a.contains(a) is True.


"""
from stdio import writeln
from sys import argv
from random import uniform
from color import Color
import stddraw


# -------------------------------------------------------------------------------
# Classes
# -------------------------------------------------------------------------------


class Point:
    #  point object stores a tuple with text, and a color
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self._point_text = f"({self.x:.2f}, {self.y:.2f})"
        self._point_color = Color(0, 0, 0)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    #  change the color of the point
    def set_color(self, color: Color):
        self._point_color = color

    # return point as tuple (x,y)
    def get(self) -> tuple:
        return (self.x, self.y)

    # draws the point with the coords to the screen
    def draw(self):
        stddraw.setPenRadius(.0075)
        stddraw.setPenColor(self._point_color)
        stddraw.point(self.x, self.y)
        stddraw.text(self.x-.05, self.y-.05, self._point_text)


class Rectangle:

    # Construct self with center (x, y), width w, and height h.
    def __init__(self, x: float, y: float,
                 w: float, h: float, color=Color(0, 0, 0)):
        self._pen_color = color
        self._x = x
        self._y = y
        self._width = w
        self._height = h
        self._x_mod = self._width/2
        self._y_mod = self._height/2
        self._vertex = [
            Point(self._x - self._x_mod, self._y - self._y_mod),
            Point(self._x + self._x_mod, self._y - self._y_mod),
            Point(self._x + self._x_mod, self._y + self._y_mod),
            Point(self._x - self._x_mod, self._y + self._y_mod)
        ]  # (bottom left, bottom right, top right, top left)
        self._drawing_coord = self._vertex[0].get()
        self._desc = f"{self._pen_color} Rectangle and "\
            f"{[point for point in self._vertex]}"

    # String constructer

    def __str__(self):
        return self._desc

    # change the color of the rectangle
    def set_color(self, color: Color):
        self._pen_color = color

    # returns the four points of the rectangle as a tuple
    def get_coords(self) -> [(float, float)]:
        return [point.get() for point in self._vertex]

    # returns the 4 points to the rectangle
    def get_point_obj(self):
        return self._vertex

    # returns a tuple of all the Rectangle data
    def get_data(self) -> tuple:
        return (self._x, self._y, self._width, self._height)

    # Return the area of self.
    def area(self) -> float:
        return self._width * self._height

    # Return the perimeter of self.
    def perimeter(self) -> float:
        return sum([self._width*2, self._height*2])

    def intersects(self, rectangle: object) -> bool:
        """
        Cond1. If A's left edge is to the right of the B's right edge, - then A
        is Totally to right Of B

        Cond2. If A's right edge is to the left of the B's left edge, - then A
        is Totally to left Of B

        Cond3. If A's top edge is below B's bottom edge, - then A is Totally
        below B

        Cond4. If A's bottom edge is above B's top edge, - then A is Totally
        above B

        Return True if self intersects other, and False otherwise.
        """

        rect1_bl, rect1_br, rect1_tr, rect1_tl = self.get_point_obj()
        rect2_bl, rect2_br, rect2_tr, rect2_tl = rectangle.get_point_obj()

        rect1_l = rect1_bl.x
        rect1_r = rect1_tr.x
        rect1_t = rect1_tr.y
        rect1_b = rect1_bl.y

        rect2_l = rect2_bl.x
        rect2_r = rect2_tr.x
        rect2_t = rect2_tr.y
        rect2_b = rect2_bl.y

        if rect1_l > rect2_r:
            return False
        elif rect1_r < rect2_l:
            return False
        elif rect1_t < rect2_b:
            return False
        elif rect1_b > rect2_t:
            return False
        else:
            return True

    def contains(self, rectangle: object) -> bool:
        """
        compairs the sides of two rectangles, computing whether rectangle 2 is
        outside rectangle 1

        Return True if rectangle 2(parameter) is completely inside of
        rectangle 1(self), and False otherwise.
        """
        rect1_bl, rect1_br, rect1_tr, rect1_tl = self.get_point_obj()
        rect2_bl, rect2_br, rect2_tr, rect2_tl = rectangle.get_point_obj()

        rect1_l = rect1_bl.x
        rect1_r = rect1_tr.x
        rect1_t = rect1_tr.y
        rect1_b = rect1_bl.y

        rect2_l = rect2_bl.x
        rect2_r = rect2_tr.x
        rect2_t = rect2_tr.y
        rect2_b = rect2_bl.y

        if rect1_b > rect2_b:
            return False
        elif rect1_t < rect2_t:
            return False
        elif rect1_l > rect2_l:
            return False
        elif rect1_r < rect2_r:
            return False
        else:
            return True

    # draws rectangle to the screen
    def draw(self):
        x, y = self._drawing_coord
        stddraw.setPenRadius(.003)
        stddraw.setPenColor(self._pen_color)
        stddraw.rectangle(x, y, self._width, self._height)

    # draws rectangle to the screen with points
    def draw_with_points(self):
        stddraw.setPenColor(self._pen_color)
        for point in self._vertex:
            point.draw()
        self.draw()


# -------------------------------------------------------------------------------
# Private Functions
# -------------------------------------------------------------------------------


def __gather_input() -> (int, int, float, float) or False:
    """
    Returns command-line input. Else default assignment params.
    (n,num_contains,low,high)
    """
    if len(argv) == 4:  # for assignment
        return (int(argv[1]), 1, float(argv[2]), float(argv[3]))

    elif len(argv) == 5:  # for fun
        return (int(argv[1]), int(argv[2]), float(argv[3]), float(argv[4]))

    else:
        return (10, 1, .2, .9)


def __get_avg(rectangle_array: [Rectangle]) -> (float, float):
    """
    Returns the average area and perimeter of a list of rectangles.
    """
    length = len(rectangle_array)
    avg_area = sum([rect.area() for rect in rectangle_array])/length
    avg_perimeter = sum([rect.perimeter() for rect in rectangle_array])/length
    return (avg_area, avg_perimeter)


def __output(data: (int, int, list, int, int)) -> None:
    """
    Given data (number of intersects, number of contains, rectangle_array,
                minimum contains, number of sims to meet minimum contains).
    Output data to command-line and stddraw.
    """

    #  data config
    intersects, contains, rectangle_array, contain_min, num_sims = data
    avg_area, avg_perimeter = __get_avg(rectangle_array)
    output_str = "\nrectangle.py by Kyle Krstulich\n"\
        f"Number of rectangles: {len(rectangle_array)}\n"\
        f"Intersects: {intersects}\nContains: {contains}\t"\
        "*Red contains green\n"\
        f"Contain minimum: {contain_min}\n"\
        f"Number of simulations needed to reach contain minimum: {num_sims}\n"\
        f"Average area of the rectangles: {avg_area}\n"\
        f"Average perameter for the rectangles: {avg_perimeter}\n"

    # Unit square graph
    stddraw.setPenRadius(.002)
    stddraw.line(0, 0, 0, 1)  # x axis
    stddraw.line(0, 0, 1, 0)  # y axis
    Point(0, 0).draw()
    for i in range(1, 6):
        i /= 5
        Point(i, 0).draw()  # x axis
        Point(0, i).draw()  # y axis

    #  command-line output
    writeln()
    writeln('-'*80)
    writeln(output_str)
    writeln('-'*80)
    writeln()

    #  stddraw output
    [rect.draw() for rect in rectangle_array]
    stddraw.show()


# -------------------------------------------------------------------------------
# Unit Tests
# -------------------------------------------------------------------------------


def main():
    """
    Assignment function
    """

    #  input
    n, contain_min, low, high = __gather_input()
    num_sims = 0

    def run_sim():
        rectangle_array = []
        contains = []
        intersects = 0

        for i in range(n):  # Rectangle array setup
            w, h = uniform(low, high), uniform(low, high)
            x_mod, y_mod = w/2, h/2  # keep rectangles within a unit square
            # x_mod, y_mod = 0, 0
            x, y = uniform(0+x_mod, 1-x_mod), uniform(0+y_mod, 1-y_mod)
            color = Color(0, 0, 255)
            rectangle_array.append(Rectangle(x, y, w, h, color))

        # intersect/contain loop
        for index, rect in enumerate(rectangle_array):

            """
            Instead of a step itteration I should implement an exclusion
            itteration. Currently this will only work if the contained
            rectangle is indexed after the container rectangle.

            For the intersects a step itteration works fine. However it could
            be computed with a list comprehension
            """
            for comp_rect in rectangle_array[index+1::]:  # For intersects
                if rect.intersects(comp_rect):
                    intersects += 1

            for comp_rect in rectangle_array:  # For contains
                if rect != comp_rect:
                    if rect.contains(comp_rect):
                        comp_rect.set_color(Color(0, 255, 0))
                        rect.set_color(Color(255, 0, 0))
                        contains.append(comp_rect)

        return (intersects, len(contains), rectangle_array)

    while True:
        intersects, contains, rectangle_array = run_sim()
        num_sims += 1
        if contains >= contain_min:
            break

    #  stddraw config
    stddraw.setXscale(-.2, 1.1)
    stddraw.setYscale(-.2, 1.1)
    stddraw.setCanvasSize(1200, 800)

    #  output
    __output((intersects, contains, rectangle_array, contain_min, num_sims))


if __name__ == "__main__":
    main()
