# coding=System

class Joueur(object):

  def __init__(self, money = 100, life = 30):

    self.money = money
    self.life = life


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
    """
     

    @param int damage : 
    @return  :
    @author
    """
    self.life = self.life - damage


  def create_tower(self, posX, posY):
    """
     

    @param float posX : 
    @param float posY : 
    @return  :
    @author
    """
    pass

  def next_Ennemi(self):
    """
     

    @return  :
    @author
    """
    pass



