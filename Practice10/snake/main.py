import pygame
import sys
import random

pygame.init()

# ---------------- SETTINGS ----------------
WIDTH = 600
HEIGHT = 400
BLOCK = 20
SPEED = 10

# ---------------- COLORS ----------------
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# ---------------- SCREEN ----------------
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# ---------------- SOUND ----------------
try:
    eat_sound = pygame.mixer.Sound("assets/eat.mp3")
    gameover_sound = pygame.mixer.Sound("assets/gameover.mp3")
except:
    eat_sound = None
    gameover_sound = None

# ---------------- SNAKE ----------------
snake = [(100, 100), (80, 100), (60, 100)]
dx = BLOCK
dy = 0

# ---------------- FOOD ----------------
def generate_food():
    while True:
        x = random.randrange(0, WIDTH, BLOCK)
        y = random.randrange(0, HEIGHT, BLOCK)
        if (x, y) not in snake:
            return x, y

food_x, food_y = generate_food()

score = 0
level = 1

# ---------------- FONT ----------------
font = pygame.font.SysFont("Verdana", 20)
big_font = pygame.font.SysFont("Verdana", 50)

# ---------------- GAME LOOP ----------------
running = True
game_over = False

while running:

    screen.fill(WHITE)

    # ---------- EVENTS ----------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # управление
            if event.key == pygame.K_UP and dy == 0:
                dx = 0
                dy = -BLOCK

            elif event.key == pygame.K_DOWN and dy == 0:
                dx = 0
                dy = BLOCK

            elif event.key == pygame.K_LEFT and dx == 0:
                dx = -BLOCK
                dy = 0

            elif event.key == pygame.K_RIGHT and dx == 0:
                dx = BLOCK
                dy = 0

            # restart
            if game_over and event.key == pygame.K_r:
                snake = [(100, 100), (80, 100), (60, 100)]
                dx = BLOCK
                dy = 0
                score = 0
                level = 1
                SPEED = 10
                food_x, food_y = generate_food()
                game_over = False

    if not game_over:

        # ---------- MOVE ----------
        head_x, head_y = snake[0]
        new_head = (head_x + dx, head_y + dy)

        # ---------- WALL COLLISION ----------
        if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
            game_over = True
            if gameover_sound:
                gameover_sound.play()

        # ---------- SELF COLLISION ----------
        if new_head in snake:
            game_over = True
            if gameover_sound:
                gameover_sound.play()

        snake.insert(0, new_head)

        # ---------- FOOD ----------
        if new_head == (food_x, food_y):
            score += 1
            if eat_sound:
                eat_sound.play()

            food_x, food_y = generate_food()

            # LEVEL SYSTEM
            if score % 3 == 0:
                level += 1
                SPEED += 2

        else:
            snake.pop()

    # ---------- DRAW SNAKE ----------
    for block in snake:
        pygame.draw.rect(screen, GREEN, (block[0], block[1], BLOCK, BLOCK))

    # ---------- DRAW FOOD ----------
    pygame.draw.rect(screen, RED, (food_x, food_y, BLOCK, BLOCK))

    # ---------- DRAW TEXT ----------
    score_text = font.render(f"Score: {score}", True, BLACK)
    level_text = font.render(f"Level: {level}", True, BLACK)

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH - 100, 10))

    # ---------- GAME OVER SCREEN ----------
    if game_over:
        text = big_font.render("GAME OVER", True, RED)
        restart_text = font.render("Press R to restart", True, BLACK)

        screen.blit(text, (150, 150))
        screen.blit(restart_text, (200, 220))

    pygame.display.flip()
    clock.tick(SPEED)

pygame.quit()
sys.exit()