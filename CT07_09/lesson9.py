riddle = "You first enter this place blind. You then come out being able to see. What is the place? "
ans = "school"
userinput = input(riddle)
split = userinput.split()
if str(split) in ans:
    print("Correct")
else:
    print("❌")