import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

# definir colores
COLORES = ((0, 255, 0), (255, 0, 0), (0, 0, 255))
WHITE = (255, 255, 255)

size = widht, height = 800, 500
coord_x = 400
coord_y = 200
speed_x = 3
speed_y = 3
c = 0
screen = pygame.display.set_mode(size)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # zona logica-----
    if coord_x > (widht-80) or coord_x < 0:
        speed_x *= -1
    if coord_y > (height-80) or coord_y < 0:
        speed_y *= -1
    coord_x += speed_x
    coord_y += speed_y
    screen.fill(COLORES[c])

    # zona logica----
    # zona de dibujo

    cuadrado = pygame.draw.rect(screen, WHITE, (coord_x, coord_y, 80, 80))

    # zona de dibujo
    pygame.display.flip()
    c += 1
    if c > 2:
        c = 0
    clock.tick(30)
