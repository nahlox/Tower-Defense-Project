class Player(object):
    def __init__(self, life = 100, money = 100):
        self.life = life
        self.money = money

    def get_Money(self):
        return self.money
    
    def get_Life(self):
        return self.life

    def add_Money(self, prize):
        self.money = self.money + prize

    def remove_Money(self, cost):
        if self.money >= cost:
            self.money = self.money - cost
            return 202
        return 406

    def add_Life(self, bonus : 0):
        self.life = self.life + bonus
        return self.life
    
    def remove_Life(self, damage = 1):
        self.life = self.life - damage
        return self.life