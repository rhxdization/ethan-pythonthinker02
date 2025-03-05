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
    # Check if userinput is equal or not equal to "end" to avoid appending "end" to order
    if userinput == "end":
        break
    else:
        # Append to list order
        order.append(userinput)
print("you have ordered the following:")
# For loop to print out users order
for i in range(len(order)):
    print(str(i+1) , ": " + str(order[i]))