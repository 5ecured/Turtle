from turtle import Turtle, Screen
import random

tim = Turtle()

colors = ['medium aquamarine', 'spring green', 'navy', 'magenta', 'blue violet', 'yellow', 'lime', 'deep sky blue', 'sienna', 'light slate gray']
directions = [0, 90, 180, 270]
tim.pensize(10)
tim.speed('fastest')

for _ in range(100):
    tim.color(random.choice(colors))
    tim.forward(50)
    tim.setheading(random.choice(directions))