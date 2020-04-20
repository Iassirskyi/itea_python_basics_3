from random import randint


dict_all_black_cells = {}

list_let = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
list_let_a = ['A', 'C', 'E', 'G']
list_let_b = ['B', 'D', 'F', 'H']

list_1 = []
for i in range(8):
    for j in range(8):
        if i%2 != 0 and j % 2 != 0:
            list_1.append((j, i))
        elif i % 2 == 0 and j % 2 == 0:
            list_1.append((j, i))
#  print(list_1)

list_2 = []
for let in list_let:
    for i in range(1,9):
        if i%2 != 0 and let in list_let_a:
            key = let + str(i)
            list_2.append(key)
        elif i%2 == 0 and let in list_let_b:
            key = let + str(i)
            list_2.append(key)
#  print(list_2)


dict_all_black_cells = {key: value for key, value in zip(list_2, list_1)}
#print(dict_all_black_cells)


class GameDesk:

    def __init__(self):

        self._n = 8
        self._m = 8
        self._desk = self._generate_desk()
        #  self._put_objects(object)

    def __str__(self):

        game_desk = self._show_desk()
        return game_desk

    def put_char(self, object):
        """
        This is a function witch put Bot and Player army on Desk.
        :param char: string
        :type char: object
        """
        for a in object.get_army_dsk():
            if a.king is None:
                self._desk[a.x][a.y] = str(object)
            else:
                self._desk[a.x][a.y] = a.king

    def move_char(self, char, x, y):
        """
        This is a function witch change coordinate Player or Bot on Desk.
        :param char: string
        :param x: coordinate x
        :param y: coordinate y
        :type char: object
        :type x: int
        :type y: int
        """
        self._desk[x][y] = str(char)

    def get_obj(self, x, y):
        """
        This is a function witch get symbol from Desk by coordinate x, y.
        :param x: coordinate x
        :param y: coordinate y
        :type x: int
        :type y: int
        """
        obj = self._desk[x][y]

        return obj

    def _generate_desk(self):

        game_desk = [[' ' for i in range(self._m)] for i in range(self._n)]

        return game_desk

    def _show_desk(self):

        game_desk = []
        game_desk.append('\n    A B C D E F G H   \n\n')

        for index, row in enumerate(self._desk):

            game_desk.append(f'{index + 1}  |')

            for i in row:
                game_desk.append(f'{i}|')
            game_desk.append(f'  {index + 1}')
            game_desk.append('\n')

        game_desk.append('\n    A B C D E F G H   \n')

        return ''.join(game_desk)


if __name__ == '__main__':

    list = ['A1', 'A3', 'B2']
    game_desk = GameDesk()
    game_desk.put_char(list)
    print(game_desk)
