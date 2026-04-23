import pygame

pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

color = BLUE
radius = 5
mode = "draw"

drawing = False
last_pos = None
start_pos = None

font = pygame.font.SysFont("Arial", 20)

screen.fill(WHITE)

# ---- Smooth line function ----
def draw_line(surface, color, start, end, width):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    distance = max(abs(dx), abs(dy))

    for i in range(distance):
        x = int(start[0] + dx * i / distance)
        y = int(start[1] + dy * i / distance)
        pygame.draw.circle(surface, color, (x, y), width)

# ---- MAIN LOOP ----
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # -------- KEYBOARD --------
        if event.type == pygame.KEYDOWN:

            # Colors
            if event.key == pygame.K_r:
                color = RED
                mode = "draw"
            elif event.key == pygame.K_g:
                color = GREEN
                mode = "draw"
            elif event.key == pygame.K_b:
                color = BLUE
                mode = "draw"

            # Tools
            elif event.key == pygame.K_e:
                mode = "erase"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_t:
                mode = "rect"

            # Brush size
            elif event.key == pygame.K_UP:
                radius += 2
            elif event.key == pygame.K_DOWN:
                radius = max(1, radius - 2)

            # Clear screen
            elif event.key == pygame.K_x:
                screen.fill(WHITE)

            # Save image
            elif event.key == pygame.K_s:
                pygame.image.save(screen, "my_drawing.png")
                print("Saved!")

        # -------- MOUSE --------
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            last_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False

            if mode == "rect":
                end = event.pos
                rect = pygame.Rect(start_pos, (end[0]-start_pos[0], end[1]-start_pos[1]))
                pygame.draw.rect(screen, color, rect, 2)

            elif mode == "circle":
                end = event.pos
                radius_c = int(((end[0]-start_pos[0])**2 + (end[1]-start_pos[1])**2) ** 0.5)
                pygame.draw.circle(screen, color, start_pos, radius_c, 2)

        elif event.type == pygame.MOUSEMOTION and drawing:
            if mode == "draw":
                draw_line(screen, color, last_pos, event.pos, radius)

            elif mode == "erase":
                draw_line(screen, WHITE, last_pos, event.pos, radius)

            last_pos = event.pos

    # ---- UI TEXT ----
    info = f"Mode: {mode} | Size: {radius}"
    text = font.render(info, True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()