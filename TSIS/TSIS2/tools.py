import pygame
from collections import deque
import math

# ---------- SMOOTH BRUSH ----------
def draw_brush(surface, color, start, end, size):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    distance = max(abs(dx), abs(dy))

    if distance == 0:
        pygame.draw.circle(surface, color, start, size)
        return

    for i in range(distance):
        x = int(start[0] + dx * i / distance)
        y = int(start[1] + dy * i / distance)
        pygame.draw.circle(surface, color, (x, y), size)


# ---------- FLOOD FILL ----------
def flood_fill(surface, x, y, new_color):
    width, height = surface.get_size()
    target_color = surface.get_at((x, y))

    if target_color == new_color:
        return

    queue = deque([(x, y)])

    while queue:
        px, py = queue.popleft()

        if px < 0 or px >= width or py < 0 or py >= height:
            continue

        if surface.get_at((px, py)) != target_color:
            continue

        surface.set_at((px, py), new_color)

        queue.append((px+1, py))
        queue.append((px-1, py))
        queue.append((px, py+1))
        queue.append((px, py-1))


# ---------- LINE PREVIEW ----------
def draw_preview_line(screen, start, end, color, size):
    pygame.draw.line(screen, color, start, end, size)