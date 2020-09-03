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
        self.colorid = 0

# create dots
dot1 = Dot()

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
            print("here")
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

    # draw dot
    screen.blit(dot1.dot, (300, 400))
    pygame.display.update()







    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if 300 < pygame.mouse.get_pos()[0] < 332 and 400 < pygame.mouse.get_pos()[1] < 432:
                    changeColor(dot1)

