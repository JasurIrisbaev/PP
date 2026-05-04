import pygame
import sys
from datetime import datetime
from tools import flood_fill, draw_preview_line, draw_brush

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSIS2 Paint")

clock = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)

screen.fill(WHITE)

color = BLUE
brush_size = 5

tool = "pencil"

drawing = False
start_pos = None
last_pos = None

font = pygame.font.SysFont("Arial", 20)

text_mode = False
text_input = ""
text_pos = (0,0)

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # ---------- KEYBOARD ----------
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_1:
                brush_size = 2
            if event.key == pygame.K_2:
                brush_size = 5
            if event.key == pygame.K_3:
                brush_size = 10

            if event.key == pygame.K_p:
                tool = "pencil"
            if event.key == pygame.K_l:
                tool = "line"
            if event.key == pygame.K_f:
                tool = "fill"
            if event.key == pygame.K_t:
                tool = "text"

            # SAVE
            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                filename = datetime.now().strftime("canvas_%Y%m%d_%H%M%S.png")
                pygame.image.save(screen, filename)
                print("Saved:", filename)

            # TEXT
            if text_mode:
                if event.key == pygame.K_RETURN:
                    img = font.render(text_input, True, color)
                    screen.blit(img, text_pos)
                    text_input = ""
                    text_mode = False

                elif event.key == pygame.K_ESCAPE:
                    text_input = ""
                    text_mode = False

                else:
                    text_input += event.unicode

        # ---------- MOUSE ----------
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            last_pos = event.pos

            if tool == "fill":
                flood_fill(screen, event.pos[0], event.pos[1], color)

            if tool == "text":
                text_mode = True
                text_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            last_pos = None

            if tool == "line":
                pygame.draw.line(screen, color, start_pos, event.pos, brush_size)

        if event.type == pygame.MOUSEMOTION:

            if drawing and tool == "pencil":
                draw_brush(screen, color, last_pos, event.pos, brush_size)
                last_pos = event.pos

    # ---------- LINE PREVIEW ----------
    if drawing and tool == "line":
        temp = screen.copy()
        mouse_pos = pygame.mouse.get_pos()
        draw_preview_line(temp, start_pos, mouse_pos, color, brush_size)
        screen.blit(temp, (0,0))

    # ---------- UI ----------
    info = font.render(f"Tool: {tool} | Size: {brush_size}", True, BLACK)
    screen.blit(info, (10,10))

    if text_mode:
        txt = font.render(text_input, True, color)
        screen.blit(txt, text_pos)

    pygame.display.flip()
    clock.tick(60)