class Map(object):
    def __init__(self, map_model, name):
        self.map = map_model
        self.name = name
    
    def get_Direction(self,  x, y, actualdirection = "right"):
        #x est entre 0 et 750
        #y est entre 
        column = x // 50
        row = y // 50
        columnRest = x % 50
        rowRest = y % 50
        if column > 15:
            column = 15
        if row > 15:
            row = 15

        if actualdirection == "right" and columnRest < 25:
            return actualdirection
        elif actualdirection == "left" and columnRest > 25:
            return actualdirection
        if actualdirection == "down" and rowRest < 25:
            return actualdirection
        elif actualdirection == "up" and rowRest > 25:
            return actualdirection
        
        stuffArround = self.locateAround(row, column)
        directions = ["up", "down", "left", "right"]
        opositDirections = ["down", "up", "right", "left" ]
        for direction in directions:
            print("ACTUAL DIRECTION IS:", actualdirection, row, column, stuffArround)
            if direction != opositDirections[directions.index(actualdirection)] and stuffArround[directions.index(direction)] not in [0, -1, 4]:
                print("RETURN 1", direction)
                return direction
        
        print("NO DIRECTION FOUND")


    def locate(self, row, column):
        return self.map[row - 1][column - 1]

    def locateAround(self, row, column):
        up, down, left, right = -1, -1, -1, -1 
        if row > 1:
            up = self.locate(int(row - 1), int(column) )
        if row < 15:
            down = self.locate(int(row + 1), int(column) )
        if column > 1:
            left = self.locate(int(row), int(column - 1))
        if column < 15:
            right = self.locate(int(row), int(column + 1))

        return up, down, left, right
