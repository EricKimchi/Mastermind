import os, pygame

# TODO: test color swapping


pygame.init()

# create the screen
screen = pygame.display.set_mode((600,600))

# title and icon
pygame.display.set_caption("Mastermind")
icon = pygame.image.load('m.png')
pygame.display.set_icon(icon)

# dots
dot1 = pygame.image.load('red.png')


# main game loop
active = True
while active:

    # background color to light gray
    screen.fill((180, 180, 180))

    # draw dot
    screen.blit(dot1, (300, 400))
    pygame.display.update()







    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if 300 < pygame.mouse.get_pos()[0] < 332 and 400 < pygame.mouse.get_pos()[1] < 432:
                    print("clicked me")
