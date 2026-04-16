import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
running = True

while running:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (250, 250), 50)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()