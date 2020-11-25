import pygame
from pygame import *


class Audio:
    title_song = 'audio/tittle_screen_bg_intro.ogg'
    title_volume = 0.2
    mixer.init()
    mixer.music.load(title_song)
    mixer.music.set_volume(title_volume)
    mixer.music.play()
