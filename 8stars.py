import turtle

# required functions to get 8stars

def jump(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def make_turtle(x, y):
    t = turtle.Turtle()
    jump(t, x, y)
    return t

def pentagram(x, y, side, color):
    t = make_turtle(x, y)
    t.hideturtle()
    t.speed(0)
    t.setheading(270-36/2)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(5):
        t.forward(side)
        t.left(180-36)
    t.end_fill()

def Eightstars():
    t = turtle.Turtle()
    t.hideturtle()
    for x, y in [[-80, -80], [-40, -80], [0, -80], [40, -80]]:
        pentagram(x, y, 40, "darkorchid4")
    for a, b in [[-80, 80], [-40, 80], [0, 80], [40, 80]]:
        pentagram(a, b, 40, "darkorchid4")

Eightstars()

turtle.done()