# coding=System

class Ennemi(object):

  """
   

  :version:
  :author:
  """

  """ ATTRIBUTES

   

  hp  (private)

   

  attack  (private)

   

  speed  (private)

   

  pos_x  (private)

   

  pos_y  (private)

   

  prize  (private)

   

  id  (private)

  """

  def __init__(self, hp = 100, attack = 1, speed = 10, posX = 0, posY = 0, prize = 1):
    """
     

    @param int hp : 
    @param int attack : 
    @param int speed : 
    @param float posX : 
    @param float posY : 
    @param int prize : 
    @return  :
    @author
    """
    self.hp = hp
    self.attack = attack
    self.speed = speed
    self.posX = posX
    self.posY = posY
    self.prize = prize


  def set_Damage(self, damage = 1):
    """
     

    @param int damage : 
    @return  :
    @author
    """
    self.damage = damage


  def get_Hp(self):
    """
     

    @return  :
    @author
    """
    return self.hp


  def get_Attack(self):
    """
     

    @return  :
    @author
    """
    return self.attack


  def get_Speed(self):
    """
     

    @return  :
    @author
    """
    return self.speed


  def get_PosX(self):
    """
     

    @return  :
    @author
    """
    return self.posX


  def get_PosY(self):
    """
     

    @return  :
    @author
    """
    return self.posY


  def get_Prize(self):
    """
     

    @return  :
    @author
    """
    return self.prize




