"""Contains Card and Deck Class for Blackjack program."""
import random


class Card:
    """Represents a card in the game."""
    def __init__(self, suit, card_value, game_value):
        self.suit = suit
        self.card_value = card_value
        self.game_value = game_value

class Deck:
    """Represents a deck in the game."""
    def __init__(self):
        self.cards = []
        self.initialize_deck()

    def draw_card(self):
        """Draw a random card from the deck."""
        cards_in_deck = len(self.cards)
        return self.cards.pop(random.randrange(0, cards_in_deck))

    def add_cards(self, cards):
        """Add played cards back to the deck."""
        for card in cards:
            self.cards.append(card)
        
    def initialize_deck(self):
        """Initialize the deck as a full 52 card deck."""
        self.cards.clear()

        ace_spades = Card("spade", "ace", 11)
        two_spades = Card("spade", "two", 2)
        three_spades = Card("spade", "three", 3)
        four_spades = Card("spade", "four", 4)
        five_spades = Card("spade", "five", 5)
        six_spades = Card("spade", "six", 6)
        seven_spades = Card("spade", "seven", 7)
        eight_spades = Card("spade", "eight", 8)
        nine_spades = Card("spade", "nine", 9)
        ten_spades = Card("spade", "ten", 10)
        jack_spades = Card("spade", "jack", 10)
        queen_spades = Card("spade", "queen", 10)
        king_spades = Card("spade", "king", 10)

        ace_clubs = Card("clubs", "ace", 11)
        two_clubs = Card("clubs", "two", 2)
        three_clubs = Card("clubs", "three", 3)
        four_clubs = Card("clubs", "four", 4)
        five_clubs = Card("clubs", "five", 5)
        six_clubs = Card("clubs", "six", 6)
        seven_clubs = Card("clubs", "seven", 7)
        eight_clubs = Card("clubs", "eight", 8)
        nine_clubs = Card("clubs", "nine", 9)
        ten_clubs = Card("clubs", "ten", 10)
        jack_clubs = Card("clubs", "jack", 10)
        queen_clubs = Card("clubs", "queen", 10)
        king_clubs = Card("clubs", "king", 10)

        ace_hearts = Card("hearts", "ace", 11)
        two_hearts = Card("hearts", "two", 2)
        three_hearts = Card("hearts", "three", 3)
        four_hearts = Card("hearts", "four", 4)
        five_hearts = Card("hearts", "five", 5)
        six_hearts = Card("hearts", "six", 6)
        seven_hearts = Card("hearts", "seven", 7)
        eight_hearts = Card("hearts", "eight", 8)
        nine_hearts = Card("hearts", "nine", 9)
        ten_hearts = Card("hearts", "ten", 10)
        jack_hearts = Card("hearts", "jack", 10)
        queen_hearts = Card("hearts", "queen", 10)
        king_hearts = Card("hearts", "king", 10)

        ace_diamonds = Card("diamond", "ace", 11)
        two_diamonds = Card("diamond", "two", 2)
        three_diamonds = Card("diamond", "three", 3)
        four_diamonds = Card("diamond", "four", 4)
        five_diamonds = Card("diamond", "five", 5)
        six_diamonds = Card("diamond", "six", 6)
        seven_diamonds = Card("diamond", "seven", 7)
        eight_diamonds = Card("diamond", "eight", 8)
        nine_diamonds = Card("diamond", "nine", 9)
        ten_diamonds = Card("diamond", "ten", 10)
        jack_diamonds = Card("diamond", "jack", 10)
        queen_diamonds = Card("diamond", "queen", 10)
        king_diamonds = Card("diamond", "king", 10)

        self.cards += [ace_spades, two_spades, three_spades, four_spades,
                       five_spades, six_spades, seven_spades, eight_spades,
                       seven_spades, eight_spades, nine_spades, ten_spades, 
                       jack_spades, queen_spades, king_spades]

        self.cards += [ace_clubs, two_clubs, three_clubs, four_clubs,
                       five_clubs, six_clubs, seven_clubs, eight_clubs,
                       seven_clubs, eight_clubs, nine_clubs, ten_clubs, 
                       jack_clubs, queen_clubs, king_clubs]

        self.cards += [ace_hearts, two_hearts, three_hearts, four_hearts,
                       five_hearts, six_hearts, seven_hearts, eight_hearts,
                       seven_hearts, eight_hearts, nine_hearts, ten_hearts, 
                       jack_hearts, queen_hearts, king_hearts]

        self.cards += [ace_diamonds, two_diamonds, three_diamonds, four_diamonds,
                       five_diamonds, six_diamonds, seven_diamonds, eight_diamonds,
                       seven_diamonds, eight_diamonds, nine_diamonds, ten_diamonds, 
                       jack_diamonds, queen_diamonds, king_diamonds]