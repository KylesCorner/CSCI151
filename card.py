"""
Kyle Krstulich
04/25/2023
CSCI151
card.py

The constructor takes two arguments, suit and face, both of which are
integers. The suit argument represents the suit of the card. 0 for hearts,
1 for diamonds, 2 for clubs, and 3 for spades. while the face argument
represents the face value of the card. 0 for an ace, 1-9 for numbered
cards, 10 for a jack, 11 for a queen, and 12 for a king.

The __init__ method initializes instance variables to store the suit, face,
value, suit_conv, face_conv, and card_string. The value variable is a tuple
that contains two values: the first value is the card's value when used as
a low ace, and the second value is the card's value when used as a high
ace. The suit_conv dictionary maps integer values to Unicode characters
that represent the four suits. The face_conv dictionary maps integer values
to strings that represent the card face values. The card_string variable is
a string that describes the card using the face_conv and suit_conv
dictionaries.

The __str__ method returns the card_string variable when the Card object is
printed.

The __repr__ method returns a string representation of the card that
includes the face value and the suit value.

The set_value and get_value methods allow the value of the card to be set
and retrieved.

The get_face method allows the face value of the card to be retrieved.
"""
from stdio import writeln
# -------------------------------------------------------------------------------
# Classes
# -------------------------------------------------------------------------------


class Card:

    #  suit = {0:heart, 1:diamond, 2:club, 3:spade}
    #  face = {0:Ace, ..., 10:jack, 11:queen, 12:king}
    def __init__(self, suit: int, face: int):
        self._face = int(face)
        self._suit = int(suit)
        self._suit_conv = {
            0: "\u2661",
            1: "\u2662",
            2: "\u2663",
            3: "\u2660"
        }
        self._face_conv = {
            0: "Ace",
            1: "Two",
            2: "Three",
            3: "Four",
            4: "Five",
            5: "Six",
            6: "Seven",
            7: "Eight",
            8: "Nine",
            9: "Ten",
            10: "Jack",
            11: "Queen",
            12: "King"
        }
        self._card_string = f"{self._face_conv[self._face]} of "\
            f"{self._suit_conv[self._suit]}'s"

        if face == 0:
            self._value = (1, 11)
        elif face >= 10:
            self._value = (10, 10)
        else:
            self._value = (self._face + 1, self._face + 1)

    def __str__(self):
        return self._card_string

    def __repr__(self):
        return f"({self._suit}, {self._face})"

    def set_value(self, value: int):
        self._value = value

    def get_value(self) -> int:
        return self._value

    def get_face(self) -> int:
        return self._face


def main():
    ace_spade = Card(3, 0)
    writeln(ace_spade)


if __name__ == "__main__":
    main()
