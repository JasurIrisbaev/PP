import pygame
import sys
import random
import time
from pygame.locals import *

pygame.init()

# ---------------- SETTINGS ----------------
FPS = 60
FramePerSec = pygame.time.Clock()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

SPEED = 5
SCORE = 0
LEVEL = 1

# ---------------- COLORS ----------------
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)

# ---------------- SCREEN ----------------
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer Game")

# ---------------- LOAD FILES ----------------
background = pygame.image.load("assets/AnimatedStreet.png")
player_img = pygame.image.load("assets/Player.png")
enemy_img = pygame.image.load("assets/Enemy.png")

# ---------------- SOUND ----------------
pygame.mixer.music.load("assets/background.wav")
pygame.mixer.music.play(-1)

crash_sound = pygame.mixer.Sound("assets/crash.wav")

# ---------------- FONTS ----------------
font_small = pygame.font.SysFont("Verdana", 20)
font_big = pygame.font.SysFont("Verdana", 40)

# ---------------- CLASSES ----------------

# 🚗 Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        # движение влево
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)

        # движение вправо
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


# 🚙 Enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE

        self.rect.move_ip(0, SPEED)

        # если ушёл за экран
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


# 💰 Coin
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(GOLD)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)

        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


# ---------------- OBJECTS ----------------
P1 = Player()

# несколько врагов
enemies = pygame.sprite.Group()
for i in range(2):
    enemy = Enemy()
    enemies.add(enemy)

# монета
C1 = Coin()
coins = pygame.sprite.Group()
coins.add(C1)

# все объекты
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(enemies)
all_sprites.add(C1)

# ---------------- EVENTS ----------------
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 3000)

# ---------------- GAME LOOP ----------------
while True:

    for event in pygame.event.get():

        # увеличение сложности
        if event.type == INC_SPEED:
            SPEED += 0.5

            # уровень
            if SPEED % 2 < 0.5:
                LEVEL += 1

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # фон
    DISPLAYSURF.blit(background, (0, 0))

    # счёт (справа)
    score_text = font_small.render("Score: " + str(SCORE), True, BLACK)
    DISPLAYSURF.blit(score_text, (SCREEN_WIDTH - 130, 10))

    # уровень
    level_text = font_small.render("Level: " + str(LEVEL), True, BLACK)
    DISPLAYSURF.blit(level_text, (10, 10))

    # движение и отрисовка
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # 💰 сбор монеты
    if pygame.sprite.spritecollideany(P1, coins):
        SCORE += 5
        C1.rect.top = 0
        C1.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    # 💥 столкновение
    if pygame.sprite.spritecollideany(P1, enemies):
        crash_sound.play()
        time.sleep(0.5)

        DISPLAYSURF.fill(RED)

        game_over = font_big.render("GAME OVER", True, BLACK)
        DISPLAYSURF.blit(game_over, (70, 250))

        pygame.display.update()

        for entity in all_sprites:
            entity.kill()

        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)