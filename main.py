import sys
import random
import pygame
import screen
import audio
from pygame import *

import snow


class Main:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(screen.size)
        self.background = snow.BLACK
        self.running = False

    def poll(self):
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                self.running = False
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self, dt):
        pass

    def draw(self):
        pass

    def run(self):

        self.running = True
        clock = pygame.time.Clock()
        while self.running:
            dt = clock.tick(60) / 1000.0

            self.screen.fill(self.background)

            self.poll()
            self.update(dt)
            self.draw()

            for i in range(len(snow.snow_list)):

                pygame.draw.circle(self.screen, snow.WHITE, snow.snow_list[i], 2)

                # Move the snow flake down by one
                snow.snow_list[i][1] += 1

                # If the snow flake has moved off the bottom of the screen
                if snow.snow_list[i][1] > 400:
                    y = random.randrange(-50, -10)
                    snow.snow_list[i][1] = y

                    x = random.randrange(0, 640)
                    snow.snow_list[i][0] = x

            pygame.display.flip()


if __name__ == '__main__':
    main = Main()
    print("Starting...")
    main.run()
    print("shutting down...")
