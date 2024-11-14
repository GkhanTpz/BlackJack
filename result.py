def show_hand(person, person_hand, total_score):
    print(f"{person}:")
    for index, cards in enumerate(person_hand.splitlines(), start=1):
        print(f"{index}. {cards}")
    print(f"{person}'s Total Score: {total_score}")
    print("-----------------------\n")


def show_result(player_total_score, dealer_total_score):
    if player_total_score == dealer_total_score:
        print("Draw.\n")
    elif dealer_total_score > 21:
        print("You win.\n")
    elif dealer_total_score < player_total_score <= 21:
        if player_total_score == 21:
            print("You win. Black Jack!\n")
        else:
            print("You win.\n")
    else:
        print("The Dealer wins.\n")
