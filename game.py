import os, pygame


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
        self.dot = pygame.image.load('red.png')
        self.id = 0
        self.x = 0
        self.y = 0
        self.colorid = 0

# create dots
dots = []
for i in range (24):
    dots.append(Dot())

def changeColor(dot):
    red = pygame.image.load('red.png')
    orange = pygame.image.load('orange.png')
    yellow = pygame.image.load('yellow.png')
    green = pygame.image.load('green.png')
    blue = pygame.image.load('blue.png')
    purple = pygame.image.load('purple.png')

    colorCode = [red, orange, yellow, green, blue, purple]

    for i in range (5):
        if dot.colorid == 5:
            dot.dot = red
            dot.colorid = 0
            break
        elif dot.colorid == i:
            dot.dot = colorCode[i + 1]
            dot.colorid = i + 1
            break


# main game loop
active = True
while active:

    # background color to light gray
    screen.fill((180, 180, 180))

    # draw dots
    x = 300
    y = 200
    col = 1
    for i in range (24):
        screen.blit(dots[i].dot, (x, y))
        dots[i].x = x
        dots[i].y = y
        x += 50
        if col == 4:
            x = 300
            y += 50
            col = 0
        col += 1
    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for dot in dots:
                    if dot.x < pygame.mouse.get_pos()[0] < dot.x + 32 and dot.y < pygame.mouse.get_pos()[1] < dot.y + 32:
                        changeColor(dot)

