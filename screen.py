import pygame
from pygame import *

class Display:
    pygame.init()

    s_name = 'Py Penis'
    s_width = 640
    s_height = 480
    s_display = pygame.display.set_mode((s_width, s_height))
    s_display_name = pygame.display.set_caption(s_name)
    s_display.fill((76,150,201))

    # define the RGB value for white, 
    #  green, blue colour . 
    white = (255, 255, 255) 
    green = (0, 255, 0) 
    blue = (0, 0, 128)

    # assigning values to X and Y variable 
    X = 400
    Y = 400

    # create a font object. 
    # 1st parameter is the font file 
    # which is present in pygame. 
    # 2nd parameter is size of the font 
    font = pygame.font.Font('freesansbold.ttf', 32) 

    # create a text suface object, 
    # on which text is drawn on it. 
    text = font.render('GeeksForGeeks', True, green, blue) 
    
    # create a rectangular object for the 
    # text surface object 
    textRect = text.get_rect()  
    
    # set the center of the rectangular object. 
    textRect.center = (X // 2, Y // 2)

    pygame.display.flip()
