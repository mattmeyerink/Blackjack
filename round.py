"""Basic Blackjack CLI Game."""
from cards import Deck

class Player:
    """Represents a player in the game."""
    def __init__(self):
        self.cards = []
    
    def sum_cards(self):
        """Returns the sum of the values of the players cards"""
        sum = 0
        for card in self.cards:
            sum += card.game_value()
        return sum
    
    def hit(self, deck):
        """Adds card from deck to the players hand."""
        self.cart.append(deck.draw_card())
    
class Round:
    """Represents a game of blackjack"""
    def __init__(self):
        self.player = Player()
        self.dealer = Player()
        self.deck = Deck()
        self.round_done = False

    def print_hands():
        """Displays the players hand and the dealers hand."""
        # Only display one of the dealers cards if they are still playing
        if not self.round_done:
            pass
        
        # Display the players cards and all of the dealers cards
        elif round_done:
            pass
    
    def play_for_dealer():
        """Plays for the dealer."""
        pass

    def player_move():
        """Perform the player's move."""
        pass