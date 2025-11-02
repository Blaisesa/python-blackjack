# python-blackjack

<!-- for now just set the thought process -->
1. define the rules of blackjack
   - standard 52-card deck
   - player aims to get as close to 21 as possible without going over
   - face cards are worth 10, aces can be 1 or 11, others are worth their face value
   - player is dealt two cards, dealer is dealt two cards (one face up, one face down)
   - player can see one of the dealer's cards
   - player can choose to hit (take another card) or stand (end their turn)
   - dealer must hit until reaching at least 17
   - player can choose to hit, stand, double down, or split (if applicable)
   - determine winning conditions (player wins, dealer wins, push)

2. define the classes needed (e.g., Card, Deck, Hand, Player, Dealer)
   - Card: represents a single playing card
   - Deck: represents the deck of cards
   - Hand: represents a player's or dealer's hand of cards
   - Player: represents the player
   - Dealer: represents the dealer

3. implement the game logic (dealing cards, player actions, dealer actions, determining winners)

4. create a user interface (text-based within the console)
   - display the current state of the game (player's hand, dealer's hand, etc.)
   - prompt the player for actions (hit, stand, double down, split)
   - show messages for wins, losses, and pushes

5. test the game thoroughly