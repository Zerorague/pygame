import pygame
import sys
# intento de mover imagen

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("juego cualquiera")
size = widht, height = 1000, 462
screen = pygame.display.set_mode(size)
background = pygame.transform.scale(
    (pygame.image.load("ecchi.jpg").convert()), size)

personaje = pygame.transform.scale(
    (pygame.image.load("pacman.png")), (70, 70))
personajeRect = personaje.get_rect()
x = 0
y = 0


while True:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if keys[pygame.K_RIGHT]:
        personajeRect.right += 10
    elif personajeRect.right >= widht:
        personajeRect.right = 0
    elif keys[pygame.K_LEFT]:
        personajeRect.left -= 10
    elif keys[pygame.K_UP]:
        personajeRect.top -= 10
    elif keys[pygame.K_DOWN]:
        personajeRect.bottom += 10
    else:
        pass

    screen.fill((50, 30, 60))
    screen.blit(personaje, personajeRect)

    pygame.display.update()
    pygame.display.flip()
    clock.tick(40)
