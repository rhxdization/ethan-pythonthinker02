# Variables
health = 100
# Show health
print("player has health of " + str(health))
# While health is more than 0 keep fighting
while health > 0:
    healthlost = random.randint(1,15)