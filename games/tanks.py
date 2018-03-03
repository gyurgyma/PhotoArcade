from abc import ABC

class game_object(ABC):
    def __init__(self, x, y, team):
        self.team = team
        self.x = x
        self.y = y
    
#
class shell(game_object):
    def __init__(self, vector):
        super(shell, self).__init__()
        self.vector = vector

class tank(game_object):
    def __init__(self):
        super(tank, self).__init__()

    def _move(self):
        pass

    def _shoot(self):
        pass
        #create shell object
