import random


def draw_hand(number, include_faces_card = True):
    hand = ""
    for card in range(number):
        hand += draw_card(include_faces_card) + "\n"
    return hand

def draw_card(include_faces_card = True):
    return get_rank(include_faces_card) + " of " + get_suit()

def get_suit():
    card_choice = random.randint(1, 4)
    if card_choice == 1:
        return "Hearts"
    elif card_choice == 2:
        return "Diamonds"
    elif card_choice == 3:
        return "Spades"
    else:
        return "Clubs"


def get_rank(include_faces_card = True):
    if include_faces_card:
        card_rank = random.randint(1, 13)
    else:
        card_rank = random.randint(2, 10)

    if card_rank == 1:
        return "Ace"
    elif card_rank == 11:
        return "Jack"
    elif card_rank == 12:
        return "Queen"
    elif card_rank == 13:
        return "King"
    else:
        return str(card_rank)


def blackjack_player(card):
    rank = card.split()[0]
    if rank in ["Jack","Queen","King"]:
        return 10
    elif rank == "Ace":
        while True:
            try:
                player_value = int(input("Choose value (1 or 11): "))
                if player_value in [1, 11]:
                    return player_value
                else:
                    print("Invalid choice. Please choose 1 or 11.")
            except ValueError:
                print("Please enter a number (1 or 11).")
    else:
        return int(rank)

def blackjack_dealer(card):
    rank = card.split()[0]
    if rank in ["Jack", "Queen", "King"]:
        return 10
    elif rank == "Ace":
        return 11  # Ace is 11 or 1, but for simplicity we return 11 here.
    else:
        return int(rank)


def game():
    while True:
        print("===========\n" +
              "BLACK JACK\n" +
              "===========\n")

        # Dealer's hand calculation
        dealer_hand = draw_hand(2)
        print("---------------------")
        print("Dealer:")
        print("1. ", dealer_hand.splitlines()[0])
        print("2.  **********")
        dealer_total_value = sum([blackjack_dealer(card) for card in dealer_hand.splitlines()])
        print("---------------------\n")

        # Player's hand calculation
        print("You:")
        player_hand = draw_hand(2)
        print(player_hand)
        player_total_value = sum([blackjack_player(card) for card in player_hand.splitlines()])
        print("Your Total Value:", player_total_value)

        # Player's decision loop
        get_player_card = ""
        while player_total_value <= 17:
            player_answer = input('Hit or Stay: ').capitalize()
            if player_answer == "Hit":
                get_player_card = draw_hand(1)
                print(get_player_card)
                player_total_value += blackjack_player(get_player_card)
                if player_total_value >= 21:
                    break
            elif player_answer == "Stay":
                break
            else:
                print("Invalid input, please choose 'Hit' or 'Stay'.")

        # Dealer's decision loop
        get_dealer_card = ""
        while dealer_total_value <= 17:
            if player_total_value > 21:
                break
            get_dealer_card = draw_hand(1)
            dealer_total_value += blackjack_dealer(get_dealer_card)
            if dealer_total_value > 21:
                for card in dealer_hand.splitlines():
                    if card == "Ace":
                        dealer_total_value -= 10
                        break

        print("---------------------\n")
        print("You:")
        print("1. ", player_hand.splitlines()[0])
        print("2. ", player_hand.splitlines()[1])
        print("Your total value:", player_total_value)
        print("---------------------\n")

        print("---------------------\n")
        print("Dealer:")
        print("1. ", dealer_hand.splitlines()[0])
        print("2. ", dealer_hand.splitlines()[1])
        print("3. ", get_dealer_card)
        print("Dealer's total value:", dealer_total_value)
        print("---------------------\n")

        # The Game Result
        if player_total_value == dealer_total_value:
            print("Draw.\n")
        elif dealer_total_value > 21:
            print("You win.\n")
        elif dealer_total_value < player_total_value <= 21:
            if player_total_value == 21:
                print("You win. Black Jack!\n")
        else:
            print("The Dealer wins.\n")

        play_again = input("Would you like to play more? (Yes/No): ").strip().lower()
        if play_again != "yes":
            break
game()
