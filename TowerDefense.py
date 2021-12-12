#Programme principal du jeu qui gère les différentes classes
from time import sleep, time
from ClassGame.Joueur import Joueur
from ClassGame.Ennemi import Ennemi
from ClassGame.Projectile import Projectile
from ClassGame.Tour import Tour
from ClassGame.mapBrouillon import map_test
from ClassGame.ClassMap import Map
import pygame

# Before you can do much with pygame, you will need to initialize it
pygame.init()
# Init de clock
clock = pygame.time.Clock()

BLACK = 255, 255, 255  # parenthèses inutiles, l'interpréteur reconnaît un tuple

# Creation de la map
gameMap = Map(map_test, "Level 1")
# Creation d'un joueur
player = Joueur(gameMap)
# Vague d'ennemis
vagueEnnemi = ["1", "2", "3", "2", "1", "1"] # 3 types d'ennemis
# On ajoute les ennemis a la liste d'ennemie du joueur :
player.add_Enemmi(vagueEnnemi)
# Creation d'une tour
player.create_tower(2, 5, "Super Tour", range=5)
# Creation d'une deuxième tour
player.create_tower(1, 4 , "Tour d'archer", range=5)
# Log du joueur
player.affiche()
player.next_Ennemi()

# Game loop
gameOn = True
fenetre = pygame.display.set_mode((750, 750))
background = pygame.Surface(fenetre.get_size())


def render():
    
    for ennemi in player.get_Ennemis():
        pygame.draw.circle(fenetre, (255, 200, 255), (ennemi.get_PosX(), ennemi.get_PosY()), 10)

def update():
    pygame.display.flip()
    clock.tick(100)


while gameOn:
    # loop
    # Création d'une image de la taille de la fenêtre
    background.fill(BLACK)
    fenetre.blit(background, (0, 0))
    while (len(player.get_EnnemisList()) != 0 or len(player.get_Ennemis()) != 0) and gameOn:
        if len(player.get_Ennemis()) != 0: #Si il y a des ennemis sur le plateau
            player.SendProjectilesOnEnnemis()  #On les recherche avec chaque tour et on tire
            for ennemi in player.get_Ennemis(): # LOG
                ennemi.logEverything()
                ennemi.walk(player.get_map())
            for ennemi in player.get_EnnemisList(): #LOG
                # print("Not on map", end=" ")
                # ennemi.logEverything() 
                pass
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOn = False
            render()
            update()
            
            
        
    gameOn = False

