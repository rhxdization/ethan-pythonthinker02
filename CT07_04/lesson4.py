import time
import random

# ## Recap 1: While Loop
# Task: Code a New Year Countdown timer. 
# Example: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, HAPPY NEW YEAR!

# 1. The countdown timer will count one by one and stop at 1.
# 2. After 1, the program will say Happy New Year
# 3. Use the time library to pause 1 seconds between each
#    number

# counter = 10
# while counter != 0:
#     print(counter)
#     counter -= 1
#     time.sleep(1)
# else:
#     print("happy new year")

# ## Task 1: List of planets
# **Task: Create a list of 8 planets in the solar system**

# **Task 1a**:
# Create a list of 8 planets in the solar system.
# (Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune)

# **Task 1b**:
# You have conquered Mars, **rename** Mars to a name of
# your liking

# **Task 1c**:
# 1. You have decided Pluto is a planet again, **add** Pluto
#    into the list
# 2. You created an artificial planet between Earth and
#    Mars called "Lalaland". **Insert** the planet in
#    correctly into the list.

# **Task 1d**:
# You launched a war againts Jupiter and destroyed it,
# **delete** Jupiter from the list

# counter = 0
# planets =[
#     "mercury",
#     "venus",
#     "earth",
#     "mars",
#     "jupiter",
#     "saturn",
#     "uranus",
#     "neptune"
# ]
# print("here are the planets " + str(planets))
# planets[3] = "skibidi toilet land"
# print("ok guys i conquered mars now its " + str(planets[3]))
# print("lets read out all the planets individually")
# for counter in range(len(planets)):
#     print(planets[counter])
# counter=0
# print("do it again!1!")
# while counter != len(planets):
#     print(planets[counter])
#     counter+=1
# print("pluto is a planet now muahahaha")
# planets.insert(10,"pluto")
# print("ok here are the planets " + str(planets))
# earth = planets.index("earth")
# planets.insert(earth, "∫ from 0 to ∞ of (e^(-x²)) / √(x² + 1) dx")
# print("i created planet ∫ from 0 to ∞ of (e^(-x²)) / √(x² + 1) dx, heres the planets " + str(planets))
# print("i hate jupiter i will kill it")
# del(planets[5])
# print("heres the planets " + str(planets))
# counter = 0
# for counter in range(len(planets)):
#     print(planets[counter])
#     if counter == planets.index("earth"):
#         print("i live here")
#     elif counter == planets.index("skibidi toilet land"):
#         print("i conquered this")
#     elif counter == planets.index("∫ from 0 to ∞ of (e^(-x²)) / √(x² + 1) dx"):
#         print("i made this")

# ## Task 3: Flight Round the Globe
# Task: Write a program to keep track of the countries you
# are visiting.

# 1. Use a while loop to ask the user what country they
#    would like to visit.
# 2. Add the country into a list
# 3. If the user types "end", exit the loop
# 4. Print all the countries in the list in this format.
#    "I would like to visit Germany"
#    "I would like to visit Japan"
#    ... 

# countries = []
# user_input = input("what country do you wanna visit ")
# while user_input != "end":
#     countries.append(user_input)
#     user_input = input("what country do you wanna visit ")
# for country in countries:
#     print("i would like to visit " + country)

# ## Task 4: Restaurant Menu
# **Task 4a**:
# Write a program to create a menu for a new
# restaurant

# 1. Using a while loop, ask the user (the restaurant manager)
#    to input food items
# 2. Add each food item into the menu list
# 3. End the loop when the user types "end"

# **Task 4b**:
# Based on the list created by the restaurant manager, do
# the following:

# 1. Imagine a customer has come in, ask the customer what
#    would they like to eat?
# 2. If the food is in the list, say "Yes we sell that,
#    please have a seat"
# 3. else, say "Sorry, please go next door, bye."

menu = []
user_input = input("what do you want on your menu ")
while user_input != "end":
    menu.append(user_input)
    user_input = input("what do you want on your menu ")
print("heres your menu: " +)