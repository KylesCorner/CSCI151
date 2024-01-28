"""
Kyle Krstulich
04/25/2023
CSCI151
player.py

This code defines a Player class, which represents a player in a card
game. The class has methods to add cards to a player's hand, calculate
the value of the player's hand, place a bet, and print information
about the player's hand and balance. The class also has methods to
determine if the player has blackjack or has bust, and to deal cards to
another player.

The __init__ method initializes a new Player object with a name, balance,
and an optional dealers_deck object. The dealers_deck object represents the
deck of cards that the dealer is using in the game.

The __calc_hand_value method calculates the value of the player's hand by
sorting the cards in the hand, determining the highest possible value for
each card, and summing the values of all the cards in the hand. The
clear_hand method removes all cards from the player's hand and resets the
hand value to zero. The put_card_in_hand method adds a card to the player's
hand and recalculates the hand value. The bet method subtracts the
specified amount from the player's balance if the balance is sufficient to
cover the bet, and returns True if the bet is placed successfully.
Otherwise, it returns False. The add_to_balance method adds the specified
amount to the player's balance.

The win method increases the player's balance by the specified winnings,
prints a message indicating that the player has won, and clears the
player's hand. The blackjack method returns True if the player's hand has a
value of 21 and False otherwise. The bust method returns True if the
player's hand has a value over 21 and False otherwise.

The deal_to method deals the specified number of cards to another player.
If the dealer's deck is too small to accommodate the requested number of
cards, a new deck is created. If the deck is below 30 cards it is shuffled.

The get_balance, get_hand_value, and get_hand_size methods return the
player's balance, hand value, and the number of cards in the player's hand,
respectively. The print_balance, print_player, and print_dealer methods
print information about the player's balance and hand, and in the case of
the print_dealer method, only prints the dealer's first card.
"""
from stdio import writeln
from deck import Deck

# -------------------------------------------------------------------------------
# Classes
# -------------------------------------------------------------------------------


class Player:

    def __init__(self, name: str, balance: float, dealers_deck=None):
        self._name = name
        self._balance = balance
        self._hand = []
        self._hand_value = 0
        self._dealers_deck = dealers_deck

    def __str__(self):
        return f"Player {self._name} has ${self._balance:.2f}"

    def __calc_hand_value(self):

        values = sorted([card.get_value() for card in self._hand])[::-1]
        overall = 0

        for val in values:
            l, h = val
            if h + overall <= 21:  # testing low value
                overall += h
            elif l + overall <= 21:  # testing high value
                overall += l
            else:  # broken hand
                overall += l
                break
        self._hand_value = overall

    def clear_hand(self):
        self._hand = []
        self._hand_value = 0

    def put_card_in_hand(self, card: object):
        self._hand.append(card)
        self.__calc_hand_value()

    def bet(self, amount: float):
        if self._balance - amount >= 0:
            self._balance -= amount
            return True
        else:
            return False

    def add_to_balance(self, amount: float):
        self._balance += amount

    def win(self, winnings: float, other: object):
        self.add_to_balance(winnings)
        writeln()
        name_str = "{:^80}".format(
            "| " + self._name + f" wins ${winnings:.2f}! |")
        bar_str = "{:^80}".format("-"*(len(name_str)//4))
        writeln(bar_str)
        writeln(name_str)
        writeln(bar_str)
        self.print_player()
        self.clear_hand()
        other.print_player()
        other.clear_hand()

    def blackjack(self):
        if self._hand_value == 21:
            return True
        else:
            return False

    def bust(self):
        if self._hand_value > 21:
            return True
        else:
            return False

    def deal_to(self, plr: object, num_cards=2):
        if self._dealers_deck.deck_size() <= num_cards:
            self._dealers_deck = Deck()
            writeln("Grabbing new deck...")

        if self._dealers_deck.deck_size() <= 20:
            self._dealers_deck.shuffle()
            writeln("Shuffling Deck...")

        cards = [self._dealers_deck.deal() for x in range(num_cards)]

        [plr.put_card_in_hand(card) for card in cards]

    def get_balance(self) -> float:
        return self._balance

    def get_hand_value(self) -> int:
        return self._hand_value

    def get_hand_size(self) -> int:
        return len(self._hand)

    def print_balance(self):
        writeln(f"Balance ${self._balance:.2f}")

    def print_player(self):
        writeln()
        writeln(self)
        self.print_hand()
        writeln(f"Hand value: {self.get_hand_value()}\n")

    def print_dealer(self):
        writeln()
        writeln(self)
        self.print_first()

    def print_hand(self):
        [writeln(card) for card in self._hand]

    def print_first(self):
        if len(self._hand) >= 1:
            writeln(self._hand[0])
        else:
            writeln("Something went wrong at print_first!")


def main():
    deck = Deck()
    plr = Player("Kyle", 420.69)
    dealer = Player("dealer", 100, deck)

    writeln(plr)
    writeln(dealer)

    dealer.deal_to(plr, 10)
    dealer.deal_to(dealer, 5)

    dealer.print_player()
    plr.print_player()


if __name__ == "__main__":
    main()
