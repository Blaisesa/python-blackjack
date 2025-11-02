import os
import random


# -------- Utility functions --------
def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


# -------- Card visuals --------
def card_string(card):
    """Convert card value to its string representation."""
    if card == 11:
        return 'A'
    elif card == 10:
        random_face = random.choice(['10', 'J', 'Q', 'K'])
        return random_face
    else:
        return str(card)


def display_card_lines(card):
    card_str = card_string(card)
    return [
        "┌─────────┐",
        f"│{card_str:<2}       │",
        "│         │",
        "│         │",
        "│    ♦    │",
        "│         │",
        "│         │",
        f"│       {card_str:>2}│",
        "└─────────┘",
    ]


def hidden_card_lines():
    """Return a hidden (face-down) card as a list of strings."""
    return [
        "┌─────────┐",
        "│░░░░░░░░░│",
        "│░░░░░░░░░│",
        "│░░░░░░░░░│",
        "│░░░░░░░░░│",
        "│░░░░░░░░░│",
        "│░░░░░░░░░│",
        "│░░░░░░░░░│",
        "└─────────┘",
    ]


def print_cards_side_by_side(cards):
    """Print a list of cards side by side."""
    card_lines = [display_card_lines(card) for card in cards]
    for i in range(len(card_lines[0])):
        print("  ".join(card[i] for card in card_lines))


def print_dealer_cards(first_card, hide_second=True):
    """Print dealer's cards (one hidden if needed)."""
    cards_to_print = [display_card_lines(first_card)]
    if hide_second:
        cards_to_print.append(hidden_card_lines())
    for i in range(len(cards_to_print[0])):
        print("  ".join(card[i] for card in cards_to_print))


# -------- Game logic --------
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
deck = cards * 4
hands = {"player": [], "dealer": []}


def game_start():
    """Start a round of Blackjack."""
    random.shuffle(deck)
    hands['player'] = [deck.pop(), deck.pop()]
    hands['dealer'] = [deck.pop(), deck.pop()]
    # Check for immediate blackjack
    print('Deck is shuffled and cards are dealt.')
    print('--------------------------------')
    if (
        sum(hands['player']) == 21
        and (hands['dealer'][0] == 11 or hands['dealer'][0] == 10)
    ):
        print("Dealer's hand:")
        print_dealer_cards(hands['dealer'][0], hide_second=True)
        print('--------------------------------')
        print("Player's hand:")
        print_cards_side_by_side(hands['player'])
        print('--------------------------------')
        print("Player has blackjack!")
        print('--------------------------------')
        print("Check if dealer also has blackjack...")
        input('Press "Enter" to continue...')
        clear_screen()
        if sum(hands['dealer']) == 21:
            print("Dealer's hand:")
            print_cards_side_by_side(hands['dealer'])
            print("Both player and dealer have blackjack! It's a tie!")
            input('Press "Enter" to restart...')
            clear_screen()
            game_start()
            return
        else:
            print_cards_side_by_side(hands['dealer'])
            print('--------------------------------')
            print("Dealer doesn't have blackjack! Player wins!")
            print('--------------------------------')
            print_cards_side_by_side(hands['player'])
            print('--------------------------------')
            print("Player wins with blackjack!")
            print('--------------------------------')
            print(
                f"Dealer's total: {sum(hands['dealer'])} vs "
                f"Player's total: {sum(hands['player'])}"
            )
            print('--------------------------------')
            input('Press "Enter" to restart...')
            clear_screen()
            game_start()
            return
    if hands['dealer'][0] == 11 or hands['dealer'][0] == 10:
        print_dealer_cards(hands['dealer'][0], hide_second=True)
        print('--------------------------------')
        print_cards_side_by_side(hands['player'])
        print(f"\nPlayer's total: {sum(hands['player'])}")
        print('--------------------------------')
        print('Dealer has a potential blackjack.')
        print('--------------------------------')
        print("Checking for dealer blackjack...")
        input('Press "Enter" to continue...')
        clear_screen()
        if sum(hands['dealer']) == 21:
            print("Dealer's hand:")
            print_cards_side_by_side(hands['dealer'])
            print("Dealer has blackjack!")
            input('Press "Enter" to restart...')
            clear_screen()
            game_start()
            return
        else:
            print("No blackjack for dealer.")
            input('Press "Enter" to continue...')
            clear_screen()
    if sum(hands['player']) == 21:
        print("Dealer's hand:")
        print_cards_side_by_side(hands['dealer'])
        print('--------------------------------')
        print("Player's hand:")
        print_cards_side_by_side(hands['player'])
        print("Player has blackjack!")
        input('Press "Enter" to restart...')
        clear_screen()
        game_start()
        return
    print('--------------------------------')
    print("Dealer's hand:")
    print_dealer_cards(hands['dealer'][0], hide_second=True)
    print('--------------------------------')
    print("Player's hand:")
    print_cards_side_by_side(hands['player'])
    print(f"\nPlayer's total: {sum(hands['player'])}")
    print('--------------------------------')
    player_hit()


def dealer_turn():
    while sum(hands['dealer']) < 17:
        hands['dealer'].append(deck.pop())
    clear_screen()
    print("Dealer's turn:")
    print_cards_side_by_side(hands['dealer'])
    print(f"Dealer's total: {sum(hands['dealer'])}")
    print('--------------------------------')
    if sum(hands['dealer']) > 21:
        print("Dealer busts! Player wins!")
    elif sum(hands['dealer']) == 21:
        print("Blackjack! Dealer wins!")
    elif sum(hands['dealer']) > sum(hands['player']):
        print_cards_side_by_side(hands['player'])
        print(f"\nPlayer's total: {sum(hands['player'])}")
        print('--------------------------------')
        print(
            f"Dealer's total: {sum(hands['dealer'])} vs "
            f"Player's total: {sum(hands['player'])}"
        )
        print('--------------------------------')
        print("Dealer wins!")
    elif sum(hands['dealer']) == sum(hands['player']):
        print_cards_side_by_side(hands['player'])
        print(f"\nPlayer's total: {sum(hands['player'])}")
        print('--------------------------------')
        print(
            f"Dealer's total: {sum(hands['dealer'])} vs "
            f"Player's total: {sum(hands['player'])}"
        )
        print('--------------------------------')
        print("It's a tie!")
    else:
        print_cards_side_by_side(hands['player'])
        print(f"\nPlayer's total: {sum(hands['player'])}")
        print('--------------------------------')
        print(
            f"Dealer's total: {sum(hands['dealer'])} vs "
            f"Player's total: {sum(hands['player'])}"
        )
        print('--------------------------------')
        print("Player wins!")
    print('--------------------------------')
    input('Press "Enter" to restart...')
    clear_screen()
    game_start()


def player_hit():
    print('Enter "h" to hit or "s" to stand:')
    choice = input().lower()
    if choice == 'h':
        hands['player'].append(deck.pop())
        clear_screen()
        print("Player hits.")
        if sum(hands['player']) > 21:
            print("Player's hand:")
            print_cards_side_by_side(hands['player'])
            print(f"\nPlayer's total: {sum(hands['player'])}")
            print("Player busts! Dealer wins.")
            input('Press "Enter" to restart...')
            clear_screen()
            game_start()
            return
        elif sum(hands['player']) == 21:
            print("Player's hand:")
            print_cards_side_by_side(hands['player'])
            print(f"\nPlayer's total: {sum(hands['player'])}")
            print("Blackjack!")
            input('Dealers turn, press "Enter" to continue...')
            clear_screen()
            dealer_turn()
            return
        else:
            print("Player's hand:")
            print_cards_side_by_side(hands['player'])
            print(f"\nPlayer's total: {sum(hands['player'])}")
            print('--------------------------------')
            player_hit()
    elif choice == 's':
        dealer_turn()
    else:
        print("Invalid input.")
        player_hit()


# -------- Entry point --------
clear_screen()
print('--------------------------------')
print('Python Blackjack has been initiated!')
input('Press Enter to continue...')
game_start()
