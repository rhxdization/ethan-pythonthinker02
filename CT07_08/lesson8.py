# # counter = 0
# # import random
# # lives = 10
# # while lives > 0:
# #     counter+=1
# #     lives-=random.randint(1,3)
# # print(counter)

# list = ["pizza",
#         "chicken",
#         "dog"]
# # for n, i in enumerate(list):
# #     print(f"{n+1}. {i}")

# num = 1
# for i in list:
#     print(str(num) + ": " + i)
#     num += 1


# # Lesson 8 - String splitting, list joining, and
# #            finding substring

# ## Recap 1: List Manipulation
# Given 3 lists, merge them into a single list, remove
# duplicates, and then split the list into 2 halves,
# ensuring both halves are sorted.

list1 = [3, 2, 1]
list2 = [6, 5, 5]
list3 = [9, 8, 7]

# 1. Merge the 3 lists and remove duplicates.
# 2. Sort the resulting list.
# 3. Split the list into 2 sorted halves.
# 4. Print the halves.
# 5. 
group = []
unique = []
merge = list1+list2+list3
# create empty unique list
for thing in merge:
    if thing not in unique: # if item it not in unique list
        unique.append(thing) # add item into unique list
unique = sorted(unique)
print(unique)

# get midpoint
mid = len(
# slice the list for first half list1 = unique[:midpoint]
# slice the list for second half
for i in range(0, len(unique), 2):
        group.append(merge[i:i+2])
print(group)
