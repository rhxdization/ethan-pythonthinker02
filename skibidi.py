# Import
import random
# Variables
health = 100
counter = 0
healthlost = 0
# Show health
print("player has health of " + str(health))
# While health is more than 0 keep fighting
while health > 0:
    # Random number from 1 to 15 to decide how much health is lost
    print("player has lost " + str(healthlost) + " health and now has " + str(health))
    healthlost = random.randint(1,15)
    # Set health
    health -= healthlost
# Print out how many times player fought
