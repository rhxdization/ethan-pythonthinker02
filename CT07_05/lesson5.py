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

food = [
    "pizza",
    "burger",
    "noodles",
    "fish",
    "egg"
]
print("i like these foods " + str(food))
del food[2]
print("nevermind i hate noodles now i only like " + str(food))
food.append("humans")
print("i like humans now i like " + str(food))
prin