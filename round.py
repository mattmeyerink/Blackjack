"""Basic Blackjack CLI Game."""
import os
from cards import Deck


class Player:
    """Represents a player in the game."""
    def __init__(self):
        self.cards = []
    
    def sum_cards(self):
        """Returns the sum of the values of the players cards"""
        has_ace = False
        sum = 0

        # Add up players cards
        for card in self.cards:
            if card.card_value == "ace":
                has_ace = True
            sum += card.game_value

        # Handle case where ace plays low
        if sum > 21 and has_ace:
            sum -= 10

        return sum
    
    def hit(self, deck):
        """Adds card from deck to the players hand."""
        self.cards.append(deck.draw_card())
    
class Round:
    """Represents a game of blackjack"""
    def __init__(self):
        self.player = Player()
        self.dealer = Player()
        self.deck = Deck()
        self.round_winner = False
        
    def print_header(self):
        """Prints the game header."""
        print()
        print("="*25)
        print()
        print("Have fun in your blackjack round!")
        print()
        print("="*25)

    def print_hands(self):
        """Displays the players hand and the dealers hand."""
        # Clear the terminal and reprint round header
        os.system("clear")
        self.print_header

        # Only display one of the dealers cards if they are still playing
        if not self.round_winner:
            print()
            print("Dealer's Cards")
            print("=" * 25)
            print("UNKNOWN")
            for card in self.dealer.cards:
                if card != self.dealer.cards[0]:
                    print(f"{card.game_value} of {card.suit}")
            print("-"*25)
            print("TOTAL = ?")
            print()

            print("Player's Cards")
            print("=" * 25)
            for card in self.player.cards:
                print(f"{card.game_value} of {card.suit}")
            print("-" * 25)
            print("TOTAL = " + str(self.player.sum_cards()))
            print()

        # Display the players cards and all of the dealers cards
        elif self.round_winner:
            print()
            print("Dealer's Cards")
            print("=" * 25)
            for card in self.dealer.cards:
                print(f"{card.game_value} of {card.suit}")
            print("-" * 25)
            print("TOTAL = " + str(self.dealer.sum_cards()))
            print()

            print("Player's Cards")
            print("=" * 25)
            for card in self.player.cards:
                print(f"{card.game_value} of {card.suit}")
            print("-" * 25)
            print("TOTAL = " + str(self.player.sum_cards()))
            print()
            pass

    def deal(self):
        """Deal two cards to each player"""
        self.dealer.hit(self.deck)
        self.dealer.hit(self.deck)
        self.player.hit(self.deck)
        self.player.hit(self.deck)

        if self.player.sum_cards() == 21:
            self.round_winner = True
            self.print_hands()
            print("BLACKJACK! You win!")

    def player_hit(self):
        """Hits the player with another card."""
        self.player.hit(self.deck)
        self.print_hands()
        
        if self.player.sum_cards() > 21:
            self.round_winner = True
            self.print_hands()
            print("BUST! Dealer wins.")

    def determine_winner(self):
        """Determine who won the game"""
        if self.player.sum_cards() > 21:
            print("BUST! Dealer wins.")

        elif self.dealer.sum_cards() > 21:
            print("DEALER BUSTS! You win")

        elif self.player.sum_cards() > self.dealer.sum_cards():
            print("You win!")

        elif self.dealer.sum_cards() > self.player.sum_cards():
            print("Dealer wins!")

        else:
            print("It's a tie!")

    def play_for_dealer(self):
        """Plays for the dealer."""
        while self.dealer.sum_cards() < 17:
            self.dealer.hit(self.deck)
        else:
            self.round_winner = True
            self.print_hands()
            self.determine_winner()