def player_hand(cards):
    rank = cards.split()[0]
    if rank in ["Jack", "Queen", "King"]:
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