#Programme principal du jeu qui gère les différentes classes
from ClassGame.Joueur import Joueur
from ClassGame.Ennemi import Ennemi
from ClassGame.Projectile import Projectile
from ClassGame.Tour import Tour

#Tests 
player = Joueur()
player.create_tower(2, 5, "Tour test numero 1 ! ")
player.create_tower(1, 4 , "Tour test 2 ! ")
player.affiche()
for tour in player.get_Towers():
    tour.affiche()

# Game loop
gameOn = True
while gameOn:
    gameOn = False

