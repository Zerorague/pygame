import pygame
import random
from screeninfo import get_monitors

pygame.init()


class Objetivo(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(
            "./img/objetivo.png").convert_alpha(), (50, 50))
        # obtener coordenadas
        self.image = self.image.get_rect()


pygame.mouse.set_visible(0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MONITOR = (get_monitors().__str__())
RESOLUCION = (1920, 1080)


screen = pygame.display.set_mode(RESOLUCION)
clock = pygame.time.Clock()

done = False

background = pygame.transform.scale(pygame.image.load(
    "./img/background.jpg").convert(), RESOLUCION)


screen.blit(background, (0, 0))
pelota_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()
for obj in range(50):
    pelota = Objetivo()
    pelota.rect.x = random.randrange(1920)
    pelota.rect.y = random.randrange(1080)

    pelota_list.add(pelota)
    all_sprite_list.add(pelota)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(background, (0, 0))
    all_sprite_list.draw(screen)

    pygame.display.flip()
