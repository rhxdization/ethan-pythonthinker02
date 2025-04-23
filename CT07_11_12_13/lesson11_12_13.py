# [
#     ['X', ' ', ' ']
#     [' ', ' ', 'O']
#     [' ', ' ', ' ']
# ]

# create a data structure to hold this values
# nested list

def initboard():
    global row
    global board
    board = []

    # outer loop
    for i in range(3):

        row = [] # create empty row
        for j in range(3): # loop through 3 times to create individual cell
            row.append(" ") # 1 cell by 1 cell
        board.append(row)

    return board # return the board

def printboard(argboard):
    count = 1
    for row in argboard:
        for col in row:
            if col == " ":
                print(f"| {count} ", end="")
            else:
                print(f"| {col} ", end="")

            if count % 3 ==0: # help to calculate that this is a new row
                print("|")
                print("-"*13)
            count += 1

#### let the player choose a move
def get_player_move(argboard, currentplayer):
    global cell
    while True:
        # asking player to enter a number 1 - 9
        move = input(f"Player {currentplayer}, Enter a number from 1 - 9: ")

        # validation first
        if move.isdigit(): # checking for numbers...
            move = int(move)
            if move >= 1 and move <= 9:
                move = move - 1 # zero based index
                row = move // 3 # return row number
                col = move % 3 # return the col
                print(f"row = {row}, col = {col}")

                # check if this particular cell is empty
                cell = argboard[row][col]
                if cell == " ":
                    argboard[row][col] = currentplayer#"X"
                    break
                else:
                    print(f"{move+1} is already taken. Choose another")

                # pass # i will write some code later
            else:
                print("psl enter number")
        else:
            print("pls enter number")
    return argboard # the move has been made, return the board

# another function for get current player
def getcurrentplayer(player):
    if player == "X":
        return "Q" 
    else:
        return "X"

#### a function to check that you have won
def checkwin(argboard):
    win = [
        # row 1 to row 3
        [ argboard[0][0], argboard[0][1], argboard[0][2] ], # row 1
        [ argboard[1][0], argboard[1][1], argboard[1][2] ], # row 2
        [ argboard[2][0], argboard[2][1], argboard[2][2] ], # row 3

        # col 1 to col 3
        [ argboard[0][0], argboard[1][0], argboard[2][0] ], # col 1
        [ argboard[0][1], argboard[1][1], argboard[2][1] ], # col 2
        [ argboard[0][2], argboard[1][2], argboard[2][2] ], # col 3

        # diagonal 1 and 2
        [ argboard[0][0], argboard[1][1], argboard[2][2] ], # diagonal 1
        [ argboard[0][2], argboard[1][1], argboard[2][0] ], # diagonal 2
    ]

    # loop through the win condition
    for condition in win:
        if condition[0] == condition[1]  == condition[2] and condition[0] != " ":
            return True
    return False

def boardfull(board):
    if board in row:
        if row in cell:
            if cell == ' ':
                return False
            else:
                return True



# main game code
board = initboard()
cplayer = ""

while True:
    printboard(board)

    # get current player
    cplayer = getcurrentplayer(cplayer)
    
    board = get_player_move(board, cplayer)

    if checkwin(board):
        print("*"*20)
        print(f"Player {cplayer} Wins!! ")
        print("*"*20)
        printboard(board)
        break
    if not(checkwin(board)) and boardfull(board):
        print("*"*20)
        print("Tie")
        print("*"*20)
        printboard(board)
        break
