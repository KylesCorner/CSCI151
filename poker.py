"""
Kyle Krstulich
3/1/23
CSCI151
poker.py

2.2.24 Poker analysis. Compose a stdrandom and stdstats client
(with appropriate functions of its own) to estimate the probabilities of
getting one pair, two pair, three of a kind, a full house, and a flush in
a five-card poker hand via simulation. Divide your program into appropriate
functions and defend your design decisions. Extra credit: Add straight and
straight flush to the list of possibilities.

"""
from stdio import writeln
import stdstats
import stdrandom
import stdarray
# -------------------------------------------------------------------------------
# Global Variables
# -------------------------------------------------------------------------------

deck = stdarray.create1D(52, ())

# -------------------------------------------------------------------------------
# Public Functions
# -------------------------------------------------------------------------------


def create_deck():
    """
    Grabs the default global deck and fills it with cards as a tuple
    (CARD_NUMBER, SUIT). Returns None
    """
    global deck
    SUITS = ["\u2660", "\u2666", "\u2665", "\u2663"]
    # spade, diamond, heart, club

    for suit_index, suit in enumerate(SUITS):  # fills array with cards

        for number in range(1, 14):

            card_index = (number + (suit_index*13))-1
            deck[card_index] = (number, suit)


def draw_card(card_index=0):
    """
    Pops a card from the global deck. Returns the card as a tuple.

    """
    return deck.pop(card_index)


# -------------------------------------------------------------------------------
# Test Client
# -------------------------------------------------------------------------------


def main():
    create_deck()
    stdrandom.shuffle(deck)

    hand = [draw_card() for x in range(5)]
    river = [draw_card() for x in range(5)]

    writeln(f"hand: {hand}")
    writeln(f"river: {river}")

    pass


if __name__ == "__main__":
    main()
