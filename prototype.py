import os

os.system('cls' if os.name == 'nt' else 'clear')

# Define the classes and functions for a simple blackjack game
# 10 represents J, Q, K; 11 represents Ace
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
deck = cards * 4  # Standard deck of 52 cards
hands = {
    "player": [],
    "dealer": []
}
game_started = False


def game_start():
    import random
    random.shuffle(deck)
    hands["player"] = [deck.pop(), deck.pop()]
    # Keep the second card hidden for the dealer
    hands["dealer"] = [deck.pop(), deck.pop()]
    print("Game started!")
    print('--------------------------------')
    if hands['dealer'][0] == 11 or hands['dealer'][0] == 10:
        print(f"Dealer's card: {hands['dealer'][0]}, X")
        print("Checking for blackjack...")
        if sum(hands["dealer"]) == 21:
            print(f"Dealer's hand: {hands['dealer'][0]}, {hands['dealer'][1]}")
            print("Blackjack! Dealer wins!")
            input('Press Enter to restart...')
            if input() == "":
                os.system('cls' if os.name == 'nt' else 'clear')
                game_start()
            else:
                return  # End the game if dealer has blackjack
        else:
            print("No blackjack for dealer.")
            print('--------------------------------')
    if sum(hands['player']) == 21:
        print(f"Player's hand: {hands['player'][0]}, {hands['player'][1]}")
        print("Blackjack! Player wins!")
        input('Press Enter to restart...')
        if input() == "":
            os.system('cls' if os.name == 'nt' else 'clear')
            game_start()
        else:
            return  # End the game if player has blackjack
    elif sum(hands['player']) > 21:
        print("Bust! Player loses.")
        input('Press Enter to restart...')
        if input() == "":
            os.system('cls' if os.name == 'nt' else 'clear')
            game_start()
        else:
            return  # End the game if player busts
    print(f"Dealer's hand: {hands['dealer'][0]}, X")
    print('--------------------------------')
    print(f"Player's hand: {hands['player'][0]}, {hands['player'][1]}")
    print(f"Player's total: {sum(hands['player'])}")
    print('--------------------------------')
    # Check for blackjack immediately after dealing for player
    if sum(hands["player"]) == 21:
        print("Blackjack! Player wins!")
        input('Press Enter to restart...')
        if input() == "":
            os.system('cls' if os.name == 'nt' else 'clear')
            game_start()
        else:
            return  # End the game if player has blackjack
    else:
        player_turn()


def player_turn():
    print('your turn: hit or stand? (h/s)')
    player_choice = input().lower()
    os.system('cls' if os.name == 'nt' else 'clear')
    if player_choice == 'h':
        hands["player"].append(deck.pop())
        print(f"Player's hand: {', '.join(map(str, hands['player']))}")
        print(f"Player's total: {sum(hands['player'])}")
        if sum(hands["player"]) > 21:
            print("Bust! Player loses.")
            if input('Press Enter to restart...') == "":
                os.system('cls' if os.name == 'nt' else 'clear')
                game_start()
            else:
                return
        elif sum(hands["player"]) == 21:
            print("Player has 21!")
            dealer_turn()
        else:
            player_turn()
    elif player_choice == 's':
        dealer_turn()
    else:
        print("Invalid choice. Please enter 'h' to hit or 's' to stand.")
        player_turn()


def dealer_turn():
    print("Dealer's turn.")
    print(f"Dealer's hand: {hands['dealer'][0]}, {hands['dealer'][1]}")
    print(f"Dealer's total: {sum(hands['dealer'])}")
    while sum(hands["dealer"]) < 17:
        hands["dealer"].append(deck.pop())
        print(f"Dealer hits: {', '.join(map(str, hands['dealer']))}")
        print(f"Dealer's total: {sum(hands['dealer'])}")
    if sum(hands["dealer"]) > 21:
        print("Dealer's total:", sum(hands["dealer"]))
        print("Dealer busts! Player wins.")
        input('Press Enter to restart...')
        if input() == "":
            os.system('cls' if os.name == 'nt' else 'clear')
            game_start()
    else:
        determine_winner()


def determine_winner():
    player_total = sum(hands["player"])
    dealer_total = sum(hands["dealer"])
    print(f"Player's total: {player_total}")
    print(f"Dealer's total: {dealer_total}")
    if player_total > dealer_total:
        print("Player wins!")
        input('Press Enter to restart...')
        if input() == "":
            os.system('cls' if os.name == 'nt' else 'clear')
            game_start()
        else:
            return
    elif dealer_total > player_total:
        print("Dealer wins!")
        input('Press Enter to restart...')
        if input() == "":
            os.system('cls' if os.name == 'nt' else 'clear')
            game_start()
    else:
        print("It's a tie!")
        input('Press Enter to restart...')
        if input() == "":
            os.system('cls' if os.name == 'nt' else 'clear')
            game_start()
        else:
            return


print("Blackjack module loaded.")
input('Press Enter to start the game...')
if input() == "":
    game_started = True
    game_start()
