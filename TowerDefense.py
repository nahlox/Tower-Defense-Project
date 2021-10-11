from os import truncate
import sys, time, pygame
pygame.init()

size = width, height = 1000, 1000
speed = [5, 5]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
running = True
while running:
    #White screen
    screen.fill((255, 255, 255))
    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    # Actualise the display
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_UP:
             pass   

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False
    time.sleep(0.01)