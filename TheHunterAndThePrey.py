import turtle
import random

# Creates the turtles that will be used in the program
t = turtle.Turtle() # responsible for drawing the environment
u = turtle.Turtle() # responsible for drawing the prey
u.color('green')
v = turtle.Turtle() # responsible for drawing the hunter
v.color('red')

def rectangle(x, y, width, height, color):
    t = make_turtle(x, y)
    t.speed(8)
    t.hideturtle()
    t.fillcolor(color)
    t.begin_fill()
    for dist in [width, height, width, height]:
        t.forward(dist)
        t.left(90)
    t.end_fill()

def make_turtle(x, y):
    t = turtle.Turtle()
    jump(t, x, y)
    return t


def jump(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

    
def move_random(t):
    if t.xcor() > 250 or t.xcor() < -250 or t.ycor() > 250 or t.ycor() < -250: # makes it so that the turtles can't go outside the rectangle
        t.setheading(t.towards(0, 0))
    t.left(random.randint(-45, 46))   # the turtles move randomly
    t.forward(random.randint(0, 26))  # the turtles move randomly
    

rectangle(-250, -250, 500, 500, 'lightblue') # creates the rectangle where the turtles will move
jump(u, random.randint(-250, 250), random.randint(-250, 250)) # makes the turtles start at a random position inside the rectangle

ggr = 0
for i in range (1, 500): # makes the turtles move 500 times
    jump(v, v.xcor(), v.ycor())
    move_random(v)
    jump(u, u.xcor(), u.ycor())

    # Calculate the distance between the hunter and prey
    distance = v.distance(u)

    # If the hunter is close to the prey, move towards the prey
    if distance < 50:
        v.write('There you are!')
        v.setheading(v.towards(u))
        v.forward(10)

    # If the prey is close to the hunter, move away from the hunter
    if distance < 50:
        u.write('Close')
        u.setheading(u.towards(v) + 180)
        u.forward(10)

        ggr += 1

print('Close calls: ', ggr)
