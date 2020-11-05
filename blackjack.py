"""Basic CLI Blackjack Game"""
from round import Round


def print_menu():
    print()
    print("Options")
    print("-" * 25)
    print("(1) Play a game of blackjack")
    print("(2) Quit")
    print()

def blackjack():
    """Manages the blackjack game"""
    print_menu()
    menu_choice = input("What would you like to do (1/2)? ")

    while menu_choice == "1":
        current_round = Round()

        current_round.print_header()

        current_round.deal()

        # Ends the game if the player gets blackjack
        if current_round.round_winner:
            print_menu()
            menu_choice = input("What would you like to do (1/2)? ")
            continue

        current_round.print_hands()

        move = input("What is your move (Hit/Stay)? ")
        while move == "Hit" and current_round.round_winner == False:
            current_round.player_hit()
            if current_round.round_winner == False:
                move = input("What is your move (Hit/Stay)? ")
        
        # Only plays the dealer if the player doesn't bust
        if not current_round.round_winner:
            current_round.play_for_dealer()

        print_menu()
        menu_choice = input("What would you like to do (1/2)? ")

blackjack()