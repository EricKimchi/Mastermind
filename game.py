# Mastermind game

import turtle, os, pyautogui, random

def relocate(*args):
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    circle.setposition(x, y)

# set up a screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("MASTERMIND")

# draw a border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("gray")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# create a circle
circle = turtle.Turtle()
circle.color("red")
circle.shape("circle")
circle.penup()
circle.speed(0)
circle.setposition(200,200)


#Main game loop
while True:
    circle.onclick(relocate)
