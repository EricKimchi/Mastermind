# Mastermind game

import turtle, os, random

# dots cycle through six colors
def changeColor(dot):
    colorcode = ["red","orange","yellow","green","blue","purple"]
    if dot.colorid == 5:
        dot.circle.fillcolor("red")
        dot.colorid = 0
    else:
        dot.circle.fillcolor(colorcode[dot.colorid + 1])
        dot.colorid += 1

# quad class to track patterns
class Quad:
    def __init__(self):
        self.level = 0
        self.pattern = ['gray','gray','gray','gray']
        self.hint = ['gray','gray','gray','gray']

# dot class
class Dot:
    def __init__(self):
        self.circle = turtle.Turtle()
        self.circle.color("gray","red")
        self.circle.shape("circle")
        self.id = 0
        self.colorid = 0
    

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
dot1 = Dot()
dot1.circle.penup()
dot1.circle.speed(0)
dot1.circle.setposition(200,200)

# make 8 Quads to track the guesses
quads = []
for i in range(8):
    quads.append(Quad())
    quads[i].level = i

#Main game loop
while True:
    dot1.circle.onclick(lambda x, y: changeColor(dot1))
