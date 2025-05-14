import random

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
    global points
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

# function w 2 parameters (hand, typeofhand (banker_h, player_s)) to show hand
def show_hand(hand, typeofhand):
    if typeofhand == "player_s":
        print("😀"*10)
        print("Player Hand")
        for card in hand:
            print(f" {card[1]} {card[0]}")
            calculate(player_hand)
        print(f"You have {points} points")
        print("😀"*10)
    elif typeofhand == "banker_h":
        print("😈" * 10)
        print("Banker Hand")
        print(f" {hand[0][1]} {hand[0][0]}\n {"? ? " * 3}")
        print("😈" * 10)
    print("\n")

# main game loop
while True:
    show_hand(player_hand, "player_s")
    show_hand(player_hand, "banker_h")

    # check if player whitejack
    if calculate(player_hand) == 21:
        print("You win! Whitejack!")
        break
    else:
        action = input("1 to hit, 2 to check. ")
        if action == "1":
            player_hand.append(deck.pop())
            if points > 21:
                print("imagine busting in the big 25")
                print("you lose")
                break
        