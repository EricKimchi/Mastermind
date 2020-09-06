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


class Hint():
    def __init__(self):
        self.color = pygame.image.load('hintgray.png')
        self.colorid = 0


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


# reset dots
def resetGame():
    for dot in dots:
        dot.dot = pygame.image.load('gray.png')
        dot.colorid = 6
    for i in range (4*(rows-1), 4*rows):
        dots[i].dot = pygame.image.load('red.png')
        dots[i].colorid = 0
    for i in range (4*rows - 8):
        hints[i].color = pygame.image.load('hintgray.png')
        hints[i].colorid = 0
    
    return setPattern()


# number of rows
rows = 8


# shift dots up one row
def shiftAbove():
    # shift all colors up one row
    for index in range (4, 4*rows - 4):
        dots[index].dot = dots[index + 4].dot
        dots[index].colorid = dots[index + 4].colorid
    # reset bottom dots to red
    for i in range (4*(rows-1), 4*rows):
        dots[i].dot = pygame.image.load('red.png')
        dots[i].colorid = 0


# create dots
dots = []
for i in range (4*rows):
    dots.append(Dot())
    dots[i].id = i

# set bottom row dots to red
for i in range (4*(rows-1), 4*rows):
    changeColor(dots[i])


# create hint dots
hints = []
for i in range (4*rows - 8):
    hints.append(Hint())
    hints[i].id = i

# create guess and reset buttons
guess = pygame.image.load('guess.png')
reset = pygame.image.load('reset.png')


# set random pattern
def setPattern():
    red = pygame.image.load('red.png')
    orange = pygame.image.load('orange.png')
    yellow = pygame.image.load('yellow.png')
    green = pygame.image.load('green.png')
    blue = pygame.image.load('blue.png')
    purple = pygame.image.load('purple.png')

    patternCode = []
    colorCode = [red, orange, yellow, green, blue, purple]
    for i in range (4):
        num = random.randint(0, 5)
        dots[i].colorid = num
        patternCode.append(num)
    return patternCode


def reveal(patternCode):
    red = pygame.image.load('red.png')
    orange = pygame.image.load('orange.png')
    yellow = pygame.image.load('yellow.png')
    green = pygame.image.load('green.png')
    blue = pygame.image.load('blue.png')
    purple = pygame.image.load('purple.png')

    colorCode = [red, orange, yellow, green, blue, purple]
    for i in range (4):
        dots[i].dot = colorCode[patternCode[i]]


# compare patterns
def compPattern(answer):

    colorCounter = [0, 0, 0, 0, 0, 0]
    ansColorCounter = [0, 0, 0, 0, 0, 0]
    hintColors = []
    hintCounter = 0
    counterIndex = 0
    hintIndex = 0

    for i in range (4):
        colorCounter[dots[4*rows - 4 + i].colorid] += 1
        ansColorCounter[answer[i]] += 1
        if dots[4*rows - 4 + i].colorid == answer[i]:
            hintColors.append(1)
            hintCounter += 1
            colorCounter[answer[i]] -= 1
            ansColorCounter[answer[i]] -= 1
            hintIndex += 1

    while (hintIndex < 4 and counterIndex < 6):
        if colorCounter[counterIndex] > 0 and ansColorCounter[counterIndex] > 0:
            hintColors.append(2)
            hintIndex += 1
            colorCounter[counterIndex] -= 1
            ansColorCounter[counterIndex] -=1
        else:
            counterIndex += 1
    
    while (len(hintColors) < 4):
        hintColors.append(0)
    
    return hintColors


#
def shiftHints(answer):
    gray = pygame.image.load('hintgray.png')
    black = pygame.image.load('hintblack.png')
    white = pygame.image.load('hintwhite.png')
    colorCode = [gray, black, white]

    # shift all hints up one row
    for index in range (4*rows - 12):
        hints[index].color = hints[index + 4].color
        hints[index].colorid = hints[index + 4].colorid
    # set new hint
    newHint = compPattern(answer)
    index = 0
    for i in range (4*rows - 12, 4*rows - 8):
        hints[i].color = colorCode[newHint[index]]
        hints[i].colorid = newHint[index]
        index += 1


# main game loop
active = True
won = True
freeze = False
# set random pattern
pattern = setPattern()
while active:

    # background color to light gray
    screen.fill((180, 180, 180))

    # draw dots
    x = 200
    y = 100
    col = 1

    for i in range (4*rows):
        screen.blit(dots[i].dot, (x, y))
        dots[i].x = x
        dots[i].y = y
        x += 50
        if col == 4:
            x = 200
            y += 50
            col = 0
        col += 1

    # draw hint dots
    x = 150
    y = 145
    col = 1
    level = 0

    for i in range (4*rows - 8):
        screen.blit(hints[i].color, (x, y))
        x += 20
        level += 1
        if col == 2:
            x = 150
            if level == 4:
                y += 30
                level = 0
            else:
                y += 20
            col = 1
        else:
            col += 1


    # draw guess and reset buttons
    screen.blit(guess, (400, 50 + 50*rows))
    screen.blit(reset, (400, 50*rows))

    pygame.display.update()

    # game events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and freeze == False:
                # guess button is pressed
                if 400 < pygame.mouse.get_pos()[0] < 528 and 50 + 50*rows < pygame.mouse.get_pos()[1] < 82 + 50*rows:
                    # compare guessed pattern and random pattern
                    for i in range (4):
                        if dots[4*rows - 4 + i].colorid != pattern[i]:
                            # won set to false if a dot is not matching
                            won = False
                    # shift dots up one row
                    shiftHints(pattern)
                    shiftAbove()
                    if won == True:
                        print("You Win!")
                        reveal(pattern)
                        freeze = True
                    elif dots[4].colorid != 6:
                        # all guesses used
                        print("You LOSE!")
                        reveal(pattern)
                        freeze = True
                    won = True

                # guessing dots are clicked
                for i in range(4*(rows-1), 4*rows):
                    if dots[i].x < pygame.mouse.get_pos()[0] < dots[i].x + 30 and dots[i].y < pygame.mouse.get_pos()[1] < dots[i].y + 30:
                        changeColor(dots[i])

                # reset button is pressed
                if 400 < pygame.mouse.get_pos()[0] < 528 and 50*rows < pygame.mouse.get_pos()[1] < 32 + 50*rows:
                    pattern = resetGame()

            elif event.button == 1 and freeze == True:
                # reset button is pressed
                if 400 < pygame.mouse.get_pos()[0] < 528 and 50*rows < pygame.mouse.get_pos()[1] < 32 + 50*rows:
                    pattern = resetGame()
                    freeze = False



