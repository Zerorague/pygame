import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

ANCHO = 900
ALTO = 600


class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(
            "./img/meteor.png").convert_alpha(), (30, 30))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 2

        if self.rect.y > ALTO:
            self.rect.y = -10
            self.rect.x = random.randrange(ANCHO)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(
            "./img/player.png").convert_alpha(), (100, 100))
        self.rect = self.image.get_rect()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x = mouse_pos[0]
        player.rect.y = mouse_pos[1]


pygame.init()
pygame.mouse.set_visible(0)
screen = pygame.display.set_mode([ANCHO, ALTO])
clock = pygame.time.Clock()
done = False
score = 0

meteor_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

for i in range(100):
    meteor = Meteor()
    meteor.rect.x = random.randrange(ANCHO)
    meteor.rect.y = random.randrange(ALTO)

    meteor_list.add(meteor)
    all_sprite_list.add(meteor)

player = Player()
all_sprite_list.add(player)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    all_sprite_list.update()

    meteor_hit_list = pygame.sprite.spritecollide(player, meteor_list, True)

    for meteor in meteor_hit_list:
        score += 1
        print(score)

    screen.fill(WHITE)

    all_sprite_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)
