from abc import ABC

class game_object(ABC):
    def __init__(self, x, y, team):
        self.team = team
        self.x = x
        self.y = y
    

class shell(game_object):
    def __init__(self):
        super(shell, self).__init__()
        

class tank(game_object):
    def __init__(self):
        super(tank, self).__init__()

    
