# coding=System

class Joueur(object):

  """
   

  :version:
  :author:
  """

  """ ATTRIBUTES

   

  life  (private)

   

  money  (private)

   

  Tours  (private)

   

  Ennemis  (private)

   

  name  (private)

  """

  def __init__(self, money_ = 100, life_ = 30):
    """
     

    @param int money_ : 
    @param float life_ : 
    @return  :
    @author
    """
    self.money = money
    seft.life = life


  def get_Money(self):
    """
     

    @return  :
    @author
    """
    return self.money


  def get_Life(self):
    """
     

    @return  :
    @author
    """
    return self.life


  def add_Money(self, prize = 0):
    """
     

    @param int prize : 
    @return  :
    @author
    """
    self.money = self.money + prize
    return self.money


  def remove_Money(self, cost = 5):
    """
     

    @param int cost : 
    @return  :
    @author
    """
    self.money = self.money - cost
    return self.money


  def add_Life(self, int = 0):
    """
     

    @param undef int : 
    @return  :
    @author
    """
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



