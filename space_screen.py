import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

screen = pygame.display.set_mode([800, 600])

pygame.display.set_caption('this is cool')

clock = pygame.time.Clock()

click_sound = pygame.mixer.Sound("audio/shot.ogg")
click_sound.set_volume(0.2)

background_position = [0, 0]

background_image = pygame.image.load("img/galaxy.jpg").convert()
player_image = pygame.image.load("img/player.png").convert()
player_image.set_colorkey(BLACK)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()

            # Copy image to screen:
    screen.blit(background_image, background_position)

    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]

    screen.blit(player_image, [x, y])

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
