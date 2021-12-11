import pygame
from ClassGame.Ennemi import Ennemi
from ClassGame.Projectile import Projectile
class Tour():
  def __init__(self, damage = 1, name = "", frequency = 1, range = 1, posX = 0, posY = 0, price = 5):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface([20, 50])
    self.image.fill("red")
    self.rect = self.image.get_rect()
    self.damage = damage
    self.name = name
    self.frequency = frequency
    self.range = range
    self.posX = posX
    self.posY = posY
    self.price = price
  
  def affiche(self):
    print(self.name, self.damage, self.range, self.posX, self.posY)

  def get_Damage(self):
    return self.damage

  def set_Range(self, range = 1):
    self.range = range

  def set_Name(self, name):
    self.name = name

  def set_frequency(self, frequency = 1):
    self.frequency = frequency

  def set_Damage(self, damage = 1):
    self.damage = damage

  def get_frequency(self):
    return self.frequency 

  def set_PosY(self, posY = 0):
    self.posY = posY

  def set_PosX(self, posX = 0):
    self.posX = posX

  def get_Price(self):
    return self.price

  def get_Name(self):
    return self.name

  def get_Range(self):
    return self.range

  def get_PosX(self):
    return self.posX

  def get_PosY(self):
    return self.posY
  
  def isInRange(self, posA, posB):
    distance = ((posA[0] - posB[0]) ** 2 + (posA[1] - posB[1]) ** 2) ** 0.5
    if distance < self.range:
      return distance
    return False

  def send_Projectile(self, target):
    print("PROJECTILE CREATED")
    projectile = Projectile(opacity = 1, posX = self.posX, posY = self.posY, pointA = target.get_PosX(), pointB = target.get_PosY())
    damage = target.set_Damage()
    return damage
  
  def search_ennemis(self, ennemisList):
    target = False
    posTour = [self.posX, self.posY]
    for ennemi in ennemisList:
      distanceInRange = self.isInRange(posTour, [ennemi.get_PosX(), ennemi.get_PosY()])
      if distanceInRange:
        if not target:
          target = [ennemi, distanceInRange]
        elif target[0].get_distance() < ennemi.get_distance():
          target = [ennemi, distanceInRange]
    if target:
      print("TARGET FOUND : ", target[0], target[0].get_PosX())
      return self.send_Projectile(target[0])
    print("MESSAGE FROM", self.name, "NO TARGET FOUND (", self.posX, ",", self.posY, ")")
    return False

  
# récuperer True or False de Ennemi 
# if True/False => add money de Joueur
# et remove ennemi de joueur 
    
