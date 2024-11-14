import random


def draw_hand(number, include_faces_card=True):
    hand = ""
    for card in range(number):
        hand += draw_card(include_faces_card) + "\n"
    return hand


def draw_card(include_faces_card=True):
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


def get_rank(include_faces_card=True):
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