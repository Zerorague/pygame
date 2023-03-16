import sys
import pygame

pygame.init()  # inicializamos el modulo

# esto es lo mismo que crear una tupla pero se especifica como ancho el primer parametro y alto el segundo
size = widht, height = 800, 700

speed = [2, 30]

black = r, g, b = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("pelota.png")
ball = pygame.transform.scale(ball, (50, 50))
# se obtiene un area rectangular que representa a la pelota
ballRect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        ballRect = ballRect.move(speed)
        if ballRect.left < 0 or ballRect.right > widht:
            speed[0] = speed[0]*-1
        if ballRect.top < 0 or ballRect.bottom > height:
            speed[1] = speed[1]*-1

        screen.fill(black)
        screen.blit(ball, ballRect)
        pygame.display.update()
        pygame.display.flip()
