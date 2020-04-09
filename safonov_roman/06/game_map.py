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


    def _put_objects (self, objects):

        for obj in objects:
            x = randint(0, self._n - 1)
            y = randint(0, self._m - 1)
                        
            while self._map[x][y] != ' ':
                x = randint(0, self._n - 1)
                y = randint(0, self._m - 1)

            obj.get_coords(x, y)
            
            self._map[x][y] = str(obj)


    def put_char(self, char, x, y):
        self._map[x][y] = str(char)


    def move_char(self, char, x, y, x_, y_):
        self._map[x][y] = ' '
        self._map[x_][y_] = str(char)
        

    def _generate_map(self):

        game_map = []
        game_map = [[' ' for i in range(self._n)] for j in range(self._m)]

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

    def show_size (self):
        return [self._n, self._m]

if __name__ == '__main__':

    game_map = GameMap(5, 5)
    print(gamemap)
