import pygame
import random

snow_list = []

for i in range(50):
    x = random.randrange(0, 640)
    y = random.randrange(0, 640)
    snow_list.append([x, y])

BLACK = [0,   0,   0]
WHITE = [255, 255, 255]
