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

# list1 = [3, 2, 1]
# list2 = [6, 5, 5]
# list3 = [9, 8, 7]

# # 1. Merge the 3 lists and remove duplicates.
# # 2. Sort the resulting list.
# # 3. Split the list into 2 sorted halves.
# # 4. Print the halves.
# # 5. 
# group = []
# unique = []
# merge = list1+list2+list3
# # create empty unique list
# for thing in merge:
#     if thing not in unique: # if item it not in unique list
#         unique.append(thing) # add item into unique list
# unique = sorted(unique)
# print(unique)

# # get midpoint
# mid = len(unique) // 2
# # slice the list for first half list1 = unique[:midpoint]
# first_half = unique[:mid]
# print(first_half)

# # slice the list for second half
# second_half = unique[mid:]
# print(second_half)

## Task 1: Password Validation

# A website requires all password to:
# 1. Be at least 8 characters long
# 2. Contain an upper and lower case
# 3. Contain a number
# 4. No other characters except alphabets or numbers

# Task:
# Write a program that will ask the user for a password, and
# check if the password fits all criteria

# You may use some of the following passwords to test your
# program:
# 1. PassW0rd
# 2. H3ll0W0r1d
# 3. BestF00d
# 4. pa55Me

eight_ch = False
upperlowerc = False
number = False
alnum = False
pw = input("enter password: ")
fr