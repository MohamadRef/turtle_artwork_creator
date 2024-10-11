# My turtle Art - Star filled with random color
# Mohamad Hussam Refaai (301603558)
# November 14th/2023
import turtle
import random


pen = turtle.Turtle()
pen.speed(0)


def random_colors():
    colors = ["blue", "red", "yellow", "green", "purple"]
    return random.choice(colors)


def star():
    pen.begin_fill()
    for _ in range(5):
        pen.color(random_colors())
        pen.stamp()
        pen.left(144)
        pen.forward(200)
    pen.end_fill()


pen.penup()
pen.goto(-100, 0)
pen.pendown()


count = 0
while count < 1:
    pen.fillcolor("orange")
    star()
    count += 1


pen.hideturtle()
turtle.done()
