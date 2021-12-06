class Ennemi(object):
  def __init__(self, id, hp = 100, attack = 1, speed = 10, posX = 0, posY = 0, prize = 1):
    self.hp = hp
    self.attack = attack
    self.speed = speed
    self.posX = posX
    self.posY = posY
    self.prize = prize
    self.id = id
    self.distanceParcourue = 0
    self.turningpoints = []
    

  def set_Damage(self, damage = 1):
    self.hp -= damage
    if self.hp <= 0:
      return True 
    return False
  
  def get_distance(self):
    return self.distanceParcourue
  def get_Hp(self):
    return self.hp
    
  def get_Attack(self):
    return self.attack

  def get_Speed(self):
    return self.speed

  def get_PosX(self):
    return self.posX

  def get_PosY(self):
    return self.posY

  def get_Prize(self):
    return self.prize

  def affiche(self): 
    print(self.posX, self.hp, self.speed, self.posY, self.prize, self.attack)