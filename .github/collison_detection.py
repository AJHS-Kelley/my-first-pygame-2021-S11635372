#pygame collison detection practice, Kenneth Whitfield, 1/11/22, 9:08 AM, v0.3

import pygame, sys, random
from pygame.locals import *

#setup pygame
pygame.init()
mainClock = pygame.time.Clock()

#setup pygame window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Collision Detection 2022')

#make color
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)