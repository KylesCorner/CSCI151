"""
Kyle Krstulich
04/17/2023
CSCI151
blackjack.py

Problem Statement
Create your own version of the popular game "Blackjack".

Assignment Details

There will only be one player and the dealer
Create a Card, Deck and Player data-type (PURPOSE OF THIS ASSIGNMENT!!!!)
Cards must be reshuffled if deck size is less than 20
Aces can be either 1 or 11 points
A tie is a push – nobody wins or loses
Dealer stands on soft 17
Winnings
Your score beats dealer’s score – 1:1 payout ratio.
(100% increase of your initial bet)
Dealer’s score beats your score – 1:1 loss ratio.
(100% decrease of your initial bet)
Natural Blackjack (A in two. Auto Win unless dealer
                   has a blackjack, then a push) – 3:2 payout ratio.
(150% increase of your initial bet.)


How to play Blackjack
Object of the Game
Each participant attempts to beat the dealer by getting a count as close to 21
as possible, without going over 21.

Card Values/Scoring
It is up to each individual player if an ace is worth 1 or 11. Face cards are
10 and any other card is its pip value.

Betting
Before the deal begins, each player places a bet, in chips, in front of him in
the designated area.

The Deal
When all the players have placed their bets, the dealer gives one card face up
to each player in rotation clockwise, and then one card face up to himself.
Another round of cards is then dealt face up to each player, but the dealer
takes his second card face down. Thus, each player except the dealer receives
two cards face up, and the dealer receives one card face up and one card face
down.

Naturals
If a player's first two cards are an ace and a "ten-card"
(a picture card or 10), giving him a count of 21 in two cards, this is a
natural or "blackjack." If any player has a natural and the dealer does not,
the dealer immediately pays that player one and a half times the amount of his
bet. If the dealer has a natural, he immediately collects the bets of all
players who do not have naturals, (but no additional amount). If the dealer and
another player both have naturals, the bet of that player is a stand-off
(a tie), and the player takes back his chips.

If the dealer's face-up card is a ten-card or an ace, he looks at his face-down
card to see if the two cards make a natural. If the face-up card is not a
ten-card or an ace, he does not look at the face-down card until it is the
dealer's turn to play.

The Play
The player to the left goes first and must decide whether to "stand"
(not ask for another card) or "hit"
(ask for another card in an attempt to get closer to a count of 21, or
 even hit 21 exactly). Thus, a player may stand on the two cards originally
dealt him, or he may ask the dealer for additional cards, one at a time, until
he either decides to stand on the total (if it is 21 or under), or goes "bust"
(if it is over 21). In the latter case, the player loses and the dealer
collects the bet wagered. The dealer then turns to the next player to his left
and serves him in the same manner.

The combination of an ace with a card other than a ten-card is known as a "soft
hand," because the player can count the ace as a 1 or 11, and either draw cards
or not. For example with a "soft 17" (an ace and a 6), the total is 7 or 17.
While a count of 17 is a good hand, the player may wish to draw for a higher
total. If the draw creates a bust hand by counting the ace as an 11, the player
simply counts the ace as a 1 and continues playing by standing or "hitting"
(asking the dealer for additional cards, one at a time).

The Dealer's Play
When the dealer has served every player, his face-down card is turned up. If
the total is 17 or more, he must stand. If the total is 16 or under, he must
take a card. He must continue to take cards until the total is 17 or more, at
which point the dealer must stand. If the dealer has an ace, and counting it as
11 would bring his total to 17 or more (but not over 21), he must count the ace
as 11 and stand. The dealer's decisions, then, are automatic on all plays,
whereas the player always has the option of taking one or more cards.

Settlement
A bet once paid and collected is never returned. Thus, one key advantage to the
dealer is that the player goes first. If the player goes bust, he has already
lost his wager, even if the dealer goes bust as well. If the dealer goes over
21, he pays each player who has stood the amount of that player's bet. If the
dealer stands at 21 or less, he pays the bet of any player having a higher
total (not exceeding 21) and collects the bet of any player having a lower
total. If there is a stand-off (a player having the same total as the dealer),
no chips are paid out or collected.
"""
from stdio import writeln, readFloat
from player import Player
from deck import Deck

# -------------------------------------------------------------------------------
# Private Functions
# -------------------------------------------------------------------------------


def __betting(bet_pool: float, plr: object) -> int:
    """
    Description:
        This function takes in two parameters, bet_pool which is a float
        representing the current betting pool, and plr which is an object
        representing the player.

        The function checks if the betting pool is equal to zero. If it is, the
        function prompts the player to enter a bet amount and assigns the value
        to the bet_pool parameter. If the player does not have enough money to
        place the bet, the function prints a message "Not enough money!" and
        sets the bet_pool to zero.
    Parameters:

        bet_pool (float): Current betting pool.
        plr (object): Player object.
    Returns:

        (int): The updated betting pool.
    """
    if bet_pool == 0:
        while True:
            writeln("-"*80)
            plr.print_player()
            writeln("Enter a bet amount.")
            bet_pool = readFloat()
            if not plr.bet(bet_pool):
                writeln("Not enough money!")
                bet_pool = 0
            else:
                break
    return bet_pool


def __initial_deal(dealer: object, plr: object, bet_pool: float) -> int:
    """
    Description:
        This function takes in three parameters, dealer which is an object
        representing the dealer, plr which is an object representing the
        player, and bet_pool which is a float representing the current betting
        pool.

        The function deals one card to the player and one card to the dealer.
        Then, it checks if the player and the dealer both have blackjack, if
        so, it prints "Neutral Tie" and adds the betting pool to the player's
        balance. If only the player has blackjack, it prints "Blackjack!", adds
        1.5 times the betting pool to the player's balance, and removes 0.5
        times the betting pool from the dealer's balance. If only the dealer
        has blackjack, it prints "House always wins", gives the entire betting
        pool to the dealer, and resets the betting pool to zero.

        The function returns the updated bet_pool.

    Parameters:

        dealer (object): Dealer object.
        plr (object): Player object.
        bet_pool (float): Current betting pool.
    Returns:

        (int): The updated betting pool.
    """

    dealer.deal_to(plr)
    dealer.deal_to(dealer)

    # Neutral Checking
    if plr.blackjack() and dealer.blackjack():
        writeln("Neutral Tie")
        plr.add_to_balance(bet_pool)
        bet_pool = 0

    elif plr.blackjack():
        writeln("Blackjack!")
        plr.win(bet_pool*1.5, dealer)
        dealer.bet(bet_pool * .5)
        bet_pool = 0

    elif dealer.blackjack():
        writeln("House always wins")
        dealer.win(bet_pool, plr)
        bet_pool = 0

    return bet_pool


def __standing(dealer: object, plr: object, bet_pool: float) -> int:
    """
    Description:
        This function takes in three parameters, dealer which is an object
        representing the dealer, plr which is an object representing the
        player, and bet_pool which is a float representing the current betting
        pool.

        The function enters a loop that continues as long as the dealer's hand
        value is less than 17. Within the loop, the dealer deals a card to
        itself.

        If the dealer's hand value exceeds 21, it busts and the function prints
        "Dealer Bust!". The player wins and the betting pool is added to their
        balance. The betting pool is then reset to zero.

        If the dealer's hand value is less than or equal to 21, it compares its
        hand value to the player's hand value. If the dealer's hand value is
        greater than the player's hand value, the dealer wins and the betting
        pool is reset to zero. If the player's hand value is greater than the
        dealer's hand value, the player wins and the betting pool is reset to
        zero. If both the player and the dealer have the same hand value, the
        function prints "Nobody wins..." and adds the betting pool to the
        player's balance. The player and dealer's hands are then cleared and
        the betting pool is reset to zero.

        The function returns the updated bet_pool.

    Parameters:

        dealer (object): Dealer object.
        plr (object): Player object.
        bet_pool (float): Current betting pool.
    Returns:

        (int): The updated betting pool.
    """
    while dealer.get_hand_value() < 17:
        dealer.deal_to(dealer, 1)
    if dealer.bust():
        writeln("Dealer Bust!")
        plr.win(bet_pool, dealer)
        bet_pool = 0
    else:
        if dealer.get_hand_value() > plr.get_hand_value():
            dealer.win(bet_pool, plr)
            bet_pool = 0
        elif dealer.get_hand_value() < plr.get_hand_value():
            plr.win(bet_pool, dealer)
            bet_pool = 0
        else:
            writeln("Nobody wins...\n")
            plr.add_to_balance(bet_pool)
            dealer.print_player()
            plr.print_player()
            plr.clear_hand()
            dealer.clear_hand()
            bet_pool = 0
    return bet_pool


# -------------------------------------------------------------------------------
# Public Functions
# -------------------------------------------------------------------------------


# Refactor
def game_loop():
    """
    This function is the main game loop for playing Blackjack. It
    initializes a Deck object, a Player object for the dealer, and a Player
    object for the player. The game_running variable is set to True to
    start the game loop. The bet_pool variable is initialized to 0.0.

    The game loop starts with a betting phase, where the player is prompted
    to enter a bet amount. The __betting function is called with bet_pool
    and plr as parameters to handle the betting logic.

    If the dealer's hand size is less than 2, the __initial_deal function
    is called with dealer, plr, and bet_pool as parameters to deal the
    initial cards to the player and dealer. If the player's hand size is 0
    after the initial deal, the game continues to the next iteration of the
    while loop.

    The UI is then displayed to the player, showing the dealer's cards, the
    player's cards, and the current pot size. The player is then prompted
    to choose an action: hit, stand, or leave. If the player chooses to
    hit, the dealer deals a card to the player. If the player chooses to
    stand, the standing variable is set to True.

    If the player chooses to leave, the game_running variable is set to
    False and the game loop ends. If the player enters any other input, a
    message is displayed to enter the correct input.

    After the player chooses an action, the function checks the player's
    hand. If the player's hand value exceeds 21, the player busts and the
    dealer wins. The __standing function is called with dealer, plr, and
    bet_pool as parameters to handle the dealer's turn and compare the
    player's and dealer's hand values if the player chooses to stand.

    The function then returns to the beginning of the while loop to start a
    new round of the game.
    """
    deck = Deck()
    dealer = Player("Dealer", 10000, deck)
    plr = Player("Kyle", 500)
    game_running = True
    bet_pool = 0.0

    while game_running:

        # Betting
        bet_pool = __betting(bet_pool, plr)

        # Inital Deal
        if dealer.get_hand_size() < 2:
            standing = False
            bet_pool = __initial_deal(dealer, plr, bet_pool)
            if plr.get_hand_size() == 0:
                continue

        # UI
        dealer.print_dealer()
        plr.print_player()
        writeln()
        writeln(f"Pot -> ${bet_pool:.2f}\n")

        # The Play
        writeln("Enter only numbers")
        writeln("1. Hit, 2. Stand, 3. Leave")
        user_in = readFloat()

        match user_in:
            case 1:
                dealer.deal_to(plr, 1)
            case 2:
                writeln("Standing.")
                standing = True
            case 3:
                writeln("GoodBye!")
                game_running = False
            case _:
                writeln("Enter correct input")

        # check players hands
        if plr.bust():
            writeln("Bust!")
            dealer.win(bet_pool, plr)
            bet_pool = 0

        # standing
        if standing:
            bet_pool = __standing(dealer, plr, bet_pool)


# -------------------------------------------------------------------------------
# Unit Tests
# -------------------------------------------------------------------------------


def main():
    deck = Deck()
    plr = Player("Kyle", 500.00)
    plr.deal_card(deck)
    plr.deal_card(deck)
    plr.deal_card(deck)
    plr.print_hand()
    writeln(plr.get_hand_value())


if __name__ == "__main__":
    game_loop()
