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

counter = 0
planets =[
    "mercury",
    "venus",
    "earth",
    "mars",
    "jupiter",
    "saturn",
    "uranus",
    "neptune"
]
print("here are the planets " + str(planets))
planets[3] = "skibidi toilet land"
print("ok guys i conquered mars now its " + str(planets[3]))
print("lets read out all the planets individually")
for counter in range(len(planets)):
    print(planets[counter])
counter=0
print("do it again!1!")
while counter != len(planets):
    print(planets[counter])
    counter+=1
print("pluto is a planet now muahahaha")
lists.insert