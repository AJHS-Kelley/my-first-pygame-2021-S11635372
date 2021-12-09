#simple Animation with PyGame, Kenneth Whitfield, 12/9/21, 9:00 AM, V 0.4

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