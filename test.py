# this is for testing code snippets
import random as r

for i in range(401):
    x_locations = list(range(1,401))
    y_locations = list(range(1,401))
    colors = ["red", "blue", "white", "green", "orange", "yellow", "teal", "magenta"]

    x_location = r.choice(x_locations)
    y_location = r.choice(y_locations)
    color = r.choice(colors)

    x_locations = x_locations.remove(x_location)
    y_locations = y_locations.remove(y_location)
    colors = colors.remove(color)

print(x_locations, y_locations, colors)