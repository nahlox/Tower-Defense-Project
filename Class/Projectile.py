class Projectile(object):
    def __init__(self, opacity = 0, posX = 0, posY = 0, pointA = 0, pointB = 0):
        self.opacity = opacity
        self.posX = posX
        self.posY = posY
        self.pointA = pointA
        self.pointB = pointB

    def get_posX(self):
        return self.posX

    def get_posY(self):
        return self.posY

    def get_velocity(self):
        #Trouver la formule
        pass
        
    def get_opacity(self):
        return self.opacity

    def get_pointA(self):
        return self.pointA

    def get_pointB(self):
        return self.pointB

    def set_Direction(self, direction):
        if not direction:
            pass
        #Trouver la formule
        pass