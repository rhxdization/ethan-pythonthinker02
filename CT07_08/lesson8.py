
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

upper = False
lower = False
num = False
alnum = False

