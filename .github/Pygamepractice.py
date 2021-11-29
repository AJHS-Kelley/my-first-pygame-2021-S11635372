# Pygame practice, Kenneth Whitfield, 11/29/21, 9:40AM, v0.8

import pygame, sys
from pygame.locals import *

# start pygame
pygame.init()

#create game window
windowSurface = pygame.display.set_mode((500, 400),0, 32)
pygame.display.set_caption ("Hello, world")

#set collor values
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# setup fonts
basicFont = pygame.font.SysFont(None, 48)

#setup text
text = basicFont.render('Hello world', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

#draw background onto window surface
windowSurface.fill(WHITE)

#draw a green polygon onto the surface
pygame.draw.polygon(windowSurface, GREEN, ((146,0), (291, 106), (236, 277), (56, 277), (0, 106)))

#draw blue lines on window surface
pygame.draw.lines(windowSurface, BLUE, (60, 60),(120, 60), 4)
pygame.draw.lines(windowSurface, BLUE, (120, 60),(60, 120))
pygame.draw.lines(windowSurface, BLUE, (60, 120),(120,120), 4)

#draw a cricle
pygame.drawcircle (windowSurface, RED, (300, 50), 20, 0)

#draw an ellispe 
pygame.draw.ellipse(windowSurface, BLACK, (300, 250, 40, 80), 1)

#draw text background rectangle onto surface
pygame.draw.rect(windowSurface,RED ,textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height +40)