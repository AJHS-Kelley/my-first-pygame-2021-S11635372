#simple Animation with PyGame, Kenneth Whitfield, 12/9/21, 8:29 AM, V 0.1

import pygame, sys, time
from pygame.locals import *

#Setup PyGame
pygame.init()

#setup the window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation Example!')