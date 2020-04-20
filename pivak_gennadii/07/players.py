import game_map


class Discs:

    def __init__(self, x, y, key, color, king=None):
        self.x = x
        self.y = y
        self.key = key
        self.color = color
        self.king = king
        #  self._is_captured = False

    '''
    def move_char(self, x, y, letter):
        """
        This is a function witch write for Character new coordinate x, y.
        :param x: coordinate x
        :param y: coordinate y
        :type x: int
        :type y: int
        """
        self.x = x
        self.y = y
        self.key = letter

        return self._x, self._y
    '''

class Player:

    _initial_dsk = 12

    def __init__(self, name):

        self._name = name
        self._color = 'red'
        self._army_dsk = self._create_army_dsk()

    def __str__(self):
        return 'O'

    def _create_army_dsk(self):

        army = []

        for key, value in game_map.dict_all_black_cells.items():

            x, y = value
            if x > 4:
                dsk = Discs(x, y, key, self._color)
                army.append(dsk)

        return army

    def disc_in_army(self, charkey):
        """
        This is a function witch check disc.

        """
        is_in_army = False
        army = self._army_dsk
        for a in army:
            if charkey == a.key:
                is_in_army = True
                break
        return is_in_army

    '''def disc_indx(self, charkey):
        """
        """
        army = self._army_dsk
        indx = army.index(charkey)

        return indx
    '''
    def get_army_dsk(self):

        return self._army_dsk

    def move_desc(self, charkey, charkey_new, new_x, new_y):
        """
        This is a function witch write new coordinate desc.

        """
        army = self._army_dsk

        for count, item in enumerate(army):
            #  print(count, item.key)
            if item.key == charkey:
                indx = count
                break
        self._army_dsk.pop(indx)
        if new_x == 0:
            dsk = Discs(new_x, new_y, charkey_new, self._color, 'o')
        else:
            dsk = Discs(new_x, new_y, charkey_new, self._color)
        army.append(dsk)
        return

    def show_stats(self):

        print('Player stats: ')
        print(f'Name: {self._name}')

    def kill_disc(self, charkey):
        """
        This is a function witch kill disc.

        """
        army = self._army_dsk

        for count, item in enumerate(army):
            #  print(count, item.key)
            if item.key == charkey:
                indx = count
                break
        self._army_dsk.pop(indx)

        return


class Bot(Player):

    def __str__(self):
        return 'X'

    def __init__(self):
        self._name = 'Botichello'
        self._color = 'black'
        self._army_dsk = self._create_army_dsk()

    def _create_army_dsk(self):

        army = []

        for key, value in game_map.dict_all_black_cells.items():

            x, y = value
            if x < 3:
                dsk = Discs(x, y, key, self._color)
                army.append(dsk)

        return army

    def get_army(self):

        return self._army

    def get_name(self):

        return self._name

    def move_desc(self, charkey, charkey_new, new_x, new_y):
        """
        This is a function witch write new coordinate disc.

        """
        army = self._army_dsk

        for count, item in enumerate(army):
            #  print(count, item.key)
            if item.key == charkey:
                indx = count
                break
        self._army_dsk.pop(indx)
        if new_x == 7:
            dsk = Discs(new_x, new_y, charkey_new, self._color, 'x')
        else:
            dsk = Discs(new_x, new_y, charkey_new, self._color)
        army.append(dsk)
        return

    def kill_disc(self, charkey):
        """
        This is a function witch write new coordinate desc.

        """
        army = self._army_dsk

        for count, item in enumerate(army):
            #  print(count, item.key)
            if item.key == charkey:
                indx = count
                break
        self._army_dsk.pop(indx)

        return


PLAYERS = [Bot, Player]

