import pygame, sys, random

pygame.init()

# --- SETTINGS ---
WIDTH = 400
HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0

# --- SCREEN ---
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

# --- FPS ---
clock = pygame.time.Clock()
FPS = 60

# --- COLORS ---
WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)

# --- LOAD ASSETS ---
background = pygame.image.load("assets/AnimatedStreet.png")
player_img = pygame.image.load("assets/Player.png")
enemy_img = pygame.image.load("assets/Enemy.png")

crash_sound = pygame.mixer.Sound("assets/crash.wav")
pygame.mixer.music.load("assets/background.wav")
pygame.mixer.music.play(-1)

# --- FONT ---
font = pygame.font.SysFont("Verdana", 20)
font_big = pygame.font.SysFont("Verdana", 40)

# ---------------- PLAYER ----------------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed[pygame.K_LEFT]:
                self.rect.move_ip(-5,0)

        if self.rect.right < WIDTH:
            if pressed[pygame.K_RIGHT]:
                self.rect.move_ip(5,0)

# ---------------- ENEMY ----------------
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.midtop = (random.randint(40, WIDTH-40), -50)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)

        if self.rect.top > HEIGHT:
            SCORE += 1
            self.rect.midtop = (random.randint(40, WIDTH-40), -50)

# ---------------- COIN ----------------
class Coin(pygame.sprite.Sprite):
    def __init__(self, enemies):
        super().__init__()

        # рисуем монету
        self.image = pygame.Surface((20,20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 215, 0), (10,10), 10)
        pygame.draw.circle(self.image, (255, 255, 0), (10,10), 6)

        self.rect = self.image.get_rect()
        self.spawn(enemies)

    def spawn(self, enemies):
        while True:
            x = random.randint(40, WIDTH-40)
            self.rect.midtop = (x, -50)

            # не пересекаться с enemy
            if not pygame.sprite.spritecollideany(self, enemies):
                break

    def move(self, enemies):
        self.rect.move_ip(0, SPEED)

        if self.rect.top > HEIGHT:
            self.spawn(enemies)

# --- CREATE OBJECTS ---
P1 = Player()
E1 = Enemy()
C1 = Coin([E1])

# --- GROUPS ---
enemies = pygame.sprite.Group()
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# --- SPEED EVENT ---
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# ---------------- GAME LOOP ----------------
while True:

    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # --- DRAW BACKGROUND ---
    screen.blit(background, (0,0))

    # --- MOVE ---
    P1.move()
    E1.move()
    C1.move(enemies)

    # --- DRAW ---
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    # --- COIN COLLISION ---
    if pygame.sprite.collide_rect(P1, C1):
        COINS += 1
        C1.spawn(enemies)

    # --- ENEMY COLLISION ---
    if pygame.sprite.spritecollideany(P1, enemies):
        crash_sound.play()
        pygame.time.delay(300)

        screen.fill(RED)

        game_over = font_big.render("GAME OVER", True, BLACK)
        screen.blit(game_over, (80, 250))

        pygame.display.update()
        pygame.time.delay(2000)

        pygame.quit()
        sys.exit()

    # --- TEXT ---
    score_text = font.render(f"Score: {SCORE}", True, BLACK)
    coins_text = font.render(f"Coins: {COINS}", True, BLACK)

    screen.blit(score_text, (10,10))
    screen.blit(coins_text, (10,40))

    pygame.display.update()
    clock.tick(FPS)