class Tour(object):
    def __init__(self, damage = 1, name = "Untitled", frequency = 1, range = 1, posX = 0, posY = 0, price = 5):
        self.damage = damage
        self.name = name
        self.frequency = frequency 
        self.range = range
        self.posX = posX
        self.posY = posY
        self.price = price

    def set_Range(self, range = 1):
        self.range = range

    def set_Name(self, name):
       self.name = name

    def set_Frequency_(self, frequency = 1):
        self.frequency = frequency

    def set_Damage(self, damage = 1):
        self.damage = damage

    def set_PosY(self, posY = 0):
        self.posY = posY

    def set_PosX(self, posX = 0):
        self.posX = posX

    def get_Damage(self):
        return self.damage
    
    def get_Frequency_(self):
        return self.frequency 

    def get_Price(self):
        return self.price


    def get_Name(self):
        return self.name


    def get_Range(self):
        return self.range


    def get_PosX(self):
        return self.posX


    def get_PosY(self):
        return self.posY
