import turtle

window = turtle.Screen()
window.setup(width=600, height=400)

t = turtle.Turtle()
t.shape = "turtle"
t.fillcolor = "orange"

t.seth(0)
while True:
for i in range(4):
        t.forward(100)
        t.right(90)
