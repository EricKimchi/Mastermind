import os, pygame, random


pygame.init()

# create the screen
screen = pygame.display.set_mode((600,600))

# title and icon
pygame.display.set_caption("Mastermind")
icon = pygame.image.load('m.png')
pygame.display.set_icon(icon)


# Dot class
class Dot():
    def __init__(self):
        self.dot = pygame.image.load('gray.png')
        self.id = 0
        self.x = 0
        self.y = 0
        self.colorid = 6


# change color
def changeColor(dot):
    red = pygame.image.load('red.png')
    orange = pygame.image.load('orange.png')
    yellow = pygame.image.load('yellow.png')
    green = pygame.image.load('green.png')
    blue = pygame.image.load('blue.png')
    purple = pygame.image.load('purple.png')
    gray = pygame.image.load('gray.png')

    colorCode = [red, orange, yellow, green, blue, purple, gray]

    for i in range (5):
        if dot.colorid == 6 or dot.colorid == 5:
            dot.dot = red
            dot.colorid = 0
            break
        elif dot.colorid == i:
            dot.dot = colorCode[i + 1]
            dot.colorid = i + 1
            break


# number of rows
rows = 8


# shift dots up one row
def shiftAbove():
    for index in range (4*rows):
        dots[index - 4].dot = dots[index].dot
        dots[index - 4].colorid = dots[index].colorid


# create dots
dots = []
for i in range (4*rows):
    dots.append(Dot())
    dots[i].id = i

for i in range (4*(rows-1), 4*rows):
    changeColor(dots[i])


# create guess button
guess = pygame.image.load('guess.png')


# main game loop
active = True
while active:

    # background color to light gray
    screen.fill((180, 180, 180))

    # draw dots
    x = 100
    y = 100
    col = 1

    for i in range (4*rows):
        screen.blit(dots[i].dot, (x, y))
        dots[i].x = x
        dots[i].y = y
        x += 50
        if col == 4:
            x = 100
            y += 50
            col = 0
        col += 1

    # draw guess button
    screen.blit(guess, (300, 50 + 50*rows))
    
    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if 300 < pygame.mouse.get_pos()[0] < 428 and 50 + 50*rows < pygame.mouse.get_pos()[1] < 82 + 50*rows:
                    print('pressed')
                for i in range(4*(rows-1), 4*rows):
                    if dots[i].x < pygame.mouse.get_pos()[0] < dots[i].x + 32 and dots[i].y < pygame.mouse.get_pos()[1] < dots[i].y + 32:
                        changeColor(dots[i])

