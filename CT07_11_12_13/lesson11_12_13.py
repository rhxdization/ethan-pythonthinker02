# ## Recap 1: diceGuess function
# Create a function named 'diceGuess' with in 1 parameter,
# 'guess' (an integer between 1 and 6). The function returns True
# if the guess matches a randomly generated number between 1 and
# 6, and False otherwise.

# 1. Import 'random' library
# 2. Define 'diceGuess' function with 1 parameter, 'guess'
#         a. Using '.randint()', create and assign the
#            'random_number' variable a random number between 1
#            and 6
#         b. Using 'return', return the boolean value of
#            'guess == random_number'

# Usage example:
# if diceGuess(5):
#     print("Correct!")
# else:
#     print("Incorrect.")

# import random

# def diceguess(guess):
#     a = random.randint(1,6)
#     if a == guess:
#         return True
    
# if diceguess(4):
#     print("✅")
# else:
#     print("❌")

# 
def initboard():
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(" ")
        board.append(row)
    return board



def printboard(argboard):
    # global board
    count = 1
    for row in argboard:
        for col in row:
            if count % 3 == 0:
                print(f"| {count} |", end="\n")
                print("-"*13)
            else:
                # if this cell is empty
                if col == " ":
                    print(f"| {count} ", end="")
                else:
                    print(f"| {col} ", end="")
            count += 1

def get_player_move(argboard):
    global move
   
    while True:
        move = input("pick a number from 1-9: ")
        if move.isnumeric():
            move = int(move)
            move -= 1
            row = move // 3
            col = move % 3
            if move > 9 or move < 0:
                print("your input sucks ngl get better lmaoooooo")
            else:
                if argboard[row][col] == " ":
                    argboard[row][col] == "X"
                    break
                else:
                    print(f"nevemind {move} is already taken your input sucks still")
        else:
            print("your input sucks ngl get better lmaoooooo")
        # print(f"row = {row}, col = {col}")
        # print("finally bro actually put an actual number 😭🙏")
    return argboard

board = initboard()

while True:
    printboard(board)
    board = get_player_move(board)

