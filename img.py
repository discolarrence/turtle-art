import pygame
from pygame.locals import *

GREEN = (0, 255, 0)
GRAY = (150, 150, 150)

A1 = {"top_left_x":45, 
    "top_left_y":455,
    "top_right_x":195,
    "top_right_y":165,
    "bottom_left_x": (),
    "bottom_left_y": (),
    "bottom_right_x": (),
    "bottom_right_y": ()}

A2 = {"top_left_x":85, 
    "top_left_y":410,
    "top_right_x":195,
    "top_right_y":165,
    "bottom_left_x": (),
    "bottom_left_y": (),
    "bottom_right_x": (),
    "bottom_right_y": ()}

A3 = {"top_left_x":85, 
    "top_left_y":410,
    "top_right_x":195,
    "top_right_y":165,
    "bottom_left_x": (),
    "bottom_left_y": (),
    "bottom_right_x": (),
    "bottom_right_y": ()}

A4 = {"top_left": (),
    "top_right": (),
    "bottom_left": (),
    "bottom_right": ()}


pygame.init()
w, h = 1200, 480
screen = pygame.display.set_mode((w, h))
running = True

img = pygame.image.load('sunburst7.jpg')
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
    pygame.draw.line(screen, GREEN, (A1["top_left_x"], A1["top_left_y"]), (A2["top_left_x"], A2["top_left_y"]), 3)

    pygame.display.flip()

pygame.quit()
