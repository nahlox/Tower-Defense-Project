#Programme principal du jeu qui gère les différentes classes
from time import sleep, time
from ClassGame.Joueur import Joueur
from ClassGame.Ennemi import Ennemi
from ClassGame.Projectile import Projectile
from ClassGame.Tour import Tour

# Creation d'un joueur
player = Joueur()

# Vague d'ennemis
vagueEnnemi = ["1", "2", "3", "2", "1", "1"] # 3 types d'ennemis

# On ajoute les ennemis a la liste d'ennemie du joueur :
player.add_Enemmi(vagueEnnemi)

# Creation d'une tour
player.create_tower(2, 5, "Tour test numero 1 ! ", range=2)

# Creation d'une deuxième tour
player.create_tower(1, 4 , "Tour test 2 ! ", range=10)

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
            for ennemi in player.get_Ennemis():
                ennemi.logEverything()
            for ennemi in player.get_EnnemisList():
                ennemi.logEverything()
            sleep(0.2)

        
    gameOn = False

