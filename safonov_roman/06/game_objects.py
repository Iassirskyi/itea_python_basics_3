class Items:


    def get_coords(self, x, y):

        self._x = x
        self._y = y


    def give_coords(self):

        return self._x, self._y

    def respond(self):
        resp = [(self._x, self._y), self._name]
        return resp


class Trap(Items):

    def __init__(self):
        self._name = 'Trap'

    def __str__(self):
        return '*'


class Heal(Items):
    
    def __init__(self):
        self._name = 'Heal'

    def __str__(self):
        return '*'

class Chest(Items):
    
    def __init__(self):
        self._name = 'Chest'

    def __str__(self):
        return '*'


GAME_OBJECTS = [Trap, Heal]
CHEST = [Chest]
