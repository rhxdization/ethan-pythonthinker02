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

# # 1. Merge the 3 lists and remove duplicates.
# # 2. Sort the resulting list.
# # 3. Split the list into 2 sorted halves.
# # 4. Print the halves.
# # 5. 

list1 = [3, 2, 1]
list2 = [6, 5, 5]
list3 = [9, 8, 7]

group = []
unique = []
merge = list1+list2+list3
for thing in merge:
    if thing not in unique: # if item it not in unique list
        unique.append(thing) # add item into unique list
unique = sorted(unique)
print(unique)

mid = len(unique) // 2
# slice the list for first half list1 = unique[:midpoint]
first_half = unique[:mid]
print(first_half)

second_half = unique[mid:]
print(second_half)

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

# eight_ch = False
# upperc = False
# lowerc = False
# number = False
# alnum = False
# pw = input("enter password: ")
# if len(pw) < 8:
#     print("password not strong enough")
# else:
#     eight_ch = True
# if eight_ch == True:
#     for i in pw: #in my password "pAs"
#         if i.isupper():
#             upperc = True
#         if i.islower():
#             lowerc = True
#         if i.isdigit():
#             number = True

# if pw.isalnum():
#     alnum = True
# if eight_ch == True and upperc == True and lowerc == True and number == True and alnum == True:
#     print("password is good to go")
# else:
#     print("bad!!!")

# ## Task 2: Mocking Text Generator

# Create a program that will turn regular sentences into a
# "SpongeBob Mocking" meme.

# For example, the program will turn "Hello my name is James"
# into "HeLlO mY nAmE iS jAmEs"

# 1. Using 'input()', ask the user for a sentence
# 2. Use loops to iterate through each letter of the sentence
# 3. Alternate between '.upper()' and '.lower()' for each letter
# 4. Print the result

# # counter = 0
# out = ""
# str = input("enter something funny ")
# for i in str:   
#     if counter % 2 == 0:
#         out += i.lower()
#         counter+=1
#     else:
#         out += i.upper()
#         counter+=1
# print(out)

# ## Task 3: Splitting a Sentence into Words (.split())
# **Task 3a**:
# Write a program to split the following string into a list of
# words using space as the delimiter:

# Example:
# Input:
# "Computers empower our modern world with their digital brains."

# Output:
# ['Computers',
#  'empower',
#  'our',
#  'modern',
#  'world',
#  'with',
#  'their',
#  'digital',
#  'brains.']

# str = "Computers empower our modern world with their digital brains."
# split = str.split()
# print(split)


# **Task 3b**:
# Write a program to split the following string into a list of
# words using a comma (,) as the delimiter:

# "Computers,empower,our,modern,world,with,their,digital,brains"

# Example:
# Input: "Computers,empower,our,modern,world,with,their,digital,brains"
# Output: ['Computers',
#          'empower',
#          'our',
#          'modern',
#          'world',
#          'with',
#          'their',
#          'digital',
#          'brains.']

# str = "Computers,empower,our,modern,world,with,their,digital,brains"
# split = str.split(",")
# print(split)

# ## Task 4: Joining Words into a Sentence (.join())
# **Task 4a**:
# Given the following list of words, write a program to join
# these words into a single string, separated by spaces:

# ['Computers', 'empower', 'our', 'modern', 'world', 'with', 'their', 'digital', 'brains.']

# Example:
# Input: ['Computers', 'empower', 'our', 'modern', 'world', 'with', 'their', 'digital', 'brains.']
# Output: "Computers empower our modern world with their digital brains."


# str = ['Computers', 'empower', 'our', 'modern', 'world', 'with', 'their', 'digital', 'brains.']
# join = " ".join(str)
# print(join)

# **Task 4b**:
# Given the following list of words, write a program to join
# these words into a single string, separated by commas:

# ['Computers', 'empower', 'our', 'modern', 'world', 'with', 'their', 'digital', 'brains.']

# Example:
# Input: ['Computers', 'empower', 'our', 'modern', 'world', 'with', 'their', 'digital', 'brains.']
# Output: "Computers,empower,our,modern,world,with,their,digital,brains"

# str = ['Computers', 'empower', 'our', 'modern', 'world', 'with', 'their', 'digital', 'brains.']
# join = ",".join(str)
# print(join)