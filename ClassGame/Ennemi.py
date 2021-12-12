class Ennemi(object):
  def __init__(self, id, hp = 100, attack = 1, speed = 10, posX = 0, posY = 0, prize = 1, direction = "right"):
    self.hp = hp
    self.attack = attack
    self.speed = speed
    self.posX = posX
    self.posY = posY
    self.direction = direction
    self.prize = prize
    self.id = id
    self.distanceParcourue = 0
    self.turningpoints = []
    

  def set_Damage(self, damage = 1):
    self.hp -= damage
    if self.hp <= 0:
      return self.prize 
    return False
  
  def get_distance(self):
    return self.distanceParcourue

  def walk(self, map):
    # Faire un appel à la map en indiquant la position, la map doit lui renvoyer la direction à prendre (right / left / up / down)
    self.direction = map.get_Direction(self.posX, self.posY, self.direction)
    if self.direction == "right":
      self.posX = self.posX + 0.1 * self.speed
    elif self.direction == "left":
      self.posX = self.posX - 0.1 * self.speed
    elif self.direction == "up":
      self.posY = self.posY - 0.1 * self.speed
    elif self.direction == "down":
      self.posY = self.posY + 0.1 * self.speed
    self.distanceParcourue = self.distanceParcourue + 0.01 * self.speed
    
    pass
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
  
  def get_Id(self):
    return self.id

  def affiche(self): 
    print(self.posX, self.hp, self.speed, self.posY, self.prize, self.attack)

  def logEverything(self):
    print("MESSAGE FROM ennemi n°", self.id, ": Still alive (", round(self.posX, 2), ",", round(self.posY, 2), ") hp :", self.hp)