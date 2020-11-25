import pygame
from pygame import *

title_song = 'audio/tittle_screen_bg_intro.ogg'
title_volume = 0.5

class Sound:
    # Starting the mixer
    mixer.init()

    # Loading the song
    mixer.music.load(title_song)

    # Setting the volume
    mixer.music.set_volume(title_volume)
