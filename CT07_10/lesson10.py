# import turtle

# window = turtle.Screen()
# window.setup(width=600, height=400)

# t = turtle.Turtle()
# t.shape("turtle")
# t.fillcolor("orange")

# while True:
#     for i in range(5):
#         t.forward(100)
#         t.right(72)

# def alert():
#     print("MOTION DETECTED!!!!! ⚠️")

# alert()
# alert()
# alert()

# import turtle

# window = turtle.Screen()
# window.setup(width=600, height=400)

# t = turtle.Turtle()
# t.shape("turtle")
# t.fillcolor("orange")

# def multiply(x,y):
#     var = x * y
#     print(var)

# multiply(3,5)

def isElderly(age):
    v = int(input("age? "))
    if v >= 65:
        v = True
    else:
        v = False
    return v
