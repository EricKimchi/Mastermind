# Mastermind game

import turtle, os, pyautogui, random

def changeColor(*args):
    if circle.fillcolor() == "red":
        circle.fillcolor("blue")
    else: 
        circle.fillcolor("red")

# TODO: "set" class to hold patterns of colored dots


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
circle.color("gray","red")
circle.shape("circle")
circle.penup()
circle.speed(0)
circle.setposition(200,200)


#Main game loop
while True:
    circle.onclick(changeColor)
