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

# ## Task 2: List of 100 unique numbers
# The program you have created from the previous task will
# sometimes generate duplicate numbers. Modify your program so
# that the 100 numbers generated are all unique.

# Modify your program from the previous task to create 100 random
# unique numbers in a list.
# 1. Use a loop to add 100 random numbers into your list.
# 2. Each number added range between 1 to 1000
# 3. Ensure that all the numbers are unique
# 4. Print the list of 100 unique numbers created

# Hint: Use a while loop to check if the number already exists in
# the loop

# import random
# numbers = []
# for i in range(0,100):
#     added = random.randint(1,1000)
#     if added not in numbers:
#         numbers.append(added)
# print("The winning numbers are: " + str(numbers))

# ## Task 3: Score Taker
# Imagine the list that you have created in Task 2 represent the
# score of a 100 students.

# Find the maximum, minimum and average from the list.

# 1. Using the 'max()' function, find the maximum score.
# 2. Using the 'min()' function, find the minimum score.
# 3. Using the 'sum()' and 'len()' function, calculate the
#    average score.

# import random
# numbers = []
# for i in range(0,100):
#     added = random.randint(1,1000)
#     if added not in numbers:
#         numbers.append(added)
# for i in numbers:
#     print(i)
# print("average score is " + str(sum(numbers) / len(numbers)))
# print("biggest score is " + str(max(numbers)))
# print("smallest score is " + str(min(numbers)))

# ## Task 4: Who is the tallest?
# Task: You are given 2 lists, 
# **namelist** contains a list of students in your class
# **heightlist** contains a list of the corresponding student's
#                height

# 1. Determine who is the tallest in class, and what is his/ her
#    name
# 2. Determine who is the shortest in class, and what is his/ her
#    name

# Hint: use .index("value of something in the list") to find the index
# of an item

# namelist = ["Olivia", "Liam", "Emma", "Noah", "Ava", "your mom",
#             "Sophia", "Lucas", "Mia", "Aiden"
#             ]
# heightlist = [160, 165, 158, 170, 162, 669, 159, 172, 164, 166]

# tallest = max(heightlist)
# shortest = min(heightlist)
# tallest_name = heightlist.index(tallest)
# shortest_name = heightlist.index(shortest)
# print("The tallest person in our class is " + namelist[tallest_name] + " at " + str(tallest) + "cm")
# print("The tallest person in our class is " + namelist[shortest_name] + " at " + str(shortest) + "cm")

# ## Task 5: Pokemon, I choose you!
# Task: You are given 2 lists,
# **pokemons** contains a list of pokemons
# **powers** contains a list of the corresponding pokemon's
#            powers

# 1. Choose 2 random pokemons from the list
# 2. Compare the powers of the 2 pokemons
# 3. Calculate who is the winner of the fight between these 2
#    pokemons
#    (pokemon with the higher power will always win)

import random
import time
pokemons = [
    "Pikachu", "Charizard", "Bulbasaur", "Squirtle",
    "Jigglypuff", "Meowth", "Psyduck", "Eevee", "Snorlax",
    "Mewtwo", "Lapras", "Gengar", "Dragonite", "Machamp",
    "Arcanine", "Alakazam", "Gyarados", "Vaporeon", "Scyther",
    "Electabuzz"
]
powers = []
for i in range(0,20):
    select = random.randint(1,200)
    if select not in powers:
        powers.append(select)
p1_pokemon = random.choice(pokemons)
p2_pokemon = random.choice(pokemons)
while p2_pokemon == p1_pokemon:
    p2_pokemon = random.choice(pokemons)
p1_index = pokemons.index(p1_pokemon)
p2_index = pokemons.index(p2_pokemon)
p1_power = powers[p1_index]
p2_power = powers[p2_index]

print("Welcome to the Squid Games- I meant Pokemon Games!")
print("Today we have 2 contestants, *insert player 1 name* and *insert player 2 name*!")
print("Player 1's pokemon is " + p1_pokemon + " with a power of " + str(p1_power) + "!")
print("Player 2's pokemon is " + p2_pokemon + " with a power of " + str(p2_power) + "!")
