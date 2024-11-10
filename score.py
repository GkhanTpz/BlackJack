import blackjack
import dealer
import player


def calculate_hand(person, card_count, is_dealer = False):
    hand = blackjack.draw_hand(card_count)
    total_score = 0
    if is_dealer:
        print(f"{person}:")
        print("1. ", hand.splitlines()[0])
        print("2.  **********")
        total_score = sum([dealer.dealer_hand(card) for card in hand.splitlines()])
        print("---------------------\n")
    else:
        print(f"{person}:")
        for index, card in enumerate(hand.splitlines(), start = 1):
            print(f"{index}. {card}")
        total_score = sum([player.player_hand(card) for card in hand.splitlines()])
        print(f"Your Total Score: {total_score}")
        print("---------------------\n")

    return hand, total_score