class Items:

    def take_coords(self, x, y):
        self._x = x
        self._y = y

    def give_coords(self):
        return self._x, self._y

    def show_coords(self):
        show_coords = [(self._x, self._y), self._name]
        return show_coords


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


class Exit(Items):
    def __init__(self):
        self._name = 'Exit'

    def __str__(self):
        return '*'


GAME_OBJECTS = [Trap, Heal]
EXIT = [Exit]
