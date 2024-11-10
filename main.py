import blackjack
import dealer
import player
import result
import score

while True:
    print("===========\n" +
        "BLACK JACK\n" +
        "===========\n")

    # Dealer's hand calculation
    dealer_hand, dealer_total_score = score.calculate_hand("Dealer", 2, True)

    # Player's hand calculation
    player_hand, player_total_score = score.calculate_hand("You", 2)

    # Player's decision loop
    get_player_card = ""
    while player_total_score <= 17:
        player_answer = input('Hit or Stay: ').capitalize()
        if player_answer == "Hit":
            get_player_card = blackjack.draw_hand(1)
            print(get_player_card)
            player_total_score += player.player_hand(get_player_card)
            if player_total_score >= 21:
                break
        elif player_answer == "Stay":
            break
        else:
            print("Invalid input, please choose 'Hit' or 'Stay'.")

    # Dealer's decision loop
    get_dealer_card = ""
    while dealer_total_score <= 17:
        if player_total_score > 21:
            break
        get_dealer_card = blackjack.draw_hand(1)
        dealer_total_score += dealer.dealer_hand(get_dealer_card)
        if dealer_total_score > 21:
            for card in dealer_hand.splitlines():
                if card == "Ace":
                    dealer_total_score -= 10
                    break

    # Player's Result
    result.print_hand("You", player_hand, player_total_score)

    # The Dealer's Result
    result.print_hand("Dealer", dealer_hand, dealer_total_score)

    # The Game Result
    result.print_result(player_total_score, dealer_total_score)

    # Play Again!
    play_again = input('Would you like to play more? (Yes/No): ').capitalize()
    if play_again != "Yes":
        break

