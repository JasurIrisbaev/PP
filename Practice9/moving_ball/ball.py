import pygame

WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 25
STEP = 20

def run_ball():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Moving Ball")

    x = WIDTH // 2
    y = HEIGHT // 2

    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (255, 0, 0), (x, y), BALL_RADIUS)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x - STEP - BALL_RADIUS >= 0:
                    x -= STEP

                elif event.key == pygame.K_RIGHT and x + STEP + BALL_RADIUS <= WIDTH:
                    x += STEP

                elif event.key == pygame.K_UP and y - STEP - BALL_RADIUS >= 0:
                    y -= STEP

                elif event.key == pygame.K_DOWN and y + STEP + BALL_RADIUS <= HEIGHT:
                    y += STEP

        clock.tick(60)

    pygame.quit()




if __name__ == "__main__":
    run_ball()