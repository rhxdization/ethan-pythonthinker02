import turtle

window = turtle.Screen()
window.setup(width=600, height=400)

t = turtle.Turtle()
t.shape = "turtle"
t.fillcolor = "orange"
t.seth(0)
for i in range(4):
    t.forward()
