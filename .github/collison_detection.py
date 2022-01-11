#pygame collison detection practice, Kenneth Whitfield, 1/11/22, 9:02 AM, v0.2

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