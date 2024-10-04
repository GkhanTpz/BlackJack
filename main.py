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
        player_value = int(input("Choose value (1 or 11): "))
        if player_value == 1:
            return 1
        elif player_value == 11:
            return 11
        else:
            print("Wrong value. Choose right.")
            while player_value != 1 or player_value != 11:
                player_value = int(input("Choose value (1 or 11): "))
                return player_value
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
    print("===========\n" +
          "BLACK JACK\n" +
          "===========\n")

    # Calculating The Dealer's hand value for blackjack
    while True:
        dealer_hand = draw_hand(2)
        if dealer_hand.splitlines()[0] != "Ace":
            break
        elif dealer_hand.splitlines()[1] == "Ace":
            continue

    print("---------------------")
    print("Dealer:")
    print("1. ", dealer_hand.splitlines()[0])
    print("2.  **********")
    dealer_total_value = sum([blackjack_dealer(card) for card in dealer_hand.splitlines()])
    print("---------------------\n")

    # Calculating Player's hand value for blackjack
    print("You:")
    player_hand = draw_hand(2)
    print(player_hand)
    player_total_value = sum([blackjack_player(card) for card in player_hand.splitlines()])
    print("Your Total Value:",player_total_value)

    # Player gets New Card
    get_player_card = ""
    while player_total_value <= 17:
        player_answer = input('Hit or Stay: ')
        if player_answer == "Hit":
            get_player_card = draw_hand(1)
            player_total_value += blackjack_player(get_player_card)
            if player_total_value >= 21:
                break
        else:
            break
    print("---------------------\n")
    print("You:")
    print("1. ", player_hand.splitlines()[0])
    print("2. ", player_hand.splitlines()[1])
    print("3. ", get_player_card)
    print("Your total value:", player_total_value)
    print("---------------------\n")

    #The Dealer gets New Card
    get_dealer_card = ""
    while dealer_total_value <= 17:
        get_dealer_card = draw_hand(1)
        dealer_total_value += blackjack_dealer(get_dealer_card)
        if dealer_total_value >= 21:
            break

    print("---------------------\n")
    print("Dealer:")
    print("1. ", dealer_hand.splitlines()[0])
    print("2. ", dealer_hand.splitlines()[1])
    print("3. ", get_dealer_card)
    print("Dealer's total value:", dealer_total_value)
    print("---------------------\n")

    # The Game Result
    if player_total_value == dealer_total_value:
        print("Draw.")
    elif player_total_value > dealer_total_value or dealer_total_value >21:
        if player_total_value == 21:
            print("You win. Black Jack!")
        else:
            print("You Win.")
    else:
        print("The Dealer wins")

game()
