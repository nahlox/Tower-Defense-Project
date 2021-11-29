import pygame

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

  def send_Projectile(self, id_Ennemi):
    ennimi = Joueur.get_Ennemi(id_Ennemi)
    test = Projectile()
    
# récuperer True or False de Ennemi 
# if True/False => add money de Joueur
# et remove ennemi de joueur 
    pass
