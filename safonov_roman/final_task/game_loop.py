from deck import Deck
from random import choice


def choose_colour():

    colour = input('Which color do you choose? [black/white] ? ')

    while True:
        if colour == 'black' or colour == 'Black':
            colour = 'black'

            break
        elif colour == 'white' or colour == 'White':
            colour = 'white'
            break
        else:
            colour = input('type only "black"/"white": ')
    return colour


def check_moves(whos_turn):

    pieces = []

    if whos_turn == 'player':
        for el in deck.p_army:
            if el.give_type() != 'dead':
                pieces.append(el.give_coords())
        way = -1
        labels = deck.b_labels

    elif whos_turn == 'bot':
        for el in deck.b_army:
            if el.give_type() != 'dead':
                pieces.append(el.give_coords())
        way = 1
        labels = deck.p_labels

    pos_moves = []
    pos_fight = []

    for el in pieces:
        move_1 = (el[0] + way * 1, el[1] - 1)
        jump_1 = (el[0] + way * 2, el[1] - 2)
        move_2 = (el[0] + way * 1, el[1] + 1)
        jump_2 = (el[0] + way * 2, el[1] + 2)

        if move_1[0] in range(0, deck_size) and move_1[1] in range(0, deck_size):

            if deck.who_s_there(move_1) == ' ':
                pos_moves.append((el, move_1))
            elif deck.who_s_there(move_1) in labels:
                if jump_1[0] in range(0, deck_size) and jump_1[1] in range(0, deck_size) and deck.who_s_there(jump_1) == ' ':
                    pos_fight.append(((el, jump_1), move_1))
                    pos_moves.append((el, jump_1))


        if move_2[0] in range(0, deck_size) and move_2[1] in range(0, deck_size):

            if deck.who_s_there(move_2) == ' ':
                pos_moves.append((el, move_2))
            elif deck.who_s_there(move_2) in labels:
                if jump_2[0] in range(0, deck_size) and jump_2[1] in range(0, deck_size) and deck.who_s_there(jump_2) == ' ':
                    pos_fight.append(((el, jump_2), move_2))
                    pos_moves.append((el, jump_2))

    return pieces, pos_moves, pos_fight


def p_turn(pieces, pos_moves, pos_fight):

    while True:
        p_from = input('Which piece you chose? ')

        while p_from not in deck.map.keys():
            p_from = input('Chose valid place: ')

        while deck.map[p_from] not in pieces:

            if deck.deck[deck.map[p_from][0]][deck.map[p_from][1]] == ' ':
                p_from = input('Choose not empty place: ')
            else:
                p_from = input('You can chose only your piece: ')

        p_to = input('Where to move? ')

        while p_to not in deck.map.keys():
            p_to = input('Chose valid place: ')

        if len(pos_fight) > 0 and (deck.map[p_from], deck.map[p_to]) not in [(el[0][0], el[0][1]) for el in p_pos_fight]:
            print ('You have to jump if it is possible! ')
        elif (deck.map[p_from], deck.map[p_to]) not in [(el[0], el[1]) for el in pos_moves]:
            print("You can't go there! ")
        else:
            break

    if len(pos_fight) > 0:
        for el in pos_fight:
            if (deck.map[p_from], deck.map[p_to]) == el[0]:
                deck.fight(*el)
    else:
        deck.move_piece(p_from, p_to)


def b_turn(pieces, pos_moves, pos_fight):

    if len(pos_fight) > 0:
        b_move = choice(pos_fight)
        deck.fight(*b_move)
    else:
        b_move = choice(pos_moves)

        b_from = ''
        b_to = ''

        for key, value in deck.map.items():
            if value == b_move[0]:
                b_from = key
            elif value == b_move[1]:
                b_to = key

        deck.move_piece(b_from, b_to)


end_game = False

while not end_game:

    p_colour = choose_colour()

    deck_size = 8
    deck = Deck(deck_size, deck_size, p_colour)
    end_round = False

    while not end_round:

        if p_colour == 'black':

            print(deck)

            p_pieces, p_pos_moves, p_pos_fight = check_moves('player')

            if len(p_pos_moves) == 0:
                end_round = 1
            else:
                p_turn(p_pieces, p_pos_moves, p_pos_fight)

            b_pieces, b_pos_moves, b_pos_fight = check_moves('bot')

            if len(b_pos_moves) != 0 and end_round != 1:
                b_turn(b_pieces, b_pos_moves, b_pos_fight)

        else:

            b_pieces, b_pos_moves, b_pos_fight = check_moves('bot')

            if len(b_pos_moves) == 0:
                end_round = 1
            else:
                b_turn(b_pieces, b_pos_moves, b_pos_fight)

            print(deck)

            p_pieces, p_pos_moves, p_pos_fight = check_moves('player')

            if len(p_pos_moves) != 0 and end_round != 1:
                p_turn(p_pieces, p_pos_moves, p_pos_fight)

    if len(p_pos_moves) == 0:
        print('you loose! ')
    else:
        print('you won! ')

    again = input('play again? (y / n): ')
    while again != 'y' and again != 'n':
        again = input('type only "y" / "n": ')

    if again == 'y':
        end_game = 0
    else:
        print('see you soon!')
        end_game = 1
