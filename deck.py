"""
Kyle Krstulich
04/25/2023
CSCI151
deck.py

This is the implementation of the Deck class for a card game. It
initializes a deck with 52 cards, represented by a list of Card objects.
The __str__ method returns a string representation of the deck, and the
get_deck method returns the deck list.

The deal method removes and returns the first card in the deck if there are
cards remaining, and returns False if the deck is empty.

The deck_size method returns the number of cards remaining in the deck.

The shuffle method shuffles the deck using the random.shuffle function.
"""
from card import Card
from stdio import writeln
import random

# -------------------------------------------------------------------------------
# Classes
# -------------------------------------------------------------------------------


class Deck:

    def __init__(self):
        self._deck = []
        for s in range(0, 4):
            for f in range(0, 13):
                self._deck.append(Card(s, f))
        self.shuffle()

    def __str__(self):
        output_str = ""
        for card in self.get_deck():
            output_str += str(card) + "\n"
        return output_str

    def get_deck(self):
        return self._deck

    def deal(self):
        if len(self._deck) > 1:
            return self._deck.pop(0)
        else:
            return False

    def deck_size(self):
        return len(self._deck)

    def shuffle(self):
        random.shuffle(self._deck)


def main():
    deck = Deck()
    card1 = deck.deal()
    writeln(card1)
    writeln(f"Deck size = {deck.deck_size()}")
    writeln(deck)


if __name__ == "__main__":
    main()
