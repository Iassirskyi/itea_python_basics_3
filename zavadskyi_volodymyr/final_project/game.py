from random import randint, choice
from time import sleep


game_on = True

cell_dict = {'A1': (0, 0), 'A2': (1, 0), 'A3': (2, 0), 'A4': (3, 0), 'A5': (4, 0), 'A6': (5, 0), 'A7': (6, 0), 'A8': (7, 0),
             'B1': (0, 1), 'B2': (1, 1), 'B3': (2, 1), 'B4': (3, 1), 'B5': (4, 1), 'B6': (5, 1), 'B7': (6, 1), 'B8': (7, 1),
             'C1': (0, 2), 'C2': (1, 2), 'C3': (2, 2), 'C4': (3, 2), 'C5': (4, 2), 'C6': (5, 2), 'C7': (6, 2), 'C8': (7, 2),
             'D1': (0, 3), 'D2': (1, 3), 'D3': (2, 3), 'D4': (3, 3), 'D5': (4, 3), 'D6': (5, 3), 'D7': (6, 3), 'D8': (7, 3),
             'E1': (0, 4), 'E2': (1, 4), 'E3': (2, 4), 'E4': (3, 4), 'E5': (4, 4), 'E6': (5, 4), 'E7': (6, 4), 'E8': (7, 4),
             'F1': (0, 5), 'F2': (1, 5), 'F3': (2, 5), 'F4': (3, 5), 'F5': (4, 5), 'F6': (5, 5), 'F7': (6, 5), 'F8': (7, 5),
             'G1': (0, 6), 'G2': (1, 6), 'G3': (2, 6), 'G4': (3, 6), 'G5': (4, 6), 'G6': (5, 6), 'G7': (6, 6), 'G8': (7, 6),
             'H1': (0, 7), 'H2': (1, 7), 'H3': (2, 7), 'H4': (3, 7), 'H5': (4, 7), 'H6': (5, 7), 'H7': (6, 7), 'H8': (7, 7)}


class Checker:

    def __init__(self, x, y, color):

        self.name = f'{x}{y}'
        self.x = x
        self.y = y
        self.color = color


    def __str__(self):
        return self.color
   

white_army = [Checker(7, 0, 'o'), Checker(7, 2, 'o'), Checker(7, 4, 'o'), Checker(7, 6, 'o'),
              Checker(6, 1, 'o'), Checker(6, 3, 'o'), Checker(6, 5, 'o'), Checker(6, 7, 'o'),
              Checker(5, 0, 'o'), Checker(5, 2, 'o'), Checker(5, 4, 'o'), Checker(5, 6, 'o')]

black_army = [Checker(0, 1, 'x'), Checker(0, 3, 'x'), Checker(0, 5, 'x'), Checker(0, 7, 'x'),
              Checker(1, 0, 'x'), Checker(1, 2, 'x'), Checker(1, 4, 'x'), Checker(1, 6, 'x'),
              Checker(2, 1, 'x'), Checker(2, 3, 'x'), Checker(2, 5, 'x'), Checker(2, 7, 'x')]

class Board:

    def __init__(self, n, m):
        self._n = n
        self._m = m
        self._board = self._generate_board()
        self._put_checkers(white_army, black_army)


    def __str__(self):

        game_board = self._show_board()
        return game_board


    def _generate_board(self):
        game_board = []
        game_board = [[' ' for i in range(self._n)] for j in range(self._m)]

        return game_board


    def _put_checkers(self, white_army, black_army):

        for checker in white_army:

            self._board[checker.x][checker.y] = 'o'

        for checker in black_army:

            self._board[checker.x][checker.y] = 'x'


    def _show_board(self):

        game_board = []

        print('   A B C D E F G H   \n')

        for index, row in enumerate(self._board):

            game_board.append(f'{index + 1} |')

            for i in row:
                game_board.append(f'{i}|')

            game_board.append('\n')

        game_board.pop()

        return ''.join(game_board)

    def _death_of_checker(self, che, army):

        for checker in army:

            if checker.name == che:
                army.remove(checker)


    def _possible_moves_white(self, che, x, y): #I could do the same as with black possible moves, but it didn`t work. I don`t know the the reason

        if self._board[int(x)][int(y)] != ' ':
            return False
        
        if self._board[che.x][che.y] != 'o':
            return False

        try:
            if self._board[int(x)][int(y)] == ' ' and self._board[int(x + 1)][int(y + 1)] == 'x':
                return True

            elif self._board[int(x)][int(y)] == ' ' and self._board[int(x + 1)][int(y - 1)] == 'x':
                return True
            
            else:
                if x != che.x - 1 or (y != che.y - 1 and y != che.y + 1):
                    return False

                else:
                    return True

        except IndexError:
                return True
        
    
    def _possible_fight_moves_black(self, black_army):

        possible_moves = {}

        for checker in black_army:

            self._board[checker.x][checker.y] = checker

            try:
                if self._board[checker.x + 1][checker.y - 1] == 'o':
                    if checker.y - 2 >= 0 and checker.x + 2 <= 7:
                        if self._board[checker.x + 2][checker.y - 2] == ' ':
                            possible_moves[checker.name] = [(checker.x + 2, checker.y - 2)]
                        
                if self._board[checker.x + 1][checker.y + 1] == 'o':
                    if checker.y + 2 <= 7 and checker.x + 2 <= 7:
                        if self._board[checker.x + 2][checker.y + 2] == ' ':
                            possible_moves[checker.name] = [(checker.x + 2, checker.y + 2)]
                        
            except IndexError:
                continue

            except KeyError:
                continue

        return possible_moves


    def _possible_moves_black(self, black_army):

        possible_moves = {}

        for checker in black_army:

            self._board[checker.x][checker.y] = checker

            try:
            
                if checker.y - 1 >= 0 and checker.x + 1 <= 7:
                    if self._board[checker.x + 1][checker.y - 1] == ' ':
                        possible_moves[checker.name] = [(checker.x + 1, checker.y - 1)]
                if checker.y + 1 <= 7 and checker.x + 1 <= 7:
                    if self._board[checker.x + 1][checker.y + 1] == ' ':
                        possible_moves[checker.name].append((checker.x + 1, checker.y + 1))

            except IndexError:
                continue

            except KeyError:
                continue

        return possible_moves


    def _move_checker(self, che, a, b, army):
        
        for checker in army:

            if checker.name == che:
                army.remove(checker)
                army.append(Checker(a, b, checker.color))
  
                 
while game_on == True:

    #player move

    game_board = Board(8, 8)
    print(game_board)
    
    first_coord = input("\nCell's coordinate of a checker to move:  ")
    second_coord = input("Destination cell's coordinate: ")

    
    try:
        check = Checker(*cell_dict[first_coord], 'o')
        choose = check.name
        first = cell_dict[first_coord]
        step = cell_dict[second_coord]
        
    except KeyError:
        print('Incorrect entry. Try again!')
        continue
    
    while True:
        
        if game_board._possible_moves_white(check, *step) == True:
            
            game_board._move_checker(choose, *step, white_army)

            if (first[0] - 2, first[1] + 2) == step:
        
                game_board._death_of_checker(f'{first[0] - 1}{first[1] + 1}', black_army)

            if (first[0] - 2, first[1] - 2) == step:

                game_board._death_of_checker(f'{first[0] - 1}{first[1] - 1}', black_army)
                
            break
        
        else:
            
            first_coord = input("\nCell's coordinate of a checker to move:  ")
            second_coord = input("Destination cell's coordinate: ")
            check = Checker(*cell_dict[first_coord], 'o')
            choose = check.name
            step = cell_dict[second_coord]

    

    game_board = Board(8, 8)
    print(game_board)

    #bot move
    
    sleep(3)

    possible_moves = game_board._possible_fight_moves_black(black_army)
        
    try:
        checker_to_move = choice(list(possible_moves.keys()))

    except IndexError:
        possible_moves = game_board._possible_moves_black(black_army)
        checker_to_move = choice(list(possible_moves.keys()))
    coords_to_move = choice(possible_moves[checker_to_move])
    
    for checker in black_army:
        if checker.name == checker_to_move:
            coord_x = checker.x
            coord_y = checker.y

    if (coord_x + 2, coord_y + 2) == coords_to_move:
        
        game_board._death_of_checker(f'{coord_x + 1}{coord_y + 1}', white_army)

    if (coord_x + 2, coord_y - 2) == coords_to_move:

        game_board._death_of_checker(f'{coord_x + 1}{coord_y - 1}', white_army)
        
    game_board._move_checker(checker_to_move, *coords_to_move, black_army)

    if white_army == []:

        print('You lost')
        game_on = False

    if black_army == []:

        print('You won')
        game_on = False
