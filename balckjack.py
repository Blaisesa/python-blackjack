import os
import random

# -------- Utility functions --------


def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

# -------- Card visuals --------


def display_card_lines(card):
    """Return card as a list of strings for printing."""
    value, card_str = card
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
# Build deck with (value, display) tuples


values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
deck = []
for value in values:
    for _ in range(4):
        if value == 10:
            display = random.choice(['10', 'J', 'Q', 'K'])
        elif value == 11:
            display = 'A'
        else:
            display = str(value)
        deck.append((value, display))

random.shuffle(deck)
hands = {"player": [], "dealer": []}

# Calculate total value of a hand, handling aces


def hand_value(hand):
    total = 0
    aces = 0
    for value, _ in hand:
        total += value
        if value == 11:
            aces += 1
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

# -------- Game functions --------


def game_start():
    """Start a round of Blackjack."""
    random.shuffle(deck)
    hands['player'] = [deck.pop(), deck.pop()]
    hands['dealer'] = [deck.pop(), deck.pop()]

    clear_screen()
    print('Deck is shuffled and cards are dealt.')
    print('--------------------------------')

    # Show initial hands
    print("Dealer's hand:")
    print_dealer_cards(hands['dealer'][0], hide_second=True)
    print('--------------------------------')
    print("Player's hand:")
    print_cards_side_by_side(hands['player'])
    print(f"\nPlayer's total: {hand_value(hands['player'])}")
    print('--------------------------------')

    # Check for immediate blackjack
    player_total = hand_value(hands['player'])
    dealer_total = hand_value(hands['dealer'])

    if player_total == 21:
        print("Player has blackjack!")
        if dealer_total == 21:
            print("Dealer also has blackjack! It's a tie!")
        else:
            print("Player wins with blackjack!")
        input('Press "Enter" to restart...')
        clear_screen()
        game_start()
        return
    if dealer_total == 21:
        print("Dealer has blackjack!")
        input('Press "Enter" to restart...')
        clear_screen()
        game_start()
        return

    player_hit()


def dealer_turn():
    while hand_value(hands['dealer']) < 17:
        hands['dealer'].append(deck.pop())

    clear_screen()
    print("Dealer's turn:")
    print_cards_side_by_side(hands['dealer'])
    dealer_total = hand_value(hands['dealer'])
    player_total = hand_value(hands['player'])
    print(f"Dealer's total: {dealer_total}")
    print('--------------------------------')

    if dealer_total > 21:
        print("Dealer busts! Player wins!")
    elif dealer_total > player_total:
        print(f"Dealer wins! ({dealer_total} vs {player_total})")
    elif dealer_total == player_total:
        print(f"It's a tie! ({dealer_total} vs {player_total})")
    else:
        print(f"Player wins! ({player_total} vs {dealer_total})")

    print('--------------------------------')
    input('Press "Enter" to restart...')
    clear_screen()
    main()


def player_hit():
    print('Enter "h" to hit or "s" to stand:')
    choice = input().lower()
    if choice == 'h':
        hands['player'].append(deck.pop())
        clear_screen()
        print("Player hits.")
        total = hand_value(hands['player'])
        print("Player's hand:")
        print_cards_side_by_side(hands['player'])
        print(f"\nPlayer's total: {total}")
        print('--------------------------------')
        if total > 21:
            print("Player busts! Dealer wins.")
            input('Press "Enter" to restart...')
            clear_screen()
            main()
        elif total == 21:
            print("Blackjack!")
            input('Dealer turn, press "Enter" to continue...')
            clear_screen()
            dealer_turn()
        else:
            player_hit()
    elif choice == 's':
        dealer_turn()
    else:
        print("Invalid input.")
        player_hit()

# -------- Entry point --------


def main():
    while True:
        clear_screen()
        print('--------------------------------')
        print('Python Blackjack has been initiated!')
        input('Press Enter to continue...')
        game_start()


clear_screen()
print('--------------------------------')
print('Python Blackjack has been initiated!')
input('Press Enter to continue...')
game_start()
