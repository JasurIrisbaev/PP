import pygame
import math
import datetime

WIDTH = 600
HEIGHT = 600


def run_clock():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mickey Clock")

    center = (WIDTH // 2, HEIGHT // 2)
    radius = 200

    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill((255, 255, 255))

        # draw clock circle
        pygame.draw.circle(screen, (0, 0, 0), center, radius, 3)

        now = datetime.datetime.now()
        seconds = now.second
        minutes = now.minute

        # calculate angles
        sec_angle = math.radians(seconds * 6 - 90)
        min_angle = math.radians(minutes * 6 - 90)

        # seconds hand
        sec_x = center[0] + 180 * math.cos(sec_angle)
        sec_y = center[1] + 180 * math.sin(sec_angle)

        # minutes hand
        min_x = center[0] + 140 * math.cos(min_angle)
        min_y = center[1] + 140 * math.sin(min_angle)

        # draw hands
        pygame.draw.line(screen, (255, 0, 0), center, (sec_x, sec_y), 3)
        pygame.draw.line(screen, (0, 0, 255), center, (min_x, min_y), 5)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(1)

    pygame.quit()


if __name__ == "__main__":
    run_clock()