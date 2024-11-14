```markdown
# Blackjack Game in Python

A Python-based command-line Blackjack game where you can play against a computer dealer. This game allows the player to draw cards, decide to "Hit" or "Stay," and attempt to beat the dealer without exceeding 21 points.

## Features

- **Dealer and Player Logic:** The player can choose to "Hit" or "Stay," while the dealer follows preset rules.
- **Face Cards and Ace Logic:** Face cards are valued at 10, and the Ace can be 1 or 11 depending on the player's choice.
- **Realistic Gameplay:** Includes a hidden card for the dealer until the player's turn is over.
- **Replay Option:** The player can choose to play multiple rounds.

## How to Play

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
   python blackjack.py
   ```

## Game Rules

- The objective is to get as close to 21 as possible without going over.
- The dealer must draw cards until they reach at least 17.
- Face cards (Jack, Queen, King) are worth 10 points, and Aces can be worth 1 or 11 points.
- If the player's total is closer to 21 than the dealer’s without exceeding 21, the player wins.

## Files

- **blackjack.py**: Main game loop.
- **card.py**: Handles card drawing and deck management.
- **dealer.py**: Contains dealer logic and scoring for the dealer's hand.
- **player.py**: Contains player-specific logic, including Ace value choices.
- **score.py**: Calculates and manages the scores for both dealer and player.
- **result.py**: Displays hands and results for each round.

## Sample Gameplay

1. The player is dealt two cards and can choose to "Hit" (draw another card) or "Stay" (end their turn).
2. The dealer follows a basic strategy, revealing only one of their cards until the player's turn ends.
3. Once both player and dealer have finished their turns, scores are calculated to determine the winner.

## Example Output

```
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

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License.
```
