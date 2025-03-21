# import packages
from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
    want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if want_to_play == "y":
        print("\n" * 10)
        print(logo)
        try_again = True

        player_cards = random.choices(cards, k=1)
        dealer_cards = random.choices(cards, k=1)
        player_card = random.choice(cards)
        player_cards.append(player_card)
        if player_card == cards[0]:
            if sum(player_cards) > 21:
                player_cards[-1] = 1
        dealer_card = random.choice(cards)
        dealer_cards.append(dealer_card)
        if dealer_card == cards[0]:
            if sum(dealer_cards) > 21:
                dealer_cards[-1] = 1
        if sum(player_cards) == 21:
            print(f"  Your cards: {player_cards}, current score: {sum(player_cards)}")
            print(f"  Computer's first card: {dealer_cards[0]}")
            print(f" Your final hand: {player_cards}, final score: 0")
            print(f" Computer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}")
            print("You win with a Blackjack!")
            try_again = False
            blackjack()
        else:
            print(f"  Your cards: {player_cards}, current score: {sum(player_cards)}")
            print(f"  Computer's first card: {dealer_cards[0]}")
            try_again = True

        while try_again:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if another_card == 'y':
                player_card = random.choice(cards)
                player_cards.append(player_card)
                if player_card == cards[0]:
                    if sum(player_cards) > 21:
                        player_cards[-1] = 1
                if sum(player_cards) > 21:
                    print(f"  Your final hand: {player_cards}, final score: {sum(player_cards)}")
                    print(f"  Computer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}")
                    print("You went over. You lose!")
                    try_again = False
                    blackjack()
                else:
                    print(f"  Your cards: {player_cards}, current score: {sum(player_cards)}")
                    print(f"  Computer's first card: {dealer_cards[0]}")

            elif another_card == "n":
                while sum(dealer_cards) < 17:
                    dealer_card = random.choice(cards)
                    dealer_cards.append(dealer_card)
                    if dealer_card == cards[0]:
                        if sum(dealer_cards) > 21:
                            dealer_cards[-1] = 1
                if sum(dealer_cards) > 21:
                    print(f"  Your final hand: {player_cards}, final score: {sum(player_cards)}")
                    print(f"  Computer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}")
                    print("Opponent went over. You win!")
                    try_again = False
                    blackjack()
                elif sum(dealer_cards) == 21:
                    print(f"  Your final hand: {player_cards}, final score: {sum(player_cards)}")
                    print(f"  Computer's final hand: {dealer_cards}, final score: 0")
                    print("Lose, opponent has Blackjack!")
                    try_again = False
                    blackjack()
                else:
                    if sum(player_cards) > sum(dealer_cards):
                        print(f"  Your final hand: {player_cards}, final score: {sum(player_cards)}")
                        print(f"  Computer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}")
                        print("You win!")
                        try_again = False
                        blackjack()
                    elif sum(player_cards) < sum(dealer_cards):
                        print(f"  Your final hand: {player_cards}, final score: {sum(player_cards)}")
                        print(f"  Computer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}")
                        print("You lose!")
                        try_again = False
                        blackjack()
                    elif sum(player_cards) == sum(dealer_cards):
                        print(f"  Your final hand: {player_cards}, final score: {sum(player_cards)}")
                        print(f"  Computer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}")
                        print("It's a draw")
                        try_again = False
                        blackjack()
    elif want_to_play == "n":
        None
blackjack()
