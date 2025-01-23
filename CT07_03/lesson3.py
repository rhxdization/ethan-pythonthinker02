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

savings = 0
while savings < 100:
    savings += int(input("How much did you save today? "))
    