# coding=System
from Projectile import *

class Tour(object):

  """
   

  :version:
  :author:
  """

  """ ATTRIBUTES

   

  damage  (private)

   

  name  (private)

   

  frequency  (private)

   

  range  (private)

   

  posX  (private)

   

  posY  (private)

   

  price  (private)

   

  id  (private)

   

  Projectiles  (private)

  """

  def __init__(self, damage = 1, name = "Untitled", frequency = 1, range = 1, posX = 0, posY = 0, price = 5):
    """
     

    @param float damage : 
    @param string name : 
    @param float frequency : 
    @param float range : 
    @param float posX : 
    @param float posY : 
    @param int price : 
    @return  :
    @author
    """
    self.damage = damage
    self.name = name
    self.frequency = frequency
    self.range = range
    self.posX = posX
    self.posY = posY
    self.price = price
    


  def get_Damage(self):
    """
     

    @return float :
    @author
    """
    return self.damage


  def set_Range(self, range = 1):
    """
     

    @param float range : 
    @return  :
    @author
    """
    self.range = range


  def set_Name(self, name):
    """
     

    @param string name : 
    @return  :
    @author
    """
    self.name = name


  def set_Frequency_(self, frequency = 1):
    """
     

    @param float frequency_ : 
    @return  :
    @author
    """
    self.frequency = frequency


  def set_Damage(self, damage = 1):
    """
     

    @param float damage : 
    @return  :
    @author
    """
    self.damage = damage


  def get_Frequency_(self):
    """
     

    @return float :
    @author
    """
    return self.frequency 


  def set_PosY(self, posY = 0):
    """
     

    @param float posY : 
    @return  :
    @author
    """
    self.posY = posY


  def set_PosX(self, posX = 0):
    """
     

    @param float posX : 
    @return  :
    @author
    """
    self.posX = posX


  def get_Price(self):
    """
     

    @return int :
    @author
    """
    return self.price


  def get_Name(self):
    """
     

    @return string :
    @author
    """
    return self.name


  def get_Range(self):
    """
     

    @return float :
    @author
    """
    return self.range


  def get_PosX(self):
    """
     

    @return float :
    @author
    """
    return self.posX


  def get_PosY(self):
    """
     

    @return float :
    @author
    """
    return self.posY




