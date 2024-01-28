"""
Kyle Krstulich
2023-03-28
CSCI151
im3.py

3.1.6 Compose a program that takes the name of a picture file as a command-line
input, and creates three images:

one with only the red components
one with only the green components
and one with only the blue components
**You must use the booksite modules when possible.
"""
import stddraw
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

# -------------------------------------------------------------------------------
# Public Functions
# -------------------------------------------------------------------------------


def change_picture_color(color: str, picture: Picture) -> Picture:
    """
    Given the color string, red green or blue, and a picture. Return a picture
    with just the corrisponding RGB value.
    """

    pic_x, pic_y = __get_dimensions(picture)
    new_picture = Picture(pic_x, pic_y)

    for x in range(pic_x):

        for y in range(pic_y):

            current_color = picture.get(x, y)

            match color:
                case "red":
                    new_color = Color(current_color.getRed(), 0, 0)
                case "green":
                    new_color = Color(0, current_color.getGreen(), 0)
                case "blue":
                    new_color = Color(0, 0, current_color.getBlue())
                case _:
                    writeln("red, green, or blue")
                    exit()

            new_picture.set(x, y, new_color)

    return new_picture


def display_pictures(pictures: [Picture]) -> None:
    """
    Itterates through picture array and draws them in order. Sets the
    screen size accordingly.
    """

    # Dimension variables
    pic_x, pic_y = __get_dimensions(pictures[0])
    shift = pic_x/6

    # Drawing
    for pic in pictures:

        stddraw.picture(pic, x=shift,  y=pic_y/2)
        shift += pic_x/3


def screen_loop() -> None:

    picture = __gather_input()
    red_pic = change_picture_color("red", picture)
    green_pic = change_picture_color("green", picture)
    blue_pic = change_picture_color("blue", picture)

    pictures = [red_pic, green_pic, blue_pic]

    # Dimension variables
    num_pics = len(pictures)
    pic_x, pic_y = __get_dimensions(pictures[0])

    # Canvas config
    stddraw.setCanvasSize(w=pic_x * num_pics - 1, h=pic_y)
    stddraw.setXscale(0, pic_x)
    stddraw.setYscale(0, pic_y)

    display_pictures(pictures)

    while True:

        stddraw.show(DOWN_TIME)

    pass

# -------------------------------------------------------------------------------
# Unit Tests
# -------------------------------------------------------------------------------


def main():
    screen_loop()


if __name__ == "__main__":
    main()
