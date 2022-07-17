import turtle

t = turtle.Turtle()

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

# creates four cicles at the squares four corners
t.color("darkorchid4")
for x, y in [[-200, -200], [200, -200], [200, 100], [-200, 100]]:
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(50)
    t.end_fill()

turtle.done()