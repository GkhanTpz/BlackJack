def dealer_hand(card):
    rank = card.split()[0]
    if rank in ["Jack", "Queen", "King"]:
        return 10
    elif rank == "Ace":
        return 11  # Ace is 11 or 1, but for simplicity we return 11 here.
    else:
        return int(rank)