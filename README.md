```markdown
# Blackjack Game in Python 🃏

A simple, text-based Blackjack game created in Python where you play against a computer dealer. This game covers essential Blackjack rules and includes various interactive elements, such as choosing card values for Aces, and "Hit" or "Stay" decisions to make each round unique.

## 📋 Table of Contents

- [Features](#features)
- [Rules](#rules)
- [Setup and Installation](#setup-and-installation)
- [How to Play](#how-to-play)
- [File Descriptions](#file-descriptions)
- [Function Explanations](#function-explanations)
- [Sample Gameplay](#sample-gameplay)
- [License](#license)

---

## 🕹️ Features

- **Player Decisions:** The player can "Hit" to draw a new card or "Stay" to end their turn.
- **Dealer Behavior:** The dealer’s hand follows Blackjack rules and draws until it reaches at least 17.
- **Score Calculation:** Face cards (Jack, Queen, King) are worth 10 points, Aces can be 1 or 11, and other cards are worth their number.
- **Replay Option:** After each game, players can choose to play again.

## 🃏 Rules

- **Objective:** Reach a score as close to 21 as possible without going over.
- **Player vs. Dealer:** You play against the dealer, aiming to beat their score or avoid busting.
- **Face Cards:** Jack, Queen, and King are worth 10 points each.
- **Ace:** Can be worth 1 or 11, depending on the player’s choice.

## ⚙️ Setup and Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/GkhanTpz/BlackJack.git
   ```
2. **Navigate to the Project Directory:**
   ```bash
   cd BlackJack
   ```
3. **Run the Game:**
   ```bash
   python card.py
   ```

## 🎮 How to Play

1. **Game Start:** When the game starts, you and the dealer are each dealt two cards.
2. **Hit or Stay:** Decide to "Hit" to get a new card or "Stay" to end your turn.
3. **Dealer's Turn:** After you stay, the dealer reveals their hidden card and draws cards according to the rules.
4. **Winning:** You win by having a higher score than the dealer without going over 21, or if the dealer busts by exceeding 21.

## 📂 File Descriptions

- **card.py**: Main game loop and card drawing functions.
- **dealer.py**: Dealer-specific functions, such as calculating the dealer's hand.
- **player.py**: Handles player-specific logic, including Ace value selection.
- **score.py**: Manages score calculation for each hand.
- **result.py**: Displays the results after each game round.

## 🔍 Function Explanations

### `card.py`
- **`draw_hand(number, include_faces_card=True)`**: Draws a specified number of cards, returning them as a formatted string. The `include_faces_card` parameter determines if face cards (Jack, Queen, King) are included.
- **`draw_card(include_faces_card=True)`**: Draws a single card with a rank and suit, based on the `include_faces_card` parameter.
- **`get_suit()`**: Randomly selects a suit (Hearts, Diamonds, Spades, or Clubs) for a card.
- **`get_rank(include_faces_card=True)`**: Generates a rank for a card, choosing between numbers (2-10) or face cards depending on the parameter.

### `score.py`
- **`calculate_hand(person, card_count, is_dealer=False)`**: Calculates the total score for the player's or dealer's hand by drawing `card_count` cards. If `is_dealer` is `True`, only one card is displayed initially.
  
### `dealer.py`
- **`dealer_hand(cards)`**: Evaluates the dealer’s cards, assigning values based on rank. Face cards are worth 10, Aces are 11, and number cards are their numeric value.

### `player.py`
- **`player_hand(cards)`**: Evaluates the player’s cards, assigning values based on rank. For an Ace, it prompts the player to choose its value (1 or 11). Other cards are valued according to their rank.

### `result.py`
- **`show_hand(person, person_hand, total_score)`**: Displays each card in a person's hand, followed by their total score.
- **`show_result(player_total_score, dealer_total_score)`**: Displays the outcome of the game, determining the winner based on the player’s and dealer’s total scores.

## 📺 Sample Gameplay

```plaintext
===========
BLACK JACK
===========

Dealer:
1. Ace of Hearts
2. **********
-----------------------

You:
1. 8 of Clubs
2. 7 of Spades
Your Total Score: 15
-----------------------

Hit or Stay: Hit
3. 5 of Diamonds
Your Total Score: 20
-----------------------

The Dealer wins.

Would you like to play more? (Yes/No):
```

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
```
