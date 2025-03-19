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
t.shape("circle")
t.fillcolor("black")
t.speed(10)
while True:
    t.seth(0)
    t.forward(60)
    t.left(90)