#Programme principal du jeu qui gère les différentes classes
from ClassGame.Joueur import Joueur
from ClassGame.Ennemi import Ennemi
from ClassGame.Projectile import Projectile
from ClassGame.Tour import Tour

# Creation d'un joueur
player = Joueur()

#Vague d'ennemis
vagueEnnemi = ["1", "2", "3", "2", "1", "1"] # 3 types d'ennemis

# On ajoute les ennemis a la liste d'ennemie du joueur :
player.add_Enemmi(vagueEnnemi)

# Creation d'une tour
player.create_tower(2, 5, "Tour test numero 1 ! ")

#Creation d'une deuxième tour
player.create_tower(1, 4 , "Tour test 2 ! ")


# Log du joueur
player.affiche()

# Log des tours
for tour in player.get_Towers():
    tour.affiche()

# log des enemis 
print(player.get_Ennemis())
for Ennemi in player.get_Ennemis():
    print("test")
    Ennemi.affiche
# Game loop
gameOn = True
while gameOn:
    gameOn = False

