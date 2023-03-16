import pygame
import sys
import random

pygame.init()
icon = pygame.transform.scale(
    (pygame.image.load("./img/pacman.png")), (20, 20))
pygame.display.set_caption("lluvia")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
# COLORES---
WHITE = (255, 255, 255)
RGB = ((255, 0, 0), (0, 255, 0), (0, 0, 255))
# GEOMETRIA---
size = width, height = 800, 500
screen = pygame.display.set_mode(size)
c = 0
coordenadas = []
for i in range(60):  # numero de circulos
    x = random.randint(0, width)
    y = random.randint(0, height)
    tam = random.randint(2, 20)

    coordenadas.append([x, y])
# Geometria---
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(WHITE)

    for j in coordenadas:
        x = j[0]
        y = j[1]
        pygame.draw.circle(screen, RGB[c], (x, y), tam)
        c += 1
        if c > 2:
            c = 0
        j[1] += 1
        if j[1] > height:
            j[1] = 0
    pygame.display.flip()
    clock.tick(60)
