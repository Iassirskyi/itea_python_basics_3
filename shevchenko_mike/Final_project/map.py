import self as self


class Map:
    army = {
        "b8": [1, 0], "d8": [3, 0], "f8": [5, 0], "h8": [7, 0],
        "a7": [0, 1], "c7": [2, 1], "e7": [4, 1], "g7": [6, 1],
        "b6": [1, 2], "d6": [3, 2], "f6": [5, 2], "h6": [7, 2],
        "a5": [0, 3], "c5": [2, 3], "e5": [4, 3], "g5": [6, 3],
        "b4": [1, 4], "d4": [3, 4], "f4": [5, 4], "h4": [7, 4],
        "a3": [0, 5], "c3": [2, 5], "e3": [4, 5], "g3": [6, 5],
        "b2": [1, 6], "d2": [3, 6], "f2": [5, 6], "h2": [7, 6],
        "a1": [0, 7], "c1": [2, 7], "e1": [4, 7], "g1": [6, 7]
    }

    def __init__(self):

        self.white = [
            'b8', 'd8', 'f8', 'h8',
            'a7', 'c7', 'e7', 'g7',
            'b6', 'd6', 'f6', 'h6'
        ]

        self.black = [
            'a3', 'c3', 'e3', 'g3',
            'b2', 'd2', 'f2', 'h2',
            'a1', 'c1', 'e1', 'g1'
        ]
        self.mainmap = [[0 for x in range(8)] for y in range(8)]
        self.fillmap()
        self.drawmap()

    def drawmap(self):
        print('   A  B C D E F G H    ')
        x = y = 0
        for y in range(8):
            for x in range(8):
                if x == 0:
                    print(f'{8 - y} |', end=" ")
                if self.mainmap[x][y] == 0:
                    print(" |", end="")
                elif self.mainmap[x][y] == 1:
                    print("X|", end="")
                elif self.mainmap[x][y] == 2:
                    print("0|", end="")
                else:
                    print(" |", end="")
            if x == 7:
                print(f' {8 - y}')
        print('   A  B C D E F G H    ')

    def fillmap(self):
        for key in self.army.keys():
            x = self.army.get(key)[0]
            y = self.army.get(key)[1]

            if key in self.black:
                self.mainmap[x][y] = 2
            elif key in self.white:
                self.mainmap[x][y] = 1
            else:
                self.mainmap[x][y] = 3

    def drawnmap(self):
       for y in range(8):
            for x in range(8):
                if self.mainmap[x][y] == 2:
                    print('B')
                elif self.mainmap[x][y] == 1:
                    print('W')
                else:
                    print(' ')

