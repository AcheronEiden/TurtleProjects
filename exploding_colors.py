import turtle as t
import random as r

t.hideturtle()
t.bgcolor("black")

def stars():
    a = 0
    b = 0

    while True:
        t.speed(0)
        t.fd(a)
        t.right(b)

        a += 3
        b += 1

        if b == 110:
            break
    
    return t

for i in range(8):
    x_coordinates = list(range(-200, 201))
    y_coordinates = list(range(-200, 201))
    colors = ["red", "blue", "white", "green", "orange", "yellow", "teal", "magenta"]

    x_coordinate = r.choice(x_coordinates)
    y_coordinate = r.choice(y_coordinates)
    color = r.choice(colors)

    t.penup()
    t.goto(x_coordinate, y_coordinate)
    t.pendown()
    t.color(color)
    stars()

    x_coordinates = x_coordinates.remove(x_coordinate)
    y_coordinates = y_coordinates.remove(y_coordinate)
    colors.remove(color)

t.done()