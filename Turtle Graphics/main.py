from turtle import Turtle, Screen, colormode
import random

timmy_the_turtle = Turtle()
colours = [
    "blue",
    "red",
    "orange red",
    "gold",
    "lime",
    "deep pink",
    "rebecca purple",
    "medium spring green",
    "hot pink",
    "deep sky blue",
    "dodger blue",
    "green yellow",
    "blanched almond",
    "peach puff",
    "slate blue",
    "light goldenrod yellow",
    "medium sea green",
    "light sky blue",
]


timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")
number_of_side = 3

for _ in range(10):
    for _ in range(number_of_side):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(360 / number_of_side)
    number_of_side += 1
    timmy_the_turtle.color(random.choice(colours))


screen = Screen()
screen.exitonclick()
