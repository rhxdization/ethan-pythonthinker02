'''
Have you played Wordle before? Try it out here >> Wordle - The New York Times (nytimes.com)

In this assignment, you are given a text file containing 5757 5-letter words. 

In this assignment, your task is to create a program that works like wordle. Your program will:

1. Choose a random word from the list

2. Allow you to input a 5-letter word

3. Validate if you have you have the letter in the correct position, correct letter but in the wrong position, or the wrong letter.

4. You can use the console output to print out the statements
'''
import random
#r - read, w - write, a - append

# write a function to ask for input, i will validate
# 5 letter word, alphabet, countercheck againts my list of words
def getword(wordlist):

    while True:
        guess = input("Guess a 5-letter word? ")
        if len(guess) == 5:
            if guess.isalpha():
                if guess in wordlist:
                    return guess.upper() ### this must be a legit guess
                else:
                    print("You must type a real word lah!")
            else:
                print("Eh, only letters leh.")
        else:
            print("It must be a 5-letter word!")


with open("ListOf5LetterWords.csv","r") as fileobj:

    contents = fileobj.read() # reads the entire contents > store in string

    # split the words into items in a list
    wordlist = contents.split(",")
    
    # choose a random word from the list
    wordle = random.choice(wordlist).upper()

# need to handle multiple letters
# wordle = "ROSES"
# print(wordle)
for chance in range(1, 7):
    checkguess = getword(wordlist)
    checkdupe = list(wordle) # change to list for dupe checking
    display_check = ""

    for i in range(len(wordle)): # pulling out the index

        # i check if correct letter in same position, check dupe
        if checkguess[i] == wordle[i]:
            display_check = display_check + checkguess[i]
        
        # i check if correct letter but wrong position, check dupe
        elif checkguess[i] in wordle:
            display_check = display_check + "?"

        else:
            display_check = display_check + "#"

    print("")
    print(f"Attempt #: {chance}")
    print(f"You guess: {checkguess}")
    print(f"Result   : {display_check}")

    # handle if you got it.
    if checkguess == wordle:
        print("You are right!")
        print(f"{checkguess} is the answer!")
        break

else:
    # if code comes here, means failed to guess 
    print("Boo hoo... You did not guess it.")
    print(f"The actual word was {wordle}")


