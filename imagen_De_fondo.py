import pygame

screen = pygame.display.set_mode([720, 720])
clock = pygame.time.Clock()

done = False

# carga de imagen
backGround = pygame.transform.scale(
    pygame.image.load("./img/playa.jpg").convert(), [720, 720])
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(backGround, [0, 0])
    pygame.display.flip()

pygame.quit()
