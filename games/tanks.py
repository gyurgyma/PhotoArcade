

class game_object():
    def __init__(self, x, y, team):
        self.team = team
        self.x = x
        self.y = y
    
#
class shell(game_object):
    def __init__(self, vector, **kwargs):
        super(shell, self).__init__(**kwargs)
        self.vector = vector

class tank(game_object):
    def __init__(self, **kwargs):
        super(tank, self).__init__(**kwargs)

    def _move(self):
        pass

    def _shoot(self):
        pass
        #create shell object
