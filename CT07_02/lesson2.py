
# recap 1

# **Task: write a separate 'for' loop to print the following
# numbers:**
# 1. from 0 - 20
# 2. from 1 to 30
# 3. from 2 to 24 (in even numbers)

# for i in range(2,25,2):
#     print(i)

# # Task 1: Introduction to while loop
# **Task: Using a separate 'while' loop, print each of the
# following:**
# 1. from 0 to 20
# 2. from 1 to 30
# 3. from 2 to 24

# skibidi = 2
# while skibidi <= 24:
#     print(skibidi)
#     skibidi+=1

# ## Task 2: while... break
# The **break** keyword will **break** out (exit) the loop.
# When a **break** is encountered, the code in the **else** will
# not be run.

# Using a while loop:
# 1. print the numbers from 1 to 10
# 2. if the number is 5, **break** out of the loop

# counter = 1
# while True:
#     print(counter)
#     counter+=1
#     if counter > 5:
#         break

# ## Task 3: while... else
# The else condition will run when the loop exits normally
# i.e. when the while condition is no longer true.

# **Task 3a**: Using a while loop
# 1. print the numbers from 1 to 10
# 2. once count has reached 10, use the else and print "Count
#    has reached 10"

# **Task 3b**:
# Now, modify your 'while' loop such that:
# 1. If the number is 5, **break** out of the loop
# 2. Ensure your code has an else

# Observe if the code in the **else** runs.

# counter = 0
# while counter < 10:
#     if counter == 5:
#         break
#     else:
#         counter+=1
#         print(counter)

# ## Task 4: Ordering Pizzas with while loop
# **Task: Using what you have learned above, code a program to
# take a customer's order for pizza.
# Declare a variable called _topping_.**

# Using a while loop:
# 1. Ask the user to enter a choice of topping
# 2. For each topping entered, concatenate to the 'topping'
#    variable
# 3. exit the while loop if the user enters "end"
# 4. On program end, print out the toppings that the customer
#    has chosen.

# topping = ""
# toppinglist = ""
# while True:
#     if topping == "end, ":
#         print("Your toppings are: " + toppinglist)
#         break
#     else:
#         toppinglist+=topping
#         topping = input("Please add topping of choise to pissa: ") + ", "

# ## Task 5: General Knowledge Quiz
# **Task: Create a program to quiz users on their general
# knowledge**

# Using the while loop, ask 3 general knowledge questions
# 1. Using input ask the question
# 2. While answer is not correct, repeat the question.
# 3. Move on to the next question when the answer is correct

# Bonus:
# 1. Add a score system
# 2. Add an ability for users to skip by saying “skip”
# 3. Disqualify user when they have tried too many times

# ans1 = "nothing"
# ans2 = 2
# ans3 = "school"
# counter = 0
# print("Welcome to the Game Show! You will answer 3 questions and answer all 3 correctly, you get a million vietnamese dong")
# while True:
#     if counter == 3:
#         print("Youve used up all your 3 attempts! Your disqualified!")
#         break
#     ansans1 = input("Lets start! What happened to the Tiananmen Square in 1989? ")
#     if ansans1 != ans1:
#         print("Wrong! Try again.")
#         counter+=1
#     else:
#         print("Correct! Nothing happened to the Tiananmen Square in 1989. Next question!")
#         counter=0
#     ansans2 = int(input("What is ( ( ( (16)^(1/3) - log2(64) + 8 * (2^4 / 2^2) )^(1/2) + (asin(0.5) / pi) ) / ( ( (3 + (7/2))^2 / (log(1000) - log(100)) )^(1/2) + (16)^(1/4) ) ) * 2? "))
#     if ansans2 != ans2:
#         print("Wrong! Try again.")
#         counter+=1
#     else:
#         print("Correct! The answer is 2. Final question!")
#         counter=0
#     ansans3 = input("It is a house. Someone goes in blind, but comes out seeing. What is the house? ")
#     if ansans3 != ans3:
#         print("Wrong! Try again.")
#         counter+=1
#     else:
#         print("Correct! Youve won the gameshow! You get a million vietnamese dong ok now go buy mcdonalds or something")
#         break
    

ans1 = "nothing"
ans2 = 2
ans3 = "school"
counter = 0

print("Welcome to the Game Show! You will answer 3 questions and if you answer all 3 correctly, you get a million Vietnamese dong!")

while True:
    if counter == 3:
        print("You've used up all your 3 attempts! You're disqualified!")
        break
    
    ansans1 = input("Let's start! What happened to Tiananmen Square in 1989? ")
    while ansans1 != ans1:
        print("Wrong! Try again.")
        counter += 1
        ansans1 = input("Let's start! What happened to Tiananmen Square in 1989? ")
    print("Correct! Nothing happened to Tiananmen Square in 1989. Next question!")
    counter = 0
    
    if counter < 3:
        ansans2 = int(input("What is ( ( ( (16)^(1/3) - log2(64) + 8 * (2^4 / 2^2) )^(1/2) + (asin(0.5) / pi) ) / ( ( (3 + (7/2))^2 / (log(1000) - log(100)) )^(1/2) + (16)^(1/4) ) ) * 2? "))
        while ansans2 != ans2:
            print("Wrong! Try again.")
            counter += 1
            ansans2 = int(input("What is ( ( ( (16)^(1/3) - log2(64) + 8 * (2^4 / 2^2) )^(1/2) + (asin(0.5) / pi) ) / ( ( (3 + (7/2))^2 / (log(1000) - log(100)) )^(1/2) + (16)^(1/4) ) ) * 2? "))
        print("Correct! The answer is 2. Final question!")
        counter = 0
    
    if counter < 3:
        ansans3 = input("It is a house. Someone goes in blind, but comes out seeing. What is the house? ")
        while ansans3 != ans3:
            print("Wrong! Try again.")
            counter += 1
            ansans3 = input("It is a house. Someone goes in blind, but comes out seeing. What is the house? ")
        print("Correct! Youve won the gameshow! You get a million vietnamese dong ok now go buy mcdonalds or something")
        break