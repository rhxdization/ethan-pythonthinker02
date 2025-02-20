# import random
# numbers = []
# for i in range(0,100):
#     added = random.randint(1,1000)
#     if added not in numbers:
#         numbers.append(added)
# print("The winning numbers are: " + str(numbers))

import random
numbers = []
for i in range(0,100):
    added = random.randint(1,1000)
    if added not in numbers:
        numbers.append(added)
for i in numbers:
    print(i)
print("average score is " + str(sum(numbers) / len(numbers)))
print("biggest score is " + str(max(numbers)))
print("smallest score is " + str(min(numbers)))
num = random.choice(numbers)
num2 = numbers.index(num)
print(num2)


# # Lesson 8 - String splitting, list joining, and
# #            finding substring

# ## Recap 1: List Manipulation
# Given 3 lists, merge them into a single list, remove
# duplicates, and then split the list into 2 halves,
# ensuring both halves are sorted.

# list1 = [3, 2, 1]
# list2 = [6, 5, 5]
# list3 = [9, 8, 7]

# 1. Merge the 3 lists and remove duplicates.
# 2. Sort the resulting list.
# 3. Split the list into 2 sorted halves.
# 4. Print the halves.
# 5. 