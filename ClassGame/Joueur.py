from time import sleep
from ClassGame.Ennemi import Ennemi
from ClassGame.Tour import Tour
import random
class Joueur(object):
  def __init__(self, map, money = 100, life = 30 ):
    self.money = money
    self.life = life
    self.map = map
    self.towers = []
    self.vagueEnnemi = []
    self.ennemisList = []
    self.ennemis = []
    
  def get_Towers(self):
    return self.towers
  def get_Money(self):
    return self.money
  def get_Ennemis(self):
    return self.ennemis
  def get_map(self):
    return self.map
  def get_EnnemisList(self):
    return self.ennemisList
  def get_Life(self):
    return self.life

  def add_Enemmi(self, ennemis):
    if type(ennemis) == str:
      entity = Ennemi(id = len(self.ennemisList))
      self.ennemisList.append(entity)
      return
    for ennemi in ennemis:
      entity = Ennemi(id = len(self.ennemisList))
      self.ennemisList.append(entity)
  
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
    del self.ennemis[0]
    self.next_Ennemi()
    self.next_Ennemi(30 + random.randint(0, 50))


  def next_Ennemi(self, delay = 0):
    if(len(self.ennemisList) > 0):
      self.ennemisList[0].set_Delay(delay)
      self.ennemis.append(self.ennemisList[0])
      del self.ennemisList[0]
      return True
    return False

  def SendProjectilesOnEnnemis(self):
    for tour in self.towers:
      shot = tour.search_ennemis(self.get_Ennemis())
      if shot != False: #Si le shot touche un ennemi
        self.add_Money(shot) #On donne de l'argent au joueur
        print("SHOT", shot)
        self.remove_Ennemi(shot)

  def affiche(self):
    print("Money & Life", self.money, self.life)
    print("Towers", self.towers)
    print("Ennemis", self.ennemis)


  def set_DamagetoEnnemi(self, ennemi, damage):
    pass