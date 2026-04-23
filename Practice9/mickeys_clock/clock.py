import pygame
from datetime import datetime

pygame.init()

# окно
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()

# === ФОН (с сохранением пропорций) ===
bg = pygame.image.load("images/clock.jpeg").convert()

bg_rect_original = bg.get_rect()
scale_factor = HEIGHT / bg_rect_original.height
new_width = int(bg_rect_original.width * scale_factor)

bg = pygame.transform.scale(bg, (new_width, HEIGHT))
bg_rect = bg.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# === РУКА (с прозрачностью) ===
hand = pygame.image.load("images/mickey_hand-removebg-preview.png").convert_alpha()
hand = pygame.transform.scale(hand, (120, 300))

# центр часов
CENTER = (WIDTH // 2, HEIGHT // 2)


def rotate(image, angle):
    rotated = pygame.transform.rotate(image, angle)
    rect = rotated.get_rect(center=CENTER)
    return rotated, rect


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # время
    now = datetime.now()
    sec = now.second
    minute = now.minute

    # углы
    sec_angle = -sec * 6
    min_angle = -minute * 6

    # вращение
    sec_hand, sec_rect = rotate(hand, sec_angle)
    min_hand, min_rect = rotate(hand, min_angle)

    # рисуем
    screen.fill((255, 255, 255))
    screen.blit(bg, bg_rect)

    screen.blit(min_hand, min_rect)   # минутная
    screen.blit(sec_hand, sec_rect)   # секундная

    pygame.display.flip()
    clock.tick(60)

pygame.quit()