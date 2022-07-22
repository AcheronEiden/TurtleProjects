import turtle as t
import random as r

t.speed(0)
t.hideturtle()
t.bgcolor("black")

a = 0
b = 0

for i in range(8):
    
    x_locations = list(range(1,401))
    y_locations = list(range(1,401))
    colors = ["red", "blue", "white", "green", "orange", "yellow", "teal", "magenta"]
    
    x_location = r.choice(x_locations)
    y_location = r.choice(y_locations)
    color = r.choice(colors)

    x_locations = x_locations.remove(x_location)
    y_locations = y_locations.remove(y_location)
    colors = colors.remove(color)

    t.penup()
    t.goto(x_location, y_location)
    t.pendown()
    t.color(color)

    a = 0
    b = 0

    while True:
        t.fd(a)
        t.right(b)

        a += 3
        b += 1

        if b == 110:
            break

t.done()