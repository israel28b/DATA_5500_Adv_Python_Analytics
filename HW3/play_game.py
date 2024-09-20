from DeckOfCards import Card, DeckOfCards, calculate_hand_value



# Main game loop
while True:
    print("Welcome to Blackjack!")
    choice = input("Do you want to play? (yes/no): ").lower()

    if choice == 'no':
        print("Goodbye!")
        break

    while choice == 'yes':
        deck = DeckOfCards()

        print("\nDeck before shuffling:")
        deck.print_deck()  # Display deck before shuffle

        deck.shuffle_deck()

        print("\nDeck after shuffling:")
        deck.print_deck()  # Display deck after shuffle

        player_hand = []
        dealer_hand = []

        player_hand.append(deck.get_card())
        dealer_hand.append(deck.get_card())
        player_hand.append(deck.get_card())
        dealer_hand.append(deck.get_card())

        print("\nDealing...")
        print("Your cards:")
        for card in player_hand:
            print(card)

        player_hand_value = calculate_hand_value(player_hand)
        dealer_hand_value = dealer_hand[0].val  
        print(f"Your hand value: {player_hand_value}")

        print("Dealer's cards:")
        print(dealer_hand[0])  
        print("Hidden card")

        # Player's turn
        while player_hand_value < 21:
            choice = input("\nDo you want to hit or stand? (hit/stand): ").lower()

            if choice == 'hit':
                player_hand.append(deck.get_card())
                print("\nYour cards:")
                for card in player_hand:
                    print(card)

                player_hand_value = calculate_hand_value(player_hand)
                print(f"Your hand value: {player_hand_value}")

                if player_hand_value > 21:
                    print("You bust!")
                    break

            elif choice == 'stand':
                break

        # Dealer's turn (dealer hits until hand value is at least 17)
        if player_hand_value <= 21:
            print("\nDealer's cards:")
            for card in dealer_hand:
                print(card)
            dealer_hand_value = calculate_hand_value(dealer_hand)
            print(f"Dealer's hand value: {dealer_hand_value}")

            while dealer_hand_value < 17:
                dealer_hand.append(deck.get_card())
                dealer_hand_value = calculate_hand_value(dealer_hand)
                print("\nDealer hits...")
                print("Dealer's cards:")
                for card in dealer_hand:
                    print(card)
                print(f"Dealer's hand value: {dealer_hand_value}")

            # Determine the outcome
            if dealer_hand_value > 21:
                print("Dealer busts! You win!")
            elif player_hand_value > dealer_hand_value:
                print("You win!")
            elif player_hand_value < dealer_hand_value:
                print("You lose!")
            else:
                print("It's a tie!")

        choice = input("\nDo you want to play again? (yes/no): ").lower()
        if choice == 'no':
            print("Goodbye!")
            break