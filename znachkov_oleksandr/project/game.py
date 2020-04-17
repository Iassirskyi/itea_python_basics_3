from mapdraw import ChessBoard
from player import Player, White, Black
from random import randint
import sys

white = White()
black = Black()

#print (white.getlist())

board = ChessBoard()
board.fillmap(white.getlist(), black.getlist())
board.drawmp()

flag = 0
while True:
    #print("Step 1")
    for draught in white.getlist():
        if flag == 2:
            #print("Step 5")
            (jum, tar) = board.ifbeatable(save, black.getlist())
            draught = save
            #print(jum, tar)
            if len(tar) == 0:
                flag = 3
                break;
        else:
            (jum, tar) = board.ifbeatable(draught, black.getlist())
            #print("Step 2")
        #print (cur, jum, tar)
        if len(tar) != 0:
            if flag != 2:
                flag = 1
            #print("Step 3")
            #print (jum, tar)
            for (jump, target) in zip(jum, tar):
                print(f'Enemy {jump} is in beatable position respectivelly to {draught}, landing on {target}')
                choice = input("You must beat one of beatable, are you agree? y/n:")
                if choice == 'y':
                    white.move(draught, target)
                    save = target
                    black.beated(jump)
                    board.fillmap(white.getlist(), black.getlist())
                    board.drawmp()
                    print("Moving to new position")
                    flag = 2
                    print("Step 4")
                    break


    if flag == 1 or flag == 2:
        print ("You must beat!")
        continue

    if flag == 0:
        while True:
            cur = input ("Input draught which to move:")
            tar = input ("Input where to move:")
            if cur not in white.getlist():
                print("You can manage only white draughts!")
                continue
            if tar in black.getlist() or tar in white.getlist():
                print(f'Target place {tar} is not free!')
                continue
            if tar not in board.chessdict.keys():
                print("No such place on the board!")
                continue
            if board.checkstep(cur, tar):
                break
            else:
                print("Wrong move. Draught steps only one position left of right")
                continue
        white.move(cur, tar)
        board.fillmap(white.getlist(), black.getlist())
        board.drawmp()
        print("Moving to new position")
    if len(black.getlist()) == 0:
        print ("Congratulations! You WON!")
        break

    # Black turns
    print ("Black turn")
    flag = 0
    while True:
        for draught in black.getlist():
            if flag == 2:
                (jum, tar) = board.ifbeatable(save, white.getlist())
                draught = save
                if len(tar) == 0:
                    flag = 3
                    break;
            else:
                (jum, tar) = board.ifbeatable(draught, white.getlist())
                # print(f'Checking if near {draught} is beatable')
                # print (draught, jum, tar)
                input()
            if len(tar) != 0:
                if flag != 2:
                    flag = 1
                print("Choosing choosig whome to beat")
                i = randint(0, len(jum)-1)
                black.move(draught, tar[i])
                save = tar[i]
                white.beated(jum[i])
                board.fillmap(white.getlist(), black.getlist())
                board.drawmp()
                flag = 2
                print(f'Black from {draught} beat white in position {jum[i]}')

        if flag == 1 or flag == 2:
           # print ("You must beat!")
            continue
        else:
            flag = 0
            break
    if len(white.getlist()) == 0:
        print("You loose!!!")
        break
    flag = 0
    for draught in black.getlist():
        tar = board.checkblackstep(draught)
        if len(tar) == 0:
            continue
        flag = 1
        target = tar[randint(0, len(tar)-1)]
        black.move(draught, target)
        board.fillmap(white.getlist(), black.getlist())
        board.drawmp()
        print(f'Black move from {draught} to {target}')

    if flag == 0:
        print("No steps for black availiable, YOU WIN!!!")
    else:
        flag = 0

