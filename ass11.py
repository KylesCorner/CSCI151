"""
Kyle Krstulich
2023-03-28
CSCI151
ass11.py

Combines the three im.py files to act as one
"""
import im1
import im2
import im3
import stddraw
from sys import argv
from stdio import writeln
from picture import Picture

DOWN_TIME = 5

# -------------------------------------------------------------------------------
# Private Functions
# -------------------------------------------------------------------------------


def __gather_input():
    """
    Returns command-line input. Else return false.
    """
    if len(argv) > 1:
        return Picture(argv[1])
    else:
        writeln("Enter a path to a picture")
        exit()

# -------------------------------------------------------------------------------
# Public Functions
# -------------------------------------------------------------------------------


def screen_loop() -> None:

    picture = __gather_input()
    gray_array = im1.grayscale_conversion(__gather_input())
    rotated_image = im2.rotate_image(picture)
    red_pic = im3.change_picture_color("red", picture)
    green_pic = im3.change_picture_color("green", picture)
    blue_pic = im3.change_picture_color("blue", picture)
    pictures = [red_pic, green_pic, blue_pic]

    loop_limit = 20

    im1.graph_values(gray_array)
    for i in range(loop_limit):
        stddraw.show(DOWN_TIME)

    stddraw.clear()

    for i in range(loop_limit):
        stddraw.picture(rotated_image)
        rotated_image = im2.rotate_image(rotated_image)
        stddraw.show(DOWN_TIME)

    stddraw.clear()

    im3.display_pictures(pictures)
    for i in range(loop_limit):
        stddraw.show(DOWN_TIME)


# -------------------------------------------------------------------------------
# Unit Tests
# -------------------------------------------------------------------------------


def main():
    screen_loop()


if __name__ == "__main__":
    main()
