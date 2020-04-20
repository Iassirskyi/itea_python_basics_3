from checkers import TYPES


ALPHABET = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')


class Deck:

    def __init__(self, n, m, p_colour):

        self._n = n
        self._m = m
        self.alpha = {ALPHABET[i]: i for i in range(self._m)}
        self.deck = self._gen_deck()
        self.p_army = self.gen_pieces(p_colour)[0]
        self.b_army = self.gen_pieces(p_colour)[1]
        self.pieces = self.p_army + self.b_army
        self.put_pieces(self.p_army + self.b_army)
        self.map = {j+str(i+1): (i, self.alpha[j]) for i in range(self._n) for j in self.alpha.keys()}
        self.p_labels, self.b_labels = self.assign_labels(p_colour)

    def __str__(self):

        deck = self._deck_view()
        return deck

    def _gen_deck(self):

        deck = [[' ' for i in range(self._n)] for j in range(self._m)]
        return deck

    def put_pieces(self, pieces):
        for el in pieces:
            self.deck[el._x][el._y] = str(el)

    def assign_labels(self, colour):

        if colour == 'black':
            p_label = ['X', 'x']
            b_label = ['O', 'o']
        else:
            p_label = ['O', 'o']
            b_label = ['X', 'x']

        return p_label, b_label

    def _deck_view(self):
        view = []
        b_line = '\n\n'

        header = list('    ')
        line = [f'{list(self.alpha.keys())[i]} ' for i in range(self._n)]
        header += ''.join(line)
        view.append(''.join(header))
        view.append(b_line)

        for ind, row in enumerate(self.deck):

            view.append(f'{ind + 1}  |')

            for i in row:

                view.append(f'{i}|')

            view.append(f'  {ind + 1}\n')

        view.append('\n')
        view.append(''.join(header))

        return ''.join(view)

    def gen_pieces(self, colour):

        def pos_gen(n):

            pos = [[i, j - i % 2] for i in range(n, n + 3) for j in range(1, self._m, 2)]

            return pos

        army = []
        if colour == 'white':
            p_chk = TYPES[0]
            b_chk = TYPES[1]
        else:
            p_chk = TYPES[1]
            b_chk = TYPES[0]

        p_army = []
        b_army = []

        for el in pos_gen(5):
            p_army.append(p_chk(el[0], el[1]))

        for el in pos_gen(0):
            b_army.append(b_chk(el[0], el[1]))

        return p_army, b_army

    def move_piece(self, p_from, p_to):
        x_from = self.map[p_from][0]
        y_from = self.map[p_from][1]
        x_to = self.map[p_to][0]
        y_to = self.map[p_to][1]

        self.deck[x_from][y_from] = ' '

        for el in self.pieces:
            if el.give_type() != 'dead' and el.give_coords() == self.map[p_from]:
                el.get_coords(self.map[p_to])
                self.deck[x_to][y_to] = str(el)

    def fight(self, move, victim):

        for el in self.pieces:
            if el.give_coords() == victim:
                self.deck[victim[0]][victim[1]] = ' '
                el.get_type = 'dead'
                if el in self.p_army:
                    self.p_army.remove(el)
                    self.pieces.remove(el)
                elif el in self.b_army:
                    self.b_army.remove(el)
                    self.pieces.remove(el)

        for key, value in self.map.items():
            if value == move[0]:
                p_from = key
            elif value == move[1]:
                p_to = key

        self.move_piece(p_from, p_to)

    def who_s_there(self, pos):
        return self.deck[pos[0]][pos[1]]


if __name__ == '__main__':

     deck = Deck(8, 8)
     print(deck.alpha)

