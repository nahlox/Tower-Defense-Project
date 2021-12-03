from pygame.constants import CONTROLLER_AXIS_LEFTX
from ClassGame.Ennemi import Ennemi
from ClassGame.Tour import Tour
class Joueur(object):
  def __init__(self, money = 100, life = 30):
    self.money = money
    self.life = life
    self.towers = []
    self.ennemis = []

  def get_Towers(self):
    return self.towers
  def get_Money(self):
    return self.money

  def get_Life(self):
    return self.life

  def add_Money(self, prize = 0):
    self.money = self.money + prize
    return self.money

  def remove_Money(self, cost = 5):
    self.money = self.money - cost
    return self.money

  def add_Life(self,bonus, int = 0):
    self.life = self.life + bonus

  def remove_Life(self, damage = 1):
    self.life = self.life - damage

  def create_tower(self, posX, posY, name="Tour d'Archer", damage=2, range=10):
    #We create a tower at PosX, PoxY with damage of 2 and range of 10
    newTower = Tour(damage=damage, name=name, range=range, posX=posX, posY=posY)
    #We save this tower in the Player
    self.towers.append(newTower)
  
  def remove_Ennemi(self, id): 
    del self.ennemis[id]

  def next_Ennemi(self):
    pass

  def affiche(self):
    print("Money & Life", self.money, self.life)
    print("Towers", self.towers)
    print("Ennemis", self.ennemis)


  def set_DamagetoEnnemi(self, ennemi, damage):
    pass