"""Basic Blackjack CLI Game."""
from cards import Deck


class Player:
    """Represents a player in the game."""
    def __init__(self, cards):
        self.cards = cards
    
    def add_card(self, card):
        """Adds the passed card to the players hand."""
        self.cards.append(card)
    
    def sum_cards(self):
        """Returns the sum of the values of the players cards"""
        sum = 0
        for card in self.cards:
            sum += card.value()
        return sum
    
