# import random
# numbers = []
# for i in range(0,100):
#     added = random.randint(1,1000)
#     if added not in numbers:
#         numbers.append(added)
# print("The winning numbers are: " + str(numbers))

# import random
# numbers = []
# for i in range(0,100):
#     added = random.randint(1,1000)
#     if added not in numbers:
#         numbers.append(added)
# for i in numbers:
#     print(i)
# print("average score is " + str(sum(numbers) / len(numbers)))
# print("biggest score is " + str(max(numbers)))
# print("smallest score is " + str(min(numbers)))
# num = random.choice(numbers)
# num2 = numbers.index(num)
# print(numbers[num2])

# ## Task 1: A list within a list 

# You are about to graduate and would like to create a database
# to keep all your friend's contact details using a 2d list.

# 1. append contact1, contact2, and contact3 into contacts
# 2. Write a nested loop to loop through each contact and print
#    the details for each contact

# contacts = []
# contact1 = ["John", 98453126, "john@gmail.com"]
# contact2 = ["Adam", 93029102, "adam@gmail.com"]
# contact3 = ["Sylvia", 87894032, "sylvia@gmail.com"]

# contacts.append(contact1)
# contacts.append(contact2)
# contacts.append(contact3)
# for _ in contacts:
#     for i in _:
#         print(i)
    
# ## Task 2: Student List
# You have been given a 2d list of students from a class
# consisting each student's name and their gender.

# 1. Write a for loop to print out the names of each student and
#    the gender beside.
   
#    e.g. Olivia F
#         Noah M

students = [
    ["Olivia", "F"], ["Noah", "M"], ["Emma", "F"],
    ["Liam", "M"], ["Ava", "F"], ["Ethan", "M"],
    ["Sophia", "F"], ["Lucas", "M"], ["Mia", "F"],
    ["Aiden", "M"], ["Isabella", "F"], ["Jackson", "M"],
    ["Amelia", "F"], ["Logan", "M"], ["Lily", "F"]]

for _ in students:
    name, gender = 