
# recap 1

# **Task: write a separate 'for' loop to print the following
# numbers:**
# 1. from 0 - 20
# 2. from 1 to 30
# 3. from 2 to 24 (in even numbers)

# for i in range(2,25,2):
#     print(i)

# # Task 1: Introduction to while loop
# **Task: Using a separate 'while' loop, print each of the
# following:**
# 1. from 0 to 20
# 2. from 1 to 30
# 3. from 2 to 24

# skibidi = 2
# while skibidi <= 24:
#     print(skibidi)
#     skibidi+=1

# ## Task 2: while... break
# The **break** keyword will **break** out (exit) the loop.
# When a **break** is encountered, the code in the **else** will
# not be run.

# Using a while loop:
# 1. print the numbers from 1 to 10
# 2. if the number is 5, **break** out of the loop

# counter = 1
# while True:
#     print(counter)
#     counter+=1
#     if counter > 5:
#         break

# ## Task 3: while... else
# The else condition will run when the loop exits normally
# i.e. when the while condition is no longer true.

# **Task 3a**: Using a while loop
# 1. print the numbers from 1 to 10
# 2. once count has reached 10, use the else and print "Count
#    has reached 10"

# **Task 3b**:
# Now, modify your 'while' loop such that:
# 1. If the number is 5, **break** out of the loop
# 2. Ensure your code has an else

# Observe if the code in the **else** runs.

counter = 0
while counter <= 10:
    counter+=1
    print("counter")
    if counter == 10:
        print("Counter has reached 10")