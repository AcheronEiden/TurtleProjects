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
    return t

t.penup()
t.goto((-1.5)*strips_width, -100) # moved the turtle to the blue strips lowest left corner
t.pendown()

rectangle("blue")
t.penup()
t.goto((-0.5)*strips_width, -100) # moved the turtle to the white strips lowest left corner
t.pendown()

rectangle("white")
t.penup()
t.goto(0.5*strips_width, -100) # moved the turtle to the red strips lowest left corner
t.pendown()

rectangle("red")

turtle.done()