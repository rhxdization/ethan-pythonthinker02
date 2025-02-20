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