import pygame as pg
import sys

pg.init()

size = widht, height = 800, 500

screen = pg.display.set_mode(size)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
