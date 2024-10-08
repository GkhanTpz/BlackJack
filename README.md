---

## Blackjack Game Code Explanation

This Python code simulates a simple Blackjack game between a player and a dealer. It implements basic Blackjack rules, allowing the player to make choices while the dealer follows predetermined game logic.

### Functions

#### `draw_hand(number, include_faces_card=True)`
- **Purpose:** Generates a hand of cards for the player or dealer.
- **Parameters:** 
  - `number`: The number of cards to draw.
  - `include_faces_card`: If `True`, the hand may include face cards (Jack, Queen, King).
- **Returns:** A string representing the cards in the hand, with each card on a new line.
- **How it works:** Calls `draw_card()` for each card drawn and concatenates the results.

#### `draw_card(include_faces_card=True)`
- **Purpose:** Draws a single card by combining a rank (like "Ace", "2", "King") and a suit (like "Hearts", "Clubs").
- **Parameters:**
  - `include_faces_card`: If `True`, the card may be a face card.
- **Returns:** A string representing a single card (e.g., "King of Hearts").

#### `get_suit()`
- **Purpose:** Randomly selects a suit for the card (Hearts, Diamonds, Spades, Clubs).
- **Returns:** A string representing the suit of the card.

#### `get_rank(include_faces_card=True)`
- **Purpose:** Generates the rank of a card.
- **Parameters:**
  - `include_faces_card`: If `True`, includes ranks like Jack, Queen, and King.
- **Returns:** A string representing the rank of the card (e.g., "Ace", "7", "King").

#### `blackjack_player(card)`
- **Purpose:** Determines the value of a player's card.
- **Parameters:** 
  - `card`: A string representing the card drawn.
- **Returns:** 
  - Face cards (Jack, Queen, King) are worth 10 points.
  - The player can choose if Ace is worth 1 or 11.
  - All other cards return their numeric value.

#### `blackjack_dealer(card)`
- **Purpose:** Determines the value of a dealer's card.
- **Parameters:** 
  - `card`: A string representing the card drawn.
- **Returns:** 
  - Face cards are worth 10 points.
  - Aces are always worth 11 points for simplicity.

#### `print_hand(person, person_hand, total_score)`
- **Purpose:** Prints the cards in a hand along with the total score.
- **Parameters:** 
  - `person`: Either "Dealer" or "Player".
  - `person_hand`: The hand (cards) drawn by the player or dealer.
  - `total_score`: The total score of the hand.

#### `calculate_hand(person, card_count, is_dealer=False)`
- **Purpose:** Draws a hand and calculates the total score.
- **Parameters:**
  - `person`: "Dealer" or "Player".
  - `card_count`: The number of cards to draw.
  - `is_dealer`: If `True`, one of the dealer's cards remains hidden.
- **Returns:** The hand and the total score of the person.

#### `print_result(player_total_score, dealer_total_score)`
- **Purpose:** Prints the result of the game based on the final scores.
- **Parameters:**
  - `player_total_score`: The player's total hand score.
  - `dealer_total_score`: The dealer's total hand score.

### Game Logic

#### `game()`
- **Purpose:** The main function to simulate a round of Blackjack between the player and the dealer.
- **How it works:**
  1. **Game Introduction:** Displays a welcome message for the Blackjack game.
  2. **Dealer’s Initial Hand:**
     - The dealer is dealt 2 cards, but only one card is shown to the player.
  3. **Player’s Hand:**
     - The player is dealt 2 cards, and their total hand value is calculated using `blackjack_player()`.
  4. **Player Hits or Stays:**
     - The player can choose to "Hit" (draw another card) or "Stay" (end their turn).
     - If the player chooses to hit, their total hand value is updated, and they continue until they either stay or exceed 21.
  5. **Dealer’s Turn:**
     - The dealer draws cards until their total hand value is at least 17.
     - The dealer's total value is updated after each card is drawn.
  6. **Endgame and Result:**
     - The game compares the player's and dealer's hand values:
       - If the values are the same, it results in a draw.
       - If the player has a higher value or if the dealer busts (exceeds 21), the player wins.
       - If the dealer has a higher value without busting, the dealer wins.
  7. **Play Again Prompt:** After each round, the player is asked if they would like to play again.

---
