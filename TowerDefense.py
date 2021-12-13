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
sysfont = pygame.font.get_default_font()

font = pygame.font.SysFont(None, 48)

BLACK = 255, 255, 255  # parenthèses inutiles, l'interpréteur reconnaît un tuple
TILESIZE = 50
# Creation de la map
gameMap = Map(map_test, "Level 1")
# Creation d'un joueur
player = Joueur(gameMap)
# Vague d'ennemis
vagueEnnemi = ["1", "2", "3", "2", "1", "1","1", "2", "3", "2", "1", "1","1", "2", "3", "2", "1", "1", "1", "1","1", "2", "3", "2", "1", "1","1","1", "2", "3", "2", "1", "1", "1", "1","1", "2", "3", "2", "1", "1",] # 3 types d'ennemis
# On ajoute les ennemis a la liste d'ennemie du joueur :
player.add_Enemmi(vagueEnnemi)
# Creation d'une tour
player.create_tower(5 * TILESIZE - 25, 3 * TILESIZE - 25, "Super Tour", range = 3 * TILESIZE)
# Creation d'une deuxième tour
player.create_tower(12 * TILESIZE - 25, 3 * TILESIZE - 25 , "Tour d'archer", range = 3 * TILESIZE)
player.create_tower(14 * TILESIZE - 25, 10 * TILESIZE - 25 , "Tour d'archer", range = 3 * TILESIZE)

# Log du joueur
player.affiche()
player.next_Ennemi()

# Game loop
gameOn = True
fenetre = pygame.display.set_mode((750, 750))
background = pygame.Surface(fenetre.get_size())



def update():
    font1 = pygame.font.SysFont('chalkduster.ttf', 50)
    img = font1.render("Argent :" + str(player.get_Money()), True, BLACK)
    fenetre.blit(img, (5, 5))
    pygame.display.flip()
    clock.tick(100)

def drawMap():
    green = (40,255,30)
    brown = (87, 49, 49)
    blue =  (0, 22, 219)
    yellow = (184, 181, 55)
    black = (0, 0, 0)
    red = (255, 13, 0)
    # -1 = Nothing
    # 0 = herbe
    # 1 = Pierre de départ
    # 2 = Chemin
    # 3 = Pont
    # 4 = Eau
    # 5 = Tour d'arrivée

    colors = [green, black, yellow, brown, blue, black]
    
    activeMap = player.get_map().get_mapModel()

    for i in range(0, len(activeMap)):
        for j in range(0, len(activeMap[i])):
            pygame.draw.rect(fenetre, colors[activeMap[i][j]], pygame.Rect(j * TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
    for towers in player.get_Towers():
        pygame.draw.circle(fenetre, black, (towers.get_PosX(), towers.get_PosY()), TILESIZE/4)


def render():
    drawMap()
    for ennemi in player.get_Ennemis():
        if ennemi.get_Delay() <= 0:
            pygame.draw.circle(fenetre, (120, 120, 120), (ennemi.get_PosX(), ennemi.get_PosY()), 10)

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
                if ennemi.get_Delay() <= 0:
                    ennemi.walk(player.get_map())
                else:
                    ennemi.set_Delay(ennemi.get_Delay() - 1)
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

