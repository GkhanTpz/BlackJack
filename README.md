```markdown
# Blackjack Game in Python 🃏

A text-based Blackjack game written in Python, where you compete against a computer-controlled dealer. This project demonstrates key programming principles, like loops, conditionals, and functions, in a fun and interactive way.

---

## 🎮 Game Overview

The objective of the game is to achieve a hand value as close to 21 as possible, without exceeding it. The player and dealer are each dealt an initial hand of two cards, with the player’s cards fully visible and only one of the dealer's cards revealed. Players can then choose to "Hit" to draw additional cards or "Stay" to keep their hand as it is. The dealer must draw cards according to the rules until their hand value reaches 17 or more.

The game ends when the player or dealer reaches 21, goes over 21, or decides to stop drawing cards. The winner is determined based on the final hand values.

---

## 📏 Game Rules

1. **Initial Deal:** Both the player and the dealer receive two cards.
2. **Objective:** Try to reach a score as close to 21 as possible without exceeding it.
3. **Card Values:**
   - **Face Cards (Jack, Queen, King):** Worth 10 points each.
   - **Number Cards:** Worth their respective numbers.
   - **Ace:** Worth 1 or 11 points, depending on the player's choice.
4. **Player's Turn:**
   - **Hit:** The player draws a new card.
   - **Stay:** The player ends their turn and keeps their current hand.
5. **Dealer's Turn:** 
   - The dealer reveals their hidden card and draws additional cards until their total score is at least 17.
6. **Winning Conditions:**
   - If the player exceeds 21, they "bust" and lose.
   - If the dealer exceeds 21, the dealer busts, and the player wins.
   - If neither busts, the hand closer to 21 wins. A score of exactly 21 with the initial two cards is a "Blackjack" and is an automatic win.

---

## 🔍 Gameplay Breakdown

1. **Game Start:** The game begins by dealing two cards each to the player and dealer.
2. **Player’s Turn:**
   - The player views their hand and the dealer’s visible card.
   - They decide to either "Hit" for a new card or "Stay" to end their turn.
   - If the player draws an Ace, they are prompted to choose whether it should be worth 1 or 11.
3. **Dealer’s Turn:** 
   - Once the player decides to stay, the dealer reveals their hidden card.
   - The dealer draws additional cards based on a fixed rule: they will continue drawing cards until their hand value reaches 17 or more.
4. **Result Calculation:** 
   - The scores are compared, and the winner is determined.
   - If both scores are the same, the game results in a draw.
5. **Play Again:** After each game, the player is asked if they want to play again.

---

## 💡 Sample Gameplay

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

Dealer's Hand:
1. Ace of Hearts
2. 6 of Clubs
Dealer's Total Score: 17
-----------------------

You win!

Would you like to play more? (Yes/No):
```


---

## 🧑‍💻 Function Explanations

### `card.py`

- **`draw_hand(number, include_faces_card=True)`**: This function draws a specified number of cards (`number`). By default, it includes face cards (Jack, Queen, King). It calls the `draw_card()` function to generate individual cards and returns them as a formatted string.

- **`draw_card(include_faces_card=True)`**: This function generates a single card with both a rank and suit. The `include_faces_card` parameter determines whether face cards are included in the deck.

- **`get_suit()`**: This function randomly selects a suit for the card. The possible suits are **Hearts**, **Diamonds**, **Spades**, and **Clubs**.

- **`get_rank(include_faces_card=True)`**: This function generates a random rank for the card. If `include_faces_card` is `True`, the rank can be any of the numbers (2–10) or the face cards (Jack, Queen, King). Otherwise, the rank is restricted to numbers between 2 and 10.

---

### `score.py`

- **`calculate_hand(person, card_count, is_dealer=False)`**: This function calculates the total score for a person’s hand (`person`) by drawing a specified number of cards (`card_count`). The `is_dealer` flag determines if the person is the dealer. If it's the dealer's hand, only one card is shown, and the other is hidden.

---

### `dealer.py`

- **`dealer_hand(cards)`**: This function processes the cards in the dealer’s hand and returns their value. Face cards are worth 10 points, Aces are worth 11 points, and numbered cards hold their face value.

---

### `player.py`

- **`player_hand(cards)`**: This function evaluates the player's cards and determines their total score. For an Ace, the player is prompted to choose between 1 or 11. The function ensures valid input and adjusts the score accordingly.

---

### `result.py`

- **`show_hand(person, person_hand, total_score)`**: This function displays the cards in the hand of the specified person (`person`), followed by their total score.

- **`show_result(player_total_score, dealer_total_score)`**: This function displays the outcome of the game, comparing the player’s score to the dealer’s. It announces whether the player wins, loses, or if the game results in a draw.

---

## 📂 File Descriptions

- **card.py**: Main game loop and card drawing functions.
- **dealer.py**: Dealer-specific functions, such as calculating the dealer's hand.
- **player.py**: Handles player-specific logic, including Ace value selection.
- **score.py**: Manages score calculation for each hand.
- **result.py**: Displays the results after each game round.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
```
