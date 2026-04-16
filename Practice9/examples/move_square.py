import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
x = 200
y = 200

running = True

while running:
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 255), (x, y, 50, 50))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 20
            elif event.key == pygame.K_RIGHT:
                x += 20

        if event.type == pygame.QUIT:
            running = False

pygame.quit()