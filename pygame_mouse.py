import pygame
import sys


class Mouse():
    def __init__(self) -> None:
        self.size = (800, 500)
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        pygame.init()
        self.x = 10
        self.y = 10
        self.xSpeed = 0
        self.ySpeed = 0

    def loop(self):
        pygame.mouse.set_visible(0)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # ----------mover con mouse-------
            # mouse_pos = pygame.mouse.get_pos()
            # x = mouse_pos[0]
            # y = mouse_pos[1]
            # ----------mover con mouse-------
            # eventos teclado---
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.xSpeed = -3
                    if event.key == pygame.K_RIGHT:
                        self.xSpeed = 3
                    if event.key == pygame.K_DOWN:
                        self.ySpeed = 3
                    if event.key == pygame.K_UP:
                        self.ySpeed = -3
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.xSpeed = 0
                    if event.key == pygame.K_RIGHT:
                        self.xSpeed = 0
                    if event.key == pygame.K_DOWN:
                        self.ySpeed = 0
                    if event.key == pygame.K_UP:
                        self.ySpeed = 0
            self.screen.fill((255, 255, 255))
            self.x += self.xSpeed
            self.y += self.ySpeed

            pygame.draw.rect(self.screen, (255, 0, 0),
                             (self.x, self.y, 50, 100))

            pygame.display.flip()
            self.clock.tick(60)


Juego = Mouse()

Juego.loop()
