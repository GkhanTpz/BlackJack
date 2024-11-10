---

# Blackjack Game

This project is a Python-based Blackjack game where the player competes against an automated dealer. The game adheres to basic Blackjack rules and is designed with modular code for ease of understanding and modification.

## Game Overview

The goal of Blackjack is to get a hand value as close to 21 as possible without going over. The player competes against a dealer who follows set rules for drawing cards.

## Project Structure

The game is organized into several modules, each handling a specific aspect of the game, from drawing cards to managing the dealer's logic. Here’s a breakdown of each module:

### 1. `main.py`

The main entry point of the game. It sets up the game loop, handles player and dealer actions, and determines the game outcome.

- **Game Setup**: Initializes the dealer's and player's hands.
- **Player Turn**:
  - Prompts the player to "Hit" or "Stay".
  - If the player chooses "Hit," they receive another card, and their score is updated.
  - If the player’s score exceeds 21, they bust, ending the game round.
- **Dealer Turn**:
  - The dealer will continue to draw cards until their hand reaches at least 17.
  - If the dealer’s hand contains an Ace, it may adjust the Ace’s value from 11 to 1 to prevent a bust.
- **Game Result**: Displays both the player’s and dealer’s hands and total scores, determining the winner.

### 2. `blackjack.py`

Manages card drawing and deck functionality, including creating suits and ranks.

- **`draw_hand(number, include_faces_card=True)`**: Draws a specified number of cards and returns them as a formatted string.
- **`draw_card(include_faces_card=True)`**: Draws a single card, randomly selecting a suit and rank.
- **`get_suit()`**: Returns a random suit ("Hearts," "Diamonds," "Spades," or "Clubs").
- **`get_rank(include_faces_card=True)`**: Returns a random rank from 2-10 and face cards (Jack, Queen, King, Ace). The face cards and Ace are included by default unless specified otherwise.

### 3. `dealer.py`

Handles the dealer’s behavior and hand scoring logic.

- **`dealer_hand(card)`**: Takes a card as input and returns its value based on standard Blackjack scoring:
  - Face cards (Jack, Queen, King) are valued at 10.
  - Ace is valued at 11 (adjustable in `main.py` to 1 if needed to avoid busting).
  - Numbered cards retain their face value.

### 4. `player.py`

Controls the player’s hand logic, allowing flexibility with Ace values.

- **`player_hand(card)`**: Determines the value of a card for the player:
  - Prompts the player to choose a value of 1 or 11 for an Ace.
  - Returns 10 for face cards and the card's number value otherwise.

### 5. `result.py`

Displays game results, including each hand and total scores.

- **`print_hand(person, person_hand, total_score)`**: Displays each card in a player’s or dealer’s hand, along with their total score.
- **`print_result(player_total_score, dealer_total_score)`**: Determines and prints the game outcome based on the player’s and dealer’s scores:
  - Declares "Draw" if scores are equal.
  - Declares the player as the winner if the dealer busts or the player's score is closer to 21.
  - Otherwise, the dealer wins.

### 6. `score.py`

Calculates the initial hands and scores for both the dealer and player.

- **`calculate_hand(person, card_count, is_dealer=False)`**:
  - Draws a specified number of cards for the player or dealer.
  - Displays the dealer’s first card while hiding the second, per standard Blackjack rules.
  - Calculates and returns the total score by summing card values using either `dealer.dealer_hand()` or `player.player_hand()` based on the `is_dealer` flag.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/GkhanTpz/BlackJack.git
   cd BlackJack
   ```

2. Run the game:
   ```bash
   python main.py
   ```

## Gameplay Instructions

1. **Objective**: Achieve a hand total closest to 21 without exceeding it.
2. **Player Actions**:
   - **Hit**: Draw an additional card.
   - **Stay**: End your turn, leaving your current total as is.
3. **Winning Conditions**:
   - If the player's score is over 21, they bust, and the dealer wins.
   - If the dealer's score exceeds 21, the player wins.
   - The hand closest to 21 without going over wins the round.

---

