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
---

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.


