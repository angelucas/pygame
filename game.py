#!/usr/bin/env python3
import pygame
from sys import exit

background_colour = (255, 150, 255)
(width, heigth) = (400, 300)

screen = pygame.display.set_mode((width, heigth))
pygame.display.set_caption('Janela dos Guris')
screen.fill(background_colour)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            exit()

    pygame.display.flip()
