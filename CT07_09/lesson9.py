ans = "school"
userinput = input("You first enter this place blind. You then come out being able to see. What is the place? ")
word = []
split = userinput.split()
for i in split:
    i = i.lower()
    
if ans in str(split):
    print("✅")
else:
    print("❌")