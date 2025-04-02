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

board = []

for i in range(3):
    row = []
    for j in range(3):
        row.append(" ")
    board.append(row)

print(board)