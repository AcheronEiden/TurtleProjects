import turtle

t = turtle.Turtle()
t.hideturtle()
t.speed(10)

strips_width = 100
height = 200

def rectangle(color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(strips_width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

rectangle("blue")
t.penup()
t.goto(strips_width, 0)
t.pendown()

rectangle("white")
t.penup()
t.goto(2*strips_width, 0)
t.pendown()

rectangle("red")
t.penup()
t.goto(3*strips_width, 0)
t.pendown()

turtle.done()