from turtle import Turtle, Screen
import random

tim = Turtle()

colors = ['medium aquamarine', 'spring green', 'navy', 'magenta', 'blue violet', 'yellow', 'lime', 'deep sky blue', 'sienna', 'light slate gray']

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for i in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(i)