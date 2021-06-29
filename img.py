from bird import GRAY
import pygame
from pygame.locals import *

RED = (255, 0, 0)
GRAY = (150, 150, 150)

pygame.init()
w, h = 1150, 470
screen = pygame.display.set_mode((w, h))
running = True

img = pygame.image.load('sunburst2.png')
img.convert()
rect = img.get_rect()
rect.center = w//2, h//2
moving = False

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(GRAY)
    screen.blit(img, rect)

    pygame.display.flip()

pygame.quit()
