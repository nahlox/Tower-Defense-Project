
import pygame
import pygame_menu
from pygame.locals import *

pygame.init()
width = 1000
height = 500
window = pygame.display.set_mode((width,height))
bg_img = pygame.image.load('Assets/map.jpg')
start_img = pygame.image.load('start_btn.png').convert_alpha()
exit_img = pygame.image.load('exit_btn.png').convert_alpha()

bg_img = pygame.transform.scale(bg_img,(width,height))
i = 0
surface = pygame.display.set_mode((600, 400))


def start_the_game() :
    # Do the job here!
    pass

menu = pygame_menu.Menu('Welcome', 400, 300,
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='Player')

menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

start_button = button.Button(100, 200, start_img, 0.8)
exit_button = button.Button(450, 200, exit_img, 0.8)



runing = True
while runing:
    window.fill((0,0,0))
    window.blit(bg_img,(i,0))
    menu.mainloop(window)
    for event in pygame.event.get():
        if event.type == QUIT:
            runing = False
    pygame.display.update()
pygame.quit()
