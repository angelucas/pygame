import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Instruction Screen")

done = False
clock = pygame.time.Clock()

rect_x = 50
rect_y = 50

rect_change_x = 5
rect_change_y = 5

font = pygame.font.Font(None, 36)

display_instructions = True
instruction_page = 1

# -------- Instruction Page Loop -----------
while not done and display_instructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            instruction_page += 1
            if instruction_page == 3:
                display_instructions = False

    screen.fill(BLACK)

    if instruction_page == 1:
        text = font.render("Instructions", True, WHITE)
        screen.blit(text, [10, 10])

        text = font.render("Page 1", True, WHITE)
        screen.blit(text, [10, 40])

    if instruction_page == 2:
        text = font.render("This program bounces a rectangle", True, WHITE)
        screen.blit(text, [10, 10])

        text = font.render("Page 2", True, WHITE)
        screen.blit(text, [10, 40])

    clock.tick(60)

    pygame.display.flip()

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])

    rect_x += rect_change_x
    rect_y += rect_change_y

    if rect_y > 450 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    if rect_x > 650 or rect_x < 0:
        rect_change_x = rect_change_x * -1

    clock.tick(60)

    pygame.display.flip()

pygame.quit()
