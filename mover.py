from matplotlib import pyplot as plt
import numpy as np
import pygame

# screen = [1, 1, 2, 2, 2, 1]
# print(screen)

# screen[3] = 8
# print(screen)

# playerPos = 2
# screen[playerPos] = 8
# print(screen)

# hay q crear un fondo o una pantalla original

# background = [1, 1, 2, 2, 2, 1]
# screen = background.copy()


# playerPos = 2
# screen[playerPos] = 8
# print(screen)
size = widht, height = 600, 480
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()  # get a pygame clock object
player = pygame.transform.scale((pygame.image.load("pelota.png")), (50, 50))

background = pygame.image.load("playa.jpg")
screen.blit(background, (0, 0))  # draw the background
position = player.get_rect()
screen.blit(player, position)  # draw the player
pygame.display.update()  # and show it all
for x in range(100):  # animate 100 frames
    screen.blit(background, position, position)  # erase
    position = position.move(2, 0)  # move player
    screen.blit(player, position)  # draw new player
    pygame.display.update()  # and show it all
    clock.tick(10)
