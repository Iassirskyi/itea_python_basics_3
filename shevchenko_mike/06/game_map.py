from random import randint


class GameMap:

    def __init__(self, n, m, objects):

        self._n = n
        self._m = m
        self._map = self._generate_map()
        self._put_objects(objects)

    def __str__(self):

        game_map = self._show_map()
        return game_map

    def _put_objects(self, objects):

        for obj in objects:
            x = randint(0, self._n - 1)
            y = randint(0, self._m - 1)
            obj.take_coords(x, y)
            self._map[x][y] = str(obj)

    def put_char(self, char, x, y):
        self._map[x][y] = str(char)

    def moving_char(self, char, x_prev, y_prev, x_next, y_next):
        self._map[x_prev][y_prev] = ' '
        self._map[x_next][y_next] = str(char)

    def _generate_map(self):

        game_map = []

        for i in range(self._n):
            row = []

            for i in range(self._m):
                row.append(' ')

            game_map.append(row)

        return game_map

    def _show_map(self):

        game_map = []

        for row in self._map:

            game_map.append('|')

            for i in row:
                game_map.append(f'{i}|')

            game_map.append('\n')

        game_map.pop()

        return ''.join(game_map)
