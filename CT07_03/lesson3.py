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

import time

minutes = int(input("how long u want to study")) * 60

while minutes != 0:
    