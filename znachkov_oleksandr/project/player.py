class Player:
    draughts = []

    def getlist(self):
        return self.draughts

    def move(self, cur, tar):
        self.draughts.remove(cur)
        self.draughts.append(tar)

    def beated(self, cur):
        self.draughts.remove(cur)


class White(Player):
    # draughts = [
    #     'e3'
    # ]

    draughts = [
        'a3', 'c3', 'e3', 'g3',
        'b2', 'd2', 'f2', 'h2',
        'a1', 'c1', 'e1', 'g1'
    ]


class Black(Player):
    # draughts = [
    #     'c5'
    # ]
    draughts = [
        'b8', 'd8', 'f8', 'h8',
        'a7', 'c7', 'e7', 'g7',
        'b6', 'd6', 'f6', 'h6',
        'f4'
    ]
