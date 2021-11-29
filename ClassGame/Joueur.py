from ClassGame.Ennemi import Ennemi
import Tour
class Joueur(object):
  def __init__(self, money = 100, life = 30):
    self.money = money
    self.life = life
    self.towers = []
    self.ennemis = []

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

  def create_tower(self, posX, posY):
    if posX and posY : 
      newTower = Tour.Tour(damage=2, name="Tour d'Archer", range=10, posX=posX, posY=posY)
      self.towers = self.towers.append(newTower)
    pass
  
  def remove_Ennemi(self, id): 
    self.ennemis.remove(Ennemi(id))

  def next_Ennemi(self):
    pass

  def affiche(self):
    print(self.money, self.life)

joueur1 = Joueur() 
joueur1.affiche()