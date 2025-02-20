# # Lesson 7 - 2 dimensional list

# ## Recap 1: Student Contact Database
# Task: Create a contact database for students
# 1. Create a list variable called students
# 2. Create 3 lists called student1, student2, student3
#     each student should have the following info:
#         1. name
#         2. phone number
#         3. CCA
# 3. Add student1, student2, student3 into the students list.
# 4. Unpack the list and use loop and string concatenation to
#    print the details for each student in the following format:

#    Name: James
#    Phone number: 85726845
#    CCA: Hockey

# ## Task 1: Introduction to List Merging
# You are given 2 lists of fruits. Merge them into 1 list and
# print the result.

# 1. Use the + operator to combine the lists.
# 2. Print the combined list.
## Task 1: Introduction to List Merging

# list1 = ["Apple", "Banana", "Cherry"]
# list2 = ["Durian", "Elderberry", "Figs"]
# fruits = list1 + list2
# print(fruits)

# # sorted stuff
# list = [1,5,69,3,68,81,420]
# sorted_nums = sorted(list)
# print(sorted_nums)

# ## Task 2: Ordered List Merging
# You are given 2 lists that contain the price of fruits. Now,
# merge 2 given lists and ensure the resulting list is sorted.

# 1. Merge the lists using the + operator.
# 2. Use the sorted() function to sort the combined list.
# 3. Print the sorted list.

# list1 = [3.20, 2.65, 1.75]
# list2 = [6.15, 5.45, 4.20]
# merge = list1+list2
# sort = sorted(merge)
# print(sort)

# ## Task 3: Splitting Lists at a Point
# You are required to divide a basket of fruits.
# Split the given list at the specified index:

# 1. Use slicing to split the list at the provided index.
# 2. Print the resulting sublists.

# fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Figs"]
# index = 3
# split = fruits[index:]
# split2 = fruits[:index]
# print("right side is " + str(split))
# print("left side is " + str(split2))

# ## Task 4: Splitting a List in Half
# You have been tasked to divide the basket of fruits into
# 2 equal halves. Given a list of even length, split it
# into 2 equal halves.

# fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Figs"]

# 1. Find the midpoint of the list.
# 2. Split the list into 2 halves using slicing.
# 3. Print both halves.

# fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Figs"]
# midpoint = len(fruits) // 2
# print(fruits[midpoint])

# ## Task 5: Identifying Common Elements in Lists
# You have been given 2 lists of fruits. However, there might be
# duplicates. Your job is to identify and print the common fruits
# between them.

# list1 = ["Apple", "Banana", "Cherry", "Durian"]
# list2 = ["Cherry", "Durian", "Elderberry", "Figs"]

# 1. Create an empty list named 'common'
# 2. Using 'for' loops, append common elements into 'common'
# 3. Print the common elements
# unique = []
# common = []
# list1 = ["Apple", "Banana", "Cherry", "Durian"]
# list2 = ["Cherry", "Durian", "Elderberry", "Figs"]
# for each in list1:
#     if each in list2:
#         common.append(each)
# print(common)
# for each in list1:
#     if each not in list2:
#         unique.append(each)
# print(unique)

# ## Task 7: Merging Lists with Conditions
# You have been given the index number of 2 groups of students.
# However, only students with even index number is allowed
# to come into the room. Create a Python script that will
# merge the 2 lists, including only the elements that are
# even from both.

# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]

# 1. Merge the lists using a list comprehension with a
#    condition. 
# 2. Print the new list.
# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
# merged = list1 + list2
# even = []
# for thing in merged:
#     if (thing%2) == 0:
#         even.append(thing)
# print(even)

# ## Task 8: Nested List Splitting
# You are given a nested list of 3 groups of students that
# are each seated in a pair. However, you want to unpack
# the nested lists in order to have a list of all students.

# nested_list = [[1, 2], [3, 4], [5, 6]]

# 1. Use a loop or list comprehension to flatten the list.
# 2. Print the flattened list.

nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = []


