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

age = 0
def isElderly(age):
    if age >= 65:
        age = True
    else:
        age = False
    return age
isElderly(66)
if age == False:
    print("you too young")
else:
    print("good")
