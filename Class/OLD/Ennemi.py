class Ennemi(object):
    def __init__(self, life = 100, attack = 1, speed = 10, posX = 0, posY = 0, prize = 1):
        self.life = life
        self.attack = attack
        self.speed = speed
        self.posX = posX
        self.posY = posY
        self.prize = prize

    def get_Life(self):
        return self.life
    
    def get_Attack(self):
        return self.attack

    def get_Speed(self):
        return self.speed

    def get_posX(self):
        return self.posX
    
    def get_posY(self):
        return self.posY
    
    def get_prize(self):
        return self.prize
    
    def set_attack(self, attack):
        self.attack = attack

    def set_speed(self, speed):
        self.speed = speed

    def set_posX(self, posX):
        self.posX = posX
    
    def set_posY(self, posY):
        self.posY = posY

    def set_prize(self, prize):
        self.prize = prize
    
    def remove_Life(self, damage = 1):
        self.life = self.life - damage
        return self.life
    
    