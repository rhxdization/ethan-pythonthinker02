ans = "school"
userinput = input("You first enter this place blind. You then come out being able to see. What is the place? ")
split = userinput.split()
for i in split:
    i = i
if ans in str(split):
    print("✅")
else:
    print("❌")