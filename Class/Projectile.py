class Projectile(object):

  def __init__(self, opacity = 0, posX = 0, posY = 0, pointA = 0, pointB = 0, velocity = 50):
    self.opacity = opacity
    self.posX = posX
    self.posY = posY
    self.pointA = pointA
    self.pointB = pointB
    self.velocity = velocity

  def get_posX(self):
    return self.posX

  def get_posY(self):
    return self.posY

  def get_velocity(self):
    return self.velocity

  def set_direction(self, direction):
    self.direction = direction

  def get_opacity(self):
    return self.opacity

  def get_pointA(self):
    return self.pointA


  def get_pointB(self):
    return self.pointB

  def affiche(self): 
    print(self.posY, self.posX, self.pointA, self.pointB, self.opacity, self.velocity)

projectile1 = Projectile()
projectile1.affiche()

