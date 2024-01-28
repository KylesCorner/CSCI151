"""
Kyle Krstulich
2023-03-27
CSCI151
im1.py

Problem Statement
3.1.4  Compose a program that takes the name of a grayscale picture file as a
command-line argument and uses stddraw to plot a histogram of the frequency of
occurrence of each of the 256 grayscale intensities.


"""
import stddraw
from stdarray import create1D
from color import Color
from stdio import writeln
from picture import Picture
from sys import argv

DOWN_TIME = 1  # animation downtime


# -------------------------------------------------------------------------------
# Private Functions
# -------------------------------------------------------------------------------


def __gather_input() -> Picture:
    """
    Returns picture from command-line input. Else return false.
    """

    if len(argv) > 1:
        return Picture(argv[1])
    else:
        writeln("Enter a path to a picture")
        exit()


def __get_dimensions(picture: Picture) -> (int, int):
    """
    Returns dimensions of picture as a tuple of ints
    """

    return (picture.width(), picture.height())


def __toGray(color: Color) -> Color:
    """
    Converts RGB color to grey. Returns converted color.
    """

    red = color.getRed()
    green = color.getGreen()
    blue = color.getBlue()
    y = int(round((.299 * red) + (.587 * green) + (.114 * blue)))

    return Color(y, y, y)


# -------------------------------------------------------------------------------
# Public Functions
# -------------------------------------------------------------------------------


def grayscale_conversion(picture: Picture) -> [int]:
    """
    Converts colored picture to greyscale. Returns array of greyscale
    intensities occurrences.
    """

    pic_x, pic_y = __get_dimensions(picture)
    gray_array = create1D(256, 0)

    for x in range(pic_x):

        for y in range(pic_y):

            current_color = picture.get(x, y)
            greyscaled_color = __toGray(current_color)
            gray_array[greyscaled_color.getBlue()] += 1
            picture.set(x, y, greyscaled_color)

    return gray_array


def graph_values(values: [int]) -> None:
    """
    Given an array of values, displays the values as a bar graph.
    """

    # Bar config
    bar_width = 3
    stddraw.setPenColor(stddraw.BLUE)

    # Canvas config
    bars_with_spaces = len(values)*bar_width*2
    stddraw.setCanvasSize(w=bars_with_spaces, h=300)
    stddraw.setXscale(0, bars_with_spaces)
    stddraw.setYscale(0, max(values)+10)

    # Drawing
    for index, val in enumerate(values):
        stddraw.filledRectangle(index*2*bar_width, 0, bar_width, val)
        stddraw.show(DOWN_TIME)


def screen_loop() -> None:
    """
    Show loop to keep screen alive
    """
    picture = __gather_input()
    gray_array = grayscale_conversion(picture)

    writeln(gray_array)
    graph_values(gray_array)

    while True:

        stddraw.show(DOWN_TIME)


# -------------------------------------------------------------------------------
# Unit Tests
# -------------------------------------------------------------------------------


def main():
    screen_loop()


if __name__ == "__main__":
    main()
