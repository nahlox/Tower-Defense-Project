import pygame
from pygame.locals import *
pygame.init()
width = 1000
height = 1000
window = pygame.display.set_mode((width,height))
bg_img = pygame.image.load('Assets/map.jpg')
bg_img = pygame.transform.scale(bg_img,(width,height))
 


while True :

    window.fill((0,0,0))
  
    window.blit(bg_img, (0, 0))
  
    
    for event in pygame.event.get() :
  
        
        if event.type == pygame.QUIT :
  
          
            pygame.quit()
  
            quit()
  
          
        pygame.display.update() 
