#simple Animation with PyGame, Kenneth Whitfield, 1/5/22, 9:39 AM, V 0.9

import pygame, sys, time
from pygame.locals import *

#Setup PyGame
pygame.init()

#setup the window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation Example!')

#setup direction variables
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4

#Make color
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#seup the box data
b1 ={'rect':pygame.Rect(300, 80, 50, 100), 'color': RED, 'dir':UPRIGHT}
b2 ={'rect':pygame.Rect(200, 200, 20, 20), 'color': GREEN, 'dir':UPLEFT}
b3 ={'rect':pygame.Rect(100, 150, 60, 60), 'color': BLUE, 'dir':UPLEFT}
boxes = [b1, b2, b3]

#run the game loop
while True:
    #check for Quit event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    windowSurface.fill(WHITE)
    
    for b in boxes:
        #move the box data structre
        if b['dir'] == DOWNLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == DOWNRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == UPLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top -= MOVESPEED
        if b['dir'] == UPRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top -= MOVESPEED

        if b['rect'].top < 0:
            #the box has moved past the top
            if b['dir'] == UPLEFT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = DOWNRIGHT
         if b ['rect'].bottom > WINDOWHEIGHT:
            #the box has moved past the bottom
            if b ['dir'] == DOWNLEFT:
                b['dir'] = UPLEFT
            if b ['dir'] == DOWNRIGHT:
                b['dir'] = UPRIGHT
        if b['rect'].left < 0:
            #the box moved past the left
            if b ['dir'] == DOWNLEFT:
                b ['dir'] = DOWNRIGHT
            if b ['dir'] == UPLEFT:
                b['dir'] = UPRIGHT
            #the box moved past the right
        if b['rect'].right . WINDOWWIDTH:
            if b ['dir'] == DOWNRIGHT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = UPLEFT
        
        # draw the box onto the game surface
        pygame.draw.rect(windowSurface, b['color'], b['rect'])

    #draw window tothe screen
    pygame.display.update()
    time.sleep(0.02)
