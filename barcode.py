"""
Kyle Krstulich
2/13/23
CSCI151
barcode.py

Problem Statement

The barcode used by the U.S. Postal System to route mail is defined as follows:
Each decimal digit in the ZIP code is encoded using a sequence of three
half-height and two full-height bars.  The barcode starts and ends with a
full-height bar (the guard rail) and includes a checksum digit (after the
five-digit ZIP code or ZIP + 4), computed by summing up the original digits
modulo 10.

Define the following functions:

Draw a half-height or full-height bar on stddraw.
Given a digit, draw its sequence of bars.
Compute the checksum digit.

Also define global code that read in a five- (or nine-) digit ZIP code as the
command-line argument and draws the corresponding postal barcode.
"""
import stddraw
from sys import argv
from stdio import writeln


class Screen:

    # -------------------------------------------------------------------------------
    # Object values and default settings
    # -------------------------------------------------------------------------------

    def __init__(self, code_to_draw, down_time=0):
        self.down_time = down_time
        self.code_to_draw = code_to_draw

        stddraw.clear(stddraw.LIGHT_GRAY)
        stddraw.setYscale(min=0, max=6)
        self.flip_display()

    # -------------------------------------------------------------------------------
    # Private methods
    # -------------------------------------------------------------------------------

    def __draw_bar(self, index, value="1"):
        """
        Draws a single bar at the index.
        """
        stddraw.filledRectangle((index*2), 0, 1, (int(value)+1))
        self.flip_display()

    # -------------------------------------------------------------------------------
    # Public methods
    # -------------------------------------------------------------------------------

    def flip_display(self):
        """
        Flips the screen and animates to the time of down_time.
        """
        stddraw.show(self.down_time)

    def draw(self):
        """
        Draws the barcode to the screen.
        """
        stddraw.setXscale(min=0, max=len(self.code_to_draw)*2)
        for index, value in enumerate(self.code_to_draw):
            self.__draw_bar(index, value)


class Complile:
    # -------------------------------------------------------------------------------
    # Compile object values and default settings
    # -------------------------------------------------------------------------------

    def __init__(self, code_string):
        self.bar_code_key = {
            1: "0011",
            2: "00101",
            3: "00110",
            4: "01001",
            5: "01010",
            6: "01100",
            7: "10001",
            8: "10010",
            9: "10100",
            0: "11000"
        }
        self.code_string = code_string
        self.output_string = "1"

    # -------------------------------------------------------------------------------
    # Private methods
    # -------------------------------------------------------------------------------

    def __checksum(self):
        """
        Generates a checksum for the command-line input value.
        Appends to the same input value.
        """
        checksum = 0

        for code in self.code_string:

            checksum += int(code)

        checksum %= 10

        self.code_string += str(checksum)

    def __parse(self):
        """
        Generates a checksum. Then parses human readable code and passes it to
        the assemble function. Appends full bar to the end.

        """
        self.__checksum()

        for code in self.code_string:

            self.__assemble(int(code))

        self.output_string += "1"

    def __assemble(self, code):
        """
        Translates human readable code into barcode format.
        """
        self.output_string += self.bar_code_key[code]

    # -------------------------------------------------------------------------------
    # Public methods
    # -------------------------------------------------------------------------------

    def output(self):
        """
        Parses and assembles human readable code into bar code.
        Returns the bar code.
        """
        self.__parse()
        return self.output_string


# -------------------------------------------------------------------------------
# Global functions
# -------------------------------------------------------------------------------

def display_loop():
    comp = Complile(code_string)
    code_to_draw = comp.output()

    io = Screen(code_to_draw=code_to_draw, down_time=10)
    io.draw()

    while True:
        io.flip_display()


# -------------------------------------------------------------------------------
# Global code
# -------------------------------------------------------------------------------

if len(argv) >= 2:
    code_string = argv[1]
else:
    writeln("Enter a number")
    exit()


if __name__ == "__main__":
    display_loop()
