import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
image = pygame.image.load("mickey_hand.png")
rotated = pygame.transform.rotate(image, 45)

running = True

while running:
    screen.fill((255, 255, 255))
    screen.blit(rotated, (200, 200))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()