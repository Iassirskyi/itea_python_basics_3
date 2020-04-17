ISBLACK = 1
ISWHITE = 2
ISNONE = 3

class ChessBoard:
    def __init__(self):
        self.chessdict = self.buildchess()

        # self.black = [
        #     'b8', 'd8', 'f8', 'h8',
        #     'a7', 'c7', 'e7', 'g7',
        #     'b6', 'd6', 'f6', 'h6',
        #     'f4'
        # ]

        # self.white = [
        #     'a3', 'c3', 'e3', 'g3',
        #     'b2', 'd2', 'f2', 'h2',
        #     'a1', 'c1', 'e1', 'g1'
        # ]
        self.mainmap = [[0 for _ in range(8)] for _ in range(8)]
        #self.fillmap()

    def buildchess(self):
        chessdict = {}
        x = 0
        flag = 1
        for letter in list("abcdefgh"):
            for y in range(8, 0, -1):
                if flag == 0:
                    key = letter + str(y)
                    chessdict[key] = [x, 8 - y]
                    if y != 1:
                        flag = 1
                else:
                    if y != 1:
                        flag = 0
            x += 1
        return chessdict

    def checkstep(self, draught, newposition):

        if self.chessdict.get(draught)[0] - 1 == self.chessdict.get(newposition)[0] and \
                self.chessdict.get(draught)[1] - 1 == self.chessdict.get(newposition)[1]:
            print("Good choice step left!")
            return True

        if self.chessdict.get(draught)[0] + 1 == self.chessdict.get(newposition)[0] and \
                self.chessdict.get(draught)[1] - 1 == self.chessdict.get(newposition)[1]:
            print("Good choice step Right!")
            return True

        print("Step is not good")
        return False

    def getkeybyvalue(self, *args):
        search = [args[0], args[1]]
        #print(search)
        for key, value in self.chessdict.items():
            if value == search:
                return key
        return None

    def getchess(self, dict):
        return (dict)


    def drawmp(self):
        print("   a b c d e f g h")
        x = 0
        for y in range(8):
            for x in range(8):
                if x == 0:
                    print(f'{8 - y} |', end="")
                if self.mainmap[x][y] == 0:
                    print(" |", end="")
                elif self.mainmap[x][y] == ISBLACK:
                    print("B|", end="")
                elif self.mainmap[x][y] == ISWHITE:
                    print("W|", end="")
                else:
                    print("x|", end="")
            if x == 7:
                print(f' {8 - y}')
        print("   a b c d e f g h")

    def fillmap(self, white, black):
        for key in self.chessdict.keys():
            x = self.chessdict.get(key)[0]
            y = self.chessdict.get(key)[1]

            if key in black:
                self.mainmap[x][y] = ISBLACK
            elif key in white:
                self.mainmap[x][y] = ISWHITE
            else:
                self.mainmap[x][y] = ISNONE

    def checkblackstep(self, draught):
        tar = []
        x = self.chessdict.get(draught)[0]
        y = self.chessdict.get(draught)[1]
        if self.mainmap[x + 1][y - 1] == ISNONE:
            tar.append(self.getkeybyvalue(x + 1, y - 1))
        if self.mainmap[x + 1][y + 1] == ISNONE:
            tar.append(self.getkeybyvalue(x + 1, y + 1))
        return tar

    def ifbeatable(self, draught, oponents):
        jum = []
        tar = []
        x = self.chessdict.get(draught)[0]
        y = self.chessdict.get(draught)[1]
        # Check left
        checkposition = self.getkeybyvalue(x - 1, y - 1)
        if checkposition in oponents:
            if x-2 >= 0 and y-2 >= 0:
                if self.mainmap[x-2][y-2] == ISNONE:
                    jum.append(checkposition)
                    tar.append(self.getkeybyvalue(x-2, y-2))
                    # print("left")
                    # return draught, checkposition, self.getkeybyvalue(x-2, y-2)
        # Check right
        checkposition = self.getkeybyvalue(x - 1, y + 1)
        if checkposition in oponents:
            if x - 2 >= 0 and y + 2 <= 7:
                if self.mainmap[x - 2][y + 2] == ISNONE:
                    jum.append(checkposition)
                    tar.append(self.getkeybyvalue(x - 2, y + 2))
                    # print("right")
                    # return draught, checkposition, self.getkeybyvalue(x - 2, y + 2)
        # Check left bottom
        checkposition = self.getkeybyvalue(x + 1, y - 1)
        if checkposition in oponents:
            if x + 2 <= 7 and y - 2 >= 0:
                if self.mainmap[x + 2][y - 2] == ISNONE:
                    #print(checkposition)
                    jum.append(checkposition)
                    tar.append(self.getkeybyvalue(x + 2, y - 2))
                    # print("left bottom")
                    # return draught, checkposition, self.getkeybyvalue(x + 2, y - 2)
        # Check right bottom
        checkposition = self.getkeybyvalue(x + 1, y + 1)
        if checkposition in oponents:
            if x + 2 <= 7 and y + 2 <= 7:
                if self.mainmap[x + 2][y + 2] == ISNONE:
                    jum.append(checkposition)
                    tar.append(self.getkeybyvalue(x + 2, y + 2))
                    # print("right bottom")
                    # return draught, checkposition, self.getkeybyvalue(x + 2, y + 2)
        return jum, tar
