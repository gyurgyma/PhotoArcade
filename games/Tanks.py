

class GameObject():
    def __init__(self, x, y, team):
        self.team = team
        self.x = x
        self.y = y


class Shell(GameObject):
    def __init__(self, vector, **kwargs):
        super(Shell, self).__init__(**kwargs)
        self.vector = vector


class Tank(GameObject):
    def __init__(self, **kwargs):
        self.is_alive = True
        super(Tank, self).__init__(**kwargs)
        self.shell = Shell()

    def _move(self):
        pass

    def shoot(self):
        pass
        # create shell object

    def reset_shell(self):
        self.shell.vector = [(0, 0), (0, 0)]
        self.shell.x = self.x
        self.shell.y = self.y

def _destroy(self):
        pass

    def destroy(self):
        self.is_alive = False
        pass

