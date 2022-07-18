import turtle

t = turtle.Turtle()
t.hideturtle()

t.penup()
t.goto(-200, -200)
t.pendown()

# create a square
t.fillcolor("black")
t.begin_fill()
for i in range(4):
    t.forward(400)
    t.left(90)
t.end_fill()

# creates four semicicles at the square's four corners
t.color("darkorchid4")
for x, y in [[-200, -85.5], [200, -200], [-200, 200], [200, 85.5]]:
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    for x in range(180):
        t.forward(1)
        t.right(1)
    t.end_fill()

turtle.done()