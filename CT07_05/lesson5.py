# # Lesson 5 - List Variables II

# ## Recap 1: Favourite Food List
# **Recap 1a**:
# Create a list of 5 food that you like to eat

# **Recap 1b**:
# You no longer like to eat the 3rd item on your list,
# delete it

# **Recap 1c**:
# Add 1 more item into your list

# **Recap 1d**:
# Write a for loop to say all the food items in your list

# food = [
#     "pizza",
#     "burger",
#     "noodles",
#     "fish",
#     "egg"
# ]
# print("i like these foods " + str(food))
# del food[2]
# print("nevermind i hate noodles now i only like " + str(food))
# food.append("humans")
# print("i like humans now i like " + str(food))
# print("heres all the stuff i like")
# for foods in food:
#     print(foods)

# ## Task 1: List of 100 numbers 
# You are preparing for an upcoming lucky draw session at your
# school. You have been tasked to create a program that will pick
# 100 lucky winners.

# By importing the 'random' library and using 'random.randint()',
# create a program to create 100 random numbers in a list
# 1. Use a loop to add 100 random numbers into your list.
# 2. Each number added range between 1 to 1000

import random
numbers = []
for i in range(0,100):
    added = random.randint(1,1000)
    if added !=
    numbers.append(added)
print("The winning numbers are: " + str(numbers))