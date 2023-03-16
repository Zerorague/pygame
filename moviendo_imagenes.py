import pygame
import math

screen = pygame.display.set_mode([720, 720])
clock = pygame.time.Clock()
pygame.mouse.set_visible(0)

done = False

# carga de imagen
backGround = pygame.transform.scale(
    pygame.image.load("./img/playa.jpg").convert(), [720, 720])

player = pygame.transform.scale(
    pygame.image.load("./img/pelota.png").convert_alpha(), [50, 50])

# quitar colores
#player.set_colorkey((255, 255, 255))


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0]
    y = mouse_pos[1]

    screen.blit(backGround, [0, 0])
    screen.blit(player, [x, y])
    pygame.display.flip()

pygame.quit()
