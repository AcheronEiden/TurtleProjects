# the file is named scanner because the final shape reminds me of an scanner scanning an object (like a planet)

import turtle as t

t.bgcolor("black")
t.color("darkorchid4")

t.speed(0)
t.hideturtle()
t.penup()
t.goto(0, 200)
t.pendown()

a = 0
b = 0

while True:
    t.fd(a)
    t.right(b)

    a += 3
    b += 1

    if b == 200:
        break
t.home() # so the turtle goes the center of the shape
t.done()