
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

ans1 = "nothing"
ans2 = 2
ans3 = "school"
counter = 0
score = 0
scoreearned = 5
questionskip = 0

print("Welcome to the Game Show! In this game, if you get 10 points, you will earn 1 million Vietnamese Dong!")

while True:
    ansans1 = input("Let's start! What happened to Tiananmen Square in 1989? ")
    while ansans1 != ans1:
        print("Wrong! Try again.")
        counter += 1
        scoreearned-=2
        if counter == 3:
            print("You've used up all your 3 attempts! You're disqualified!")
            break
        ansans1 = input("What happened to Tiananmen Square in 1989? ")
    if counter == 3:
        break   
    else:
        print("Correct! Nothing happened to Tiananmen Square in 1989. Next question!")
        score+=scoreearned
    counter = 0
    scoreearned=5
    ansans2 = int(input("What is ( ( ( (16)^(1/3) - log2(64) + 8 * (2^4 / 2^2) )^(1/2) + (asin(0.5) / pi) ) / ( ( (3 + (7/2))^2 / (log(1000) - log(100)) )^(1/2) + (16)^(1/4) ) ) * 2? "))
    while ansans2 != ans2:
        print("Wrong! Try again.")
        counter += 1
        scoreearned-=2
        if counter == 3:
            print("You've used up all your 3 attempts! You're disqualified!")
            break
        ansans2 = int(input("What is ( ( ( (16)^(1/3) - log2(64) + 8 * (2^4 / 2^2) )^(1/2) + (asin(0.5) / pi) ) / ( ( (3 + (7/2))^2 / (log(1000) - log(100)) )^(1/2) + (16)^(1/4) ) ) * 2? "))
    if counter == 3:
        break   
    else:
        print("Correct! The answer is 2. Final question!")
        score+=scoreearned
    counter = 0
    scoreearned=5
    ansans3 = input("It is a house. Someone goes in blind, but comes out seeing. What is the house? ")
    while ansans3 != ans3:
        print("Wrong! Try again.")
        counter += 1
        scoreearned-=2
        if counter == 3:
            print("You've used up all your 3 attempts! You're disqualified!")
            break
        ansans3 = input("It is a house. Someone goes in blind, but comes out seeing. What is the house? ")
    if counter == 3:
        break   
    else:
        print("Correct! The answer is a school. Now lets check if youve scored enough...")
        score+=scoreearned
        counter=0
        scoreeearned=5
        if score >= 10:
            print("Congrats! Youve won 1 million Vietnamese Dong! ok now go buy mcdonalds or smth (Score: " + str(score) + ")")
        else:
            print("Sorry, you lost! your score: " +str(score) + ". Better luck next time!")
        break

# # Define my variables
# max_attempts = 3
# score = 0

# questions_answers = [
#     "qn1?", "ans1",
#     "qn2?", "ans2", 
#     "qn3?", "ans3"
# ]

# for i in range(0, len(questions_answers), 2):
#     question = questions_answers[i]
#     answer = questions_answers[i + 1]
#     attempts = 0

#     while attempts < max_attempts:
#         user_input = input(question)
        
#         if user_input.lower() == answer.lower():
#             score += 1
#             print("Correct!")
#             break
#         elif user_input.lower() == "skip":
#             print("Question skipped.")
#             break
#         else:
#             print("Wrong!")
#             attempts += 1

#         if attempts == max_attempts:
#             print("Too many attempts! Try the next question.")

# print(f"Your final score is {score} out of {len(questions_answers) // 2}.")