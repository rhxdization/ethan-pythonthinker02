# ## Recap 1: Riddler
# **Task: Using a while loop, code a riddler program**
# 1. Think of a riddle
# 2. Using the while loop, ask the user the riddle and
#    check the answer
# 3. While answer is not correct, repeat the question

# ans = "2"
# riddle = "( ( ( (16)^(1/3) - log2(64) + 8 * (2^4 / 2^2) )^(1/2) + (asin(0.5) / pi) ) / ( ( (3 + (7/2))^2 / (log(1000) - log(100)) )^(1/2) + (16)^(1/4) ) ) * 2 is what "

# userinput = input(riddle)
# while userinput != ans:
#     print("no.")
#     userinput = input(riddle)

# print("ok you pass")

# ## Task 1: Study Timer
# **Task: Write a program that acts as a study timer**
# 1. The user must input how many minutes they plan to study
# 2. Use a while loop to count down the minutes
# 3. Display "Good job!" once the timer is up

# Hint: you will need the time.sleep(). However this function
# only takes in seconds.
# You will need to write a conversion algorithm to change
# minutes to seconds.

# import time

# timer = int(input("how long u want to study (minutes) ")) * 60

# while timer != 0:
#     time.sleep(1)
#     if (timer % 60) == 0:
#         print(str(timer/60) + " minutes left")
#     timer-=1

# print("good job")

# ## Task 2: Allowance Savings Tracker
# **Task: Write a program to track how much you save, and
# inform you when your savings is more than $100**
# 1. Create a variable called savings
# 2. Using a while loop, ask how much money you save every
#    day
# 3. While savings is less than 100, you continue to save
# 4. Exit the program when savings is more than 100 and
#    congratulate the user.

# savings = 0.0
# while savings < 100:
#     savings += float(input("How much did you save today? "))
#     print("You now have $" + str(savings) + ".")
# print("You saved $100 or more. ($" + str(savings) + ") Congrats!")

# ## Task 3: Multiplication Quiz
# **Task: Ms Tan, your math teacher knows that you are a
# programming whiz,
# she has asked you to help code a multiplication quiz for
# the class to practice.**

# Here are her requirements:
# 1. Students have to answer 15 questions in total
# 2. Students have 3 lives (chances). i.e. they can get the
#    question wrong 3 times.
# 3. The questions will be in this format: "What is 3 x 19? ". 
# 4. The numbers for each question will be randomly generated
#    and between the range of 2 to 20.
# 5. If the student answers correctly, move on to the next
#    question
# 6. If the student answers wrongly, minus 1 life, and ask
#     the question again.
# 7. If the student has no more lives, exit and print
#     "GO AND SEE MS TAN FOR REMEDIAL"

import random
questions = 15
lives = 3
questionno = 1
ans = 0
no1 = random.randint(2,20)
no2 = random.randint(2,20)
print("hi ms tan told me to give tihs to you so uhh suffer")
while questionno != (questions+1):
    ans = int(input("question " + str(questionno) + ": what is " + str(no1) + " * " + str(no2) + "? "))
    if ans != (no1*no2):
        print("WRONG 👿👿👿")
        lives -= 1
    else:
        print("ok good")
        no1 = random.randint(2,20)
        no2 = random.randint(2,20)
        questionno += 1
    if lives == 0:
        print("GO AND MEET TEACHER IN DETENTION ROOM 😡😡😡😡😡😡🤬🤬🤬")
        break
if lives != 0:  
    print("you passed... for now 😈😈")