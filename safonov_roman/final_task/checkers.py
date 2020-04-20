class Checkers:

    def __init__(self, x, y):

        self._x = x
        self._y = y
        self._color = None
        self._type = None

    #piece, king

    def __str__(self):
        icon = ''

        if self._color == 'black':
            icon = 'X'
        elif self._color == 'white':
            icon = 'O'

        return icon

    def give_coords(self):
        return self._x, self._y

    def get_coords(self, destination):
        self._x = destination[0]
        self._y = destination[1]

    def give_type(self):
        return self._type

    def get_type(self, type):
        self._type = type

    def give_colour(self):
        return self._color

class W_Piece(Checkers):

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._type = 'piece'
        self._color = 'white'

    def __str__(self):
        return 'O'

class B_Piece(Checkers):

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._type = 'piece'
        self._color = 'black'

    def __str__(self):
        return 'X'

TYPES = [W_Piece,B_Piece]