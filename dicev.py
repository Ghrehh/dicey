import random, pygame, sys
from pygame.locals import *
from random import randint


dark_green = (0, 51, 25)

gox = 175
goy = 250

go1_button = pygame.image.load('go.png')
go2_button = pygame.image.load('go2.png')
boxRect = pygame.Rect(gox, goy, 50, 50)



mousex = 0 # used to store x coordinate of mouse event
mousey = 0 # used to store y coordinate of mouse event


def main():
    global DISPLAYSURF, clock, text, font
    pygame.init()

    rando = 6

    font = pygame.font.Font(None, 200)
    text = font.render(str(rando), True, (0, 128, 0))

    DISPLAYSURF = pygame.display.set_mode((400, 300))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Dicey')

    while True:
        mouseClicked = False

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
        hover = False
        if boxRect.collidepoint(mousex, mousey):
            hover = True

        if (hover == True) and (mouseClicked == True):
            rando = randint(1,6)
            text = font.render(str(rando), True, (0, 128, 0))


        draw(hover)


def draw(hover):
    DISPLAYSURF.fill((204, 255, 204))   
    pygame.draw.rect(DISPLAYSURF, dark_green, pygame.Rect(0, 250, 400, 50))

    DISPLAYSURF.blit(text,(160 , 60))

    if hover:
        DISPLAYSURF.blit(go2_button, (gox, goy))
    else:
        DISPLAYSURF.blit(go1_button, (gox, goy))

    pygame.display.update()
    clock.tick(30)


main()


