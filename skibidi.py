# # Import
# import random
# # Variables
# health = 100
# counter = 0
# healthlost = 0
# # Show health
# print("player has health of " + str(health))
# # While health is more than 0 keep fighting
# while health > 0:
#     # Random number from 1 to 15 to decide how much health is lost
#     healthlost = random.randint(1,15)
#     # Set health
#     health -= healthlost
#     if health < 0:
#         break
#     else:
#         counter += 1
#         print("player has lost " + str(healthlost) + " health and now has " + str(health))
# # Print out how many times player fought
# print("player fought " + str(counter) + " times")



# Variables
order = []
userinput = ""
# While loop that will end if users input is "end"
while userinput != "end":
    userinput = input("what would you like to order: ")
    if userinput == "end":
        break
    else:
        order.append(userinput)
