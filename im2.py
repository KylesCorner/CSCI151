"""
Kyle Krstulich
2023-03-27
CSCI151
im2.py

3.1.5  Compose a program that takes the name of a picture file as a
command-line argument and flips the image horizontally.
"""
import stddraw
from stdio import writeln
from picture import Picture
from sys import argv

DOWN_TIME = 50  # animation downtime


# -------------------------------------------------------------------------------
# Private Functions
# -------------------------------------------------------------------------------


def __gather_input() -> Picture:
    """
    Returns command-line input. Else return false.
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


def __move_90(width: int, height: int,  x: int, y: int) -> (int, int):
    """
    Rotates the given pixel by 90 degrees.
    """
    x2 = -y + width
    y2 = x
    return (x2, y2)

# -------------------------------------------------------------------------------
# Public Functions
# -------------------------------------------------------------------------------


def rotate_image(picture: Picture, looping: bool = False) -> Picture:
    """
    Itterates through the picture rotates it and returns the rotated picture.
    """
    # Pictures
    picture_width, picture_height = __get_dimensions(picture)
    new_picture = Picture(picture_width, picture_height)

    for x in range(picture_width):

        for y in range(picture_height):

            nx, ny = __move_90(picture_width, picture_height, x, y)
            color_from_point = picture.get(x, y)

            new_picture.set(nx, ny, color_from_point)

    if not looping:
        picture_width, picture_height = __get_dimensions(new_picture)
        stddraw.setCanvasSize(w=picture_width, h=picture_height)

    return new_picture


def screen_loop() -> None:
    """
    Rotates the image 90 degrees, draws it to the screen, then loops to keep
    the screen alive
    """
    picture = __gather_input()
    new_picture = rotate_image(picture)

    stddraw.picture(new_picture)

    while True:

        stddraw.show(DOWN_TIME)


# -------------------------------------------------------------------------------
# Unit Tests
# -------------------------------------------------------------------------------

def spinning_picture():
    picture = __gather_input()
    new_picture = rotate_image(picture)

    while True:
        stddraw.picture(new_picture)

        new_picture = rotate_image(new_picture, looping=True)

        stddraw.show(DOWN_TIME)


def main():
    screen_loop()


if __name__ == "__main__":
    main()
