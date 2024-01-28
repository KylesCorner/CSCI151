"""
Kyle Krstulich
04/01/2023
CSCI151
picturefilter.py

3.1.33 Slide show. Compose a program that takes the names of several image
files as command-line arguments and displays them in a slide show (one every
                                                                two seconds),
using a fade effect to black and a fade from black between pictures.

3.1.35 Rotation filter. Compose a program that takes two command-line arguments
(the name of an image file and a real number theta) and rotates the image θ
degrees counterclockwise. To rotate, copy the color of each pixel (si, sj) in
the source image to a target pixel (ti, tj) whose coordinates are given by the
following formulas:

ti = (si – ci)cos θ – (sj – cj)sin θ + ci

tj = (si – ci)sin θ + (sj – cj)cos θ + cj

where (ci, cj) is the center of the image.

3.1.36 Swirl filter. Creating a swirl effect is similar to rotation, except
that the angle changes as a function of distance to the center. Use the same
formulas as in the previous exercise, but compute θ as a function of
(si, sj)—specifically, π / 256 times the distance to the center.

3.1.37 Wave filter. Compose a filter like those in the previous two exercises
that creates a wave effect, by copying the color of each pixel (si, s j) in the
source image to a target pixel (ti, t j),
where ti = si and tj = sj +20 sin(2 πsi/64).
Add code to take the amplitude (20 in the accompanying figure) and the
frequency (64 in the accompanying figure) as command-line arguments. Experiment
with various values of these parameters.

3.1.38 Glass filter. Compose a program that takes the name of an image file as
a command-line argument and applies a glass filter: set each pixel p to the
color of a random neighboring pixel (whose pixel coordinates are each within 5
pixels of p’s coordinates).
"""
from stdio import writeln
from random import randint
from sys import argv
from picture import Picture
import stddraw
import math

DOWN_TIME = 2000  # animation down time


# -------------------------------------------------------------------------------
# Private Functions
# -------------------------------------------------------------------------------


def __gather_input():
    """
    Returns a picture or a list of pictures depending on command-line argument.
    Exits when no picture path is provided.

    returns (command, [arguments], [pictures])

    This can be implemented better. I could parse the input gathering all the
    command flags(-) and expect a number of arguments after the command.
    """
    # command : number of arguments
    commands = {"-h": ["help menu"], "-S": ["slide show"],
                "-r": ["rotate image", "angle in radians"],
                "-s": ["swirl image", "swirl mod"],
                "-w": ["wave image", "amplitude", "frequency"],
                "-g": ["glass image"],
                "-a": ["all filters"]}
    argument = []
    pictures = []

    def help_menu():
        menu_str = '\n'
        for command, id in commands.items():
            desc = id[0]
            id = "\t".join(id[1::])
            menu_str += desc + "\t" + command + "\t" + id + "\tPICTURES\n"

        menu_str += "\nExample: \n\t>>> python3 picturefilter.py -w 45 36 mandrill.jpg" \
            " dog.jpg\n"

        writeln(menu_str)
        exit()

    if len(argv) < 3:
        help_menu()
    else:
        command = argv[1]

    if command not in commands:
        help_menu()

    match command:
        case "-h":
            help_menu()
        case "-S":
            writeln("Slide Show")
            pictures = [Picture(path) for path in argv[2::]]

        case "-r":
            if len(argv) < 4:
                help_menu()
            writeln("rotate picture")
            argument = [int(argv[2])]
            pictures = [Picture(path) for path in argv[3::]]

        case "-s":
            if len(argv) < 4:
                help_menu()
            writeln("swirl picture")
            argument = [int(argv[2])]
            pictures = [Picture(path) for path in argv[3::]]

        case "-w":
            if len(argv) < 5:
                help_menu()
            writeln("wave picture")
            argument = [int(argv[2]), int(argv[3])]
            pictures = [Picture(path) for path in argv[4::]]

        case "-g":
            if len(argv) < 2:
                help_menu()
            writeln("glass picture")
            pictures = [Picture(path) for path in argv[2::]]

        case "-a":
            if len(argv) < 2:
                help_menu()
            writeln("glass picture")
            pictures = [Picture(path) for path in argv[2::]]

        case _:
            help_menu()

    return (command, argument, pictures)


def __get_dimensions(picture: Picture) -> (int, int):
    """
    Returns dimensions of picture as a tuple of ints
    """

    return (picture.width(), picture.height())
# -------------------------------------------------------------------------------
# Public Functions
# -------------------------------------------------------------------------------


def rotation_filter(picture: Picture, theta: float) -> Picture:
    """

    ti = (si – ci)cos θ – (sj – cj)sin θ + ci

    tj = (si – ci)sin θ + (sj – cj)cos θ + cj

    where (ci, cj) is the center of the image.
    """
    pic_x, pic_y = __get_dimensions(picture)
    center_x, center_y = pic_x//2, pic_y//2
    new_picture = Picture(pic_x, pic_y)
    theta = math.radians(theta)

    for x in range(pic_x):

        for y in range(pic_y):
            nx = (x - center_x) * math.cos(theta) + (y - center_y) * \
                math.sin(theta) + center_x

            ny = -(x - center_x) * math.sin(theta) + (y - center_y) * \
                math.cos(theta) + center_y

            new_picture.set(int(nx), int(ny), picture.get(x, y))

    return new_picture


def swirl_filter(picture: Picture, swirl_mod: int) -> Picture:
    """
    compute θ as a function of
    (si, sj)—specifically, π / 256 times the distance to the center.

    """
    pic_x, pic_y = __get_dimensions(picture)
    center_x, center_y = pic_x//2, pic_y//2
    new_picture = Picture(pic_x, pic_y)

    def __get_theta(x, y):
        r = math.sqrt((x - center_x)**2 + (y - center_y)**2)
        theta = math.pi * r / swirl_mod

        return theta

    for x in range(pic_x):

        for y in range(pic_y):

            theta = __get_theta(x, y)

            nx = (x - center_x) * math.cos(theta) + (y - center_y) * \
                math.sin(theta) + center_x

            ny = -(x - center_x) * math.sin(theta) + (y - center_y) * \
                math.cos(theta) + center_y

            new_picture.set(int(nx), int(ny), picture.get(x, y))

    return new_picture


def wave_filter(picture: Picture,
                amplitude: int = 20, frequency: int = 64) -> Picture:
    """
    copying the color of each pixel (si, s j) in the
    source image to a target pixel (ti, t j),
    where ti = si and tj = sj +20 sin(2 πsi/64).
    """
    pic_x, pic_y = __get_dimensions(picture)
    new_picture = Picture(pic_x, pic_y)

    for x in range(pic_x):

        for y in range(pic_y):
            nx = x
            ny = y + amplitude*math.sin(2*math.pi*x/frequency)

            new_picture.set(int(nx), int(ny), picture.get(x, y))

    return new_picture


def glass_filter(picture: Picture) -> Picture:
    """
    set each pixel p to the
    color of a random neighboring pixel (whose pixel coordinates are each
                                         within 5 pixels of p’s coordinates).
    """
    pic_x, pic_y = __get_dimensions(picture)
    new_picture = Picture(pic_x, pic_y)

    def __rdm_pixel(x, y):
        """
        Returns a random neighboring pixel within 5 pixels
        """
        random_num = randint(-5, 5)
        nx, ny = random_num + x, random_num + y
        x_limit = 0 <= nx <= (pic_x - 1)
        y_limit = 0 <= ny <= (pic_y - 1)

        if x_limit and y_limit:
            return (nx, ny)
        else:
            __rdm_pixel(x, y)

    for x in range(pic_x):

        for y in range(pic_y):
            rdm_pixel = __rdm_pixel(x, y)

            if rdm_pixel:
                nx, ny = rdm_pixel
                new_picture.set(x, y, picture.get(nx, ny))

    return new_picture


def slide_show(pictures: [Picture]) -> None:
    """
    Takes a list of pictures and displays them one after another to a delay of
    DOWN_TIME. Loops recursively.
    """

    for picture in pictures:
        stddraw.clear()
        stddraw.picture(picture)
        stddraw.show(DOWN_TIME)

    slide_show(pictures)


def pics_with_filters(pictures=[Picture]):

    def __filters(picture):
        amplitude = randint(0, 100)
        frequency = randint(0, 100)
        swirl_mod = randint(0, 512)
        rotation = randint(0, 360)

        rotate_pic = rotation_filter(picture, rotation)
        swirl_pic = swirl_filter(picture, swirl_mod)
        wave_pic = wave_filter(picture, amplitude, frequency)
        glass_pic = glass_filter(picture)
        return [picture, rotate_pic, swirl_pic, wave_pic, glass_pic]

    filtered_pictures = []

    for pic in pictures:
        filter = __filters(pic)
        for filt_pic in filter:
            filtered_pictures.append(filt_pic)

    slide_show(filtered_pictures)

# -------------------------------------------------------------------------------
# Unit Tests
# -------------------------------------------------------------------------------


def build_test():
    picture = __gather_input()

    if type(picture) == list:
        slide_show(picture)
    else:
        rotate_pic = rotation_filter(picture, 25)
        swirl_pic = swirl_filter(picture, 256)
        wave_pic = wave_filter(picture)
        glass_pic = glass_filter(picture)
        pictures = [picture, rotate_pic, swirl_pic, wave_pic, glass_pic]
        slide_show(pictures)

    stddraw.show()


def main():
    """
    Handle Commands
    """
    command, argument, pictures = __gather_input()
    writeln(command)
    writeln(argument)
    writeln(pictures)

    if command == "-S":
        slide_show(pictures)

    elif command == "-r":
        new_pictures = []
        for pic in pictures:
            new_pictures.append(rotation_filter(pic, argument[0]))
        slide_show(new_pictures)

    elif command == "-s":
        new_pictures = []
        for pic in pictures:
            new_pictures.append(swirl_filter(pic, argument[0]))
        slide_show(new_pictures)

    elif command == "-w":
        new_pictures = []
        for pic in pictures:
            new_pictures.append(wave_filter(pic, argument[0], argument[1]))
        slide_show(new_pictures)

    elif command == "-g":
        new_pictures = []
        for pic in pictures:
            new_pictures.append(glass_filter(pic))
        slide_show(new_pictures)

    elif command == "-a":
        pics_with_filters(pictures)

    pass


if __name__ == "__main__":
    main()
