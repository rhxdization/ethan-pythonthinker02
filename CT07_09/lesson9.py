ans = "school"
userinput = input("You first enter this place blind. You then come out being able to see. What is the place? ")
split = userinput.split()
if str(split) in ans:
    print("✅")
else:
    print("❌")