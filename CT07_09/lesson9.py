# ans = "egg"
# userinput = input("I must be opened before being able to use. What am I? ")
# word = []
# split = userinput.split()
# for i in split:
#     i = i.lower()
#     word.append(i)
# if ans in str(word):
#     print("✅")
# else:
#     print("❌")

import turtle
window = turtle.Screen()
window.setup(width=600, height=600)
window.bgcolor("forestgreen")
t = turtle.Turtle()
t.shape("square")
t.fillcolor("black")
t.up()
t.goto(-300,225)
t.seth(0)
for i in range(0,24):
    t.stamp()
    t.forward(25)
t.goto(-300,-225)
t.pendown()
t.pencolor("red")
t.seth(0)
t.forward(600)
t.hideturtle()

sally = turtle.Turtle()
sally.up()
sally.seth(90)
sally.shape("turtle")
sally.color("red")
sally.goto(-150,-250)
sally.write("Sally", align="center", font=("Arial", 20))

X_Æ_A_12 = turtle.Turtle()
X_Æ_A_12.up()
X_Æ_A_12.seth(90)
X_Æ_A_12.shape("turtle")
X_Æ_A_12.color("yellow")
X_Æ_A_12.goto(0,-250)



window.mainloop()