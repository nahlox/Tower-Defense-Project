#Programme principal du jeu qui gère les différentes classes
from time import sleep, time
from ClassGame.Joueur import Joueur
from ClassGame.Ennemi import Ennemi
from ClassGame.Projectile import Projectile
from ClassGame.Tour import Tour
from ClassGame.mapBrouillon import map_test
from ClassGame.ClassMap import Map
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

# Log des tours
for tour in player.get_Towers():
    print("TOUR SUR LE PLATEAU", end="  ")
    tour.affiche()

# log de la liste d'ennemis
player.next_Ennemi()
for ennemi in player.get_EnnemisList():
    print("ENNEMI EN ATTENTE", end="    ")
    ennemi.affiche()
for ennemi in player.get_Ennemis():
    print("ENNEMI SUR LE JEU", end="    ")
    ennemi.affiche()

# Game loop
gameOn = True
while gameOn:
    while len(player.get_EnnemisList()) != 0 or len(player.get_Ennemis()) != 0:
        if len(player.get_Ennemis()) != 0: #Si il y a des ennemis sur le plateau
            player.SendProjectilesOnEnnemis()  #On les recherche avec chaque tour et on tire
            for ennemi in player.get_Ennemis(): # LOG
                ennemi.logEverything()
                ennemi.walk(player.get_map())
            for ennemi in player.get_EnnemisList(): #LOG
                print("Not on map", end=" ")
                ennemi.logEverything() 
            sleep(0.01)
            
        
    gameOn = False

