import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

# definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

size = widht, height = 800, 500

screen = pygame.display.set_mode(size)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # zona de dibujo

    for i in range(10, 250, 3):
        screen.fill(BLACK)
        circulo = pygame.draw.circle(screen, RED, [400, 250], i, 5)
        pygame.display.update(circulo)
        clock.tick(60)

    # zona de dibujo
    screen.fill(BLACK)
    pygame.display.flip()
