# coding=System

class Projectile(object):

  """
   

  :version:
  :author:
  """

  """ ATTRIBUTES

   

  velocity  (private)

   

  opacity  (private)

   

  posX  (private)

   

  posY  (private)

   projectile direction :
   y=Ax+B

  PointA  (private)

   projectile direction :
   y=Ax+B

  PointB  (private)

  """

  def __init__(self, opacity = 0, posX = 0, posY = 0, pointA = 0, pointB = 0, velocity = 50):
    """
     

    @param float opacity : 
    @param float posX : 
    @param float posY : 
    @param float pointA : 
    @param float pointB : 
    @param int velocity : 
    @return  :
    @author
    """
    self.opacity = opacity
    self.posX = posX
    self.posY = posY
    self.pointA = pointA
    self.pointB = pointB
    self.velocity = velocity


  def get_posX(self):
    """
     

    @return  :
    @author
    """
    return self.posX


  def get_posY(self):
    """
     

    @return  :
    @author
    """
    return self.posY


  def get_velocity(self):
    """
     

    @return  :
    @author
    """
    return self.velocity


  def set_direction(self, direction):
    """
     NOT CORRECT

    @param float direction : 
    @return  :
    @author
    """
    self.direction = direction


  def get_opacity(self):
    """
     

    @return  :
    @author
    """
    return self.opacity


  def get_pointA(self):
    """
     

    @return  :
    @author
    """
    return self.pointA


  def get_pointB(self):
    """
     

    @return  :
    @author
    """
    return self.pointB




