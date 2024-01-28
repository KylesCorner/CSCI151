
"""
Kyle Krstulich
1/25/23
cards.py
CSCI 151

Creates a shuffles a deck of cards
"""
import stdio
import stdarray
from random import randint

SUITS = [" of Hearts"," of Diamonds"," of Clubs"," of Spades"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
deck = [rank+suit for suit in SUITS for rank in RANKS]

stdio.writeln(deck)




