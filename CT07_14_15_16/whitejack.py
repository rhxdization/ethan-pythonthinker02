import random
import time

suits = ["♣ Clubs", "♦ Diamonds","❤  Hearts","♠ Spades"]
ranks = ['2','3','4','5','6','7','8','9','Jack','Queen','King','Ace']

# Step 1: Create the deck of cards
# Create a dictionary to store the value of each card rank
# Cards 2–10 are worth their face value, J, Q, K are worth 10, 
# and Ace can be 1 or 11
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
'Jack':10, 'Queen':10,'King':10, 'Ace':11}

# variable to store your deck
deck = []
player_hand = []
banker_hand = []

# build the deck
for suit in suits:
    for rank in ranks:
        deck.append([suit, rank])

# shuffle the deck
for i in range(10):
    random.shuffle(deck)

# draw out a card
banker_hand = [deck.pop(), deck.pop()]
player_hand = [deck.pop(), deck.pop()]

# function w 1 parameter (hand) to calculate score of hand
def calculate(hand):
    points = 0
    count_aces = 0
    for card in hand:
        cardvalue = values[card[1]]
        points += cardvalue
        if card[1] == "Ace":
            count_aces += 1
    while points > 21 and count_aces > 0:
        points -= 10
        count_aces -= 1
    return points

# function w 2 parameters (hand, typeofhand (banker_h, player_s, banker_s)) to show hand
def show_hand(hand, typeofhand):
    if typeofhand == "player_s":
        print("😀"*10)
        print("Player Hand")
        for card in hand:
            print(f" {card[1]} {card[0]}")
            calculate(player_hand)
        print(f"You have {calculate(player_hand)} points")
        print("😀"*10)
    elif typeofhand == "banker_h":
        print("😈" * 10)
        print("Banker Hand")
        print(f" {hand[0][1]} {hand[0][0]}\n {"? ? " * 3}")
        print("😈" * 10)
        print("\n")
    elif typeofhand == "banker_s":
        print("😈"*10)
        print("Banker Hand")
        for card in hand:
            print(f" {card[1]} {card[0]}")
            calculate(banker_hand)
        print(f"Banker has {calculate(banker_hand)} points")
        print("😈"*10)
# main game loop
while True:
    show_hand(player_hand, "player_s")
    show_hand(banker_hand, "banker_h")

    # check if player whitejack
    if calculate(player_hand) == 21:
        print("You win! Whitejack!")
        break
    else:
        action = input("1 to hit, 2 to check. ")
        if action == "1":
            player_hand.append(deck.pop())
            if calculate(player_hand) > 21:
                show_hand(player_hand, "player_s")
                show_hand(player_hand, "banker_h")
                print("imagine busting in the big 25")
                print("you lose")
                break
        elif action == "2":
            print("Banker is thinking...")
            print("\n")
            time.sleep(1)
            while calculate(banker_hand) <= 17:
                banker_hand.append(deck.pop())
                show_hand(player_hand, "player_s")
                show_hand(banker_hand, "banker_s")
                print("\n")
                if calculate(banker_hand) > 21:
                    print("Banker busted!")
                    print("You win!")
                    break
                elif calculate(banker_hand) > calculate(player_hand):
                    print("imagine losing to the banker")
                    print("you lose")
                    break
                elif calculate(banker_hand) == calculate(player_hand):
                    print("push")
                    print("its a tie")
                    break
                elif calculate(banker_hand) < calculate(player_hand):
                    print("You scored more points!")
                    print("You win!")
                    break
                print(banker_hand)
                time.sleep(1)
            break