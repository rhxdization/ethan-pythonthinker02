
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

# list1 = [3, 2, 1]
# list2 = [6, 5, 5]
# list3 = [9, 8, 7]
# unique = []

# merge = list1+list2+list3
# for thing in merge:
#     if thing not in unique:
#         unique.append(thing)
# unique = sorted(unique)
# print(unique)

# mid = len(unique) // 2
# first_half = unique[:mid]
# print(first_half)

# second_half = unique[mid:]
# print(second_half)

# upper = False
# lower = False
# num = False
# alnum = True
# pw = input("what is your password: ")

# if len(pw) < 8:
#     print("password is not strong enough")
# else:
#         for letter in pw:
#             if upper == False:
#                 upper = letter.isupper()
#             if lower == False:
#                 lower = letter.islower()
#             if num == False:
#                 num = letter.isnumeric()
#             if alnum == False:
#                 alnum = letter.isalnum()
#         if upper == True and lower == True and num == True and alnum == True:
#             print("password is strong")
#         else:
#             print("password is not good")

# ## Task 2: Mocking Text Generator

# Create a program that will turn regular sentences into a
# "SpongeBob Mocking" meme.

# For example, the program will turn "Hello my name is James"
# into "HeLlO mY nAmE iS jAmEs"

# 1. Using 'input()', ask the user for a sentence
# 2. Use loops to iterate through each letter of the sentence
# 3. Alternate between '.upper()' and '.lower()' for each letter
# 4. Print the result
counter = 0
input = input("input ")
input2 = ""
for i in input:
    if counter % 2 == 0:
        i = i.lower()
        input2 += i
    else:
        i = i.upper()
        input2 += i
print(input2)