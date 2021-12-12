from pygame.locals import *
import pygame, sys

#couleurs
green = (40,255,30)
brown = (40,60,90)
blue =  (150, 25, 0, 20)
yellow = (0,155,155)
silver = (192,192,192)

grass = 0
dirt = 1
water = 2
bridge = 3
stone = 4

colours = {
    grass: green,
    dirt: yellow,
    water: blue,
    bridge : brown,
    }

tilemap = [
        [stone,grass,grass,grass, grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass],
        [dirt,dirt,dirt,dirt, dirt,dirt,dirt,dirt,dirt,dirt,dirt,dirt,dirt,grass,grass,grass,grass],
        [grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,dirt,grass,grass,grass,grass],
        [grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,dirt,grass,grass,grass,grass],
        [grass,grass,grass,grass, grass,grass,grass,grass,grass,grass,dirt,grass,grass,grass,grass],
        [grass,grass,grass,grass, grass,grass,grass,grass,grass,grass,dirt,grass,grass,grass,grass],
        [grass,grass,grass,dirt, dirt,dirt,dirt,grass,grass,grass,dirt,grass,grass,grass,grass],
        [grass,grass,grass,dirt, grass,grass,dirt,grass,grass,grass,dirt,grass,grass,grass,grass],
        [water,water,water,bridge,water,water,bridge,water,water,bridge,water,water,water,water,water,],
        [water,water,water,bridge,water,water,bridge,water,water,bridge,water,water,water,water,water,],
        [grass,grass,grass,dirt, grass,grass,dirt,grass,grass,grass,dirt,grass,grass,grass,grass],
        [grass,grass,grass,dirt, grass,grass,dirt,grass,grass,grass,dirt,grass,grass,grass,grass],
        [dirt,dirt,dirt,dirt, grass,grass,grass,dirt,dirt,dirt,dirt,grass,grass,grass,grass],
        [grass,grass,grass,grass, grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass],
        [grass,grass,grass,grass, grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass],
        

        ]

TILESIZE = 50
MAPWIDTH =  750
MAPHEIGHT = 750

pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))
while True:


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    pygame.display.update()