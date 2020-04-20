from random import randint, choice
from players import Bot, Player, Discs
from game_map import GameDesk
import game_map

P = 'P'
B = 'B'


def capture_disk(pl_r):

    possible_capture = {}
    player_army = pl_r.get_army_dsk()
    if str(pl_r) == 'O':
        increment_x = - 1
        enemy = 'X'
    else:
        increment_x = 1
        enemy = 'O'

    for disk in player_army:

        key_old = disk.key
        new_x = disk.x + increment_x
        new_y = disk.y - 1

        if coordinate_in_map(new_x, new_y):
            obj = game_map_.get_obj(new_x, new_y)

            if obj == enemy:
                 key_kill = key_by_coordinate(new_x, new_y)
                 new_x = new_x + increment_x
                 new_y = new_y - 1

                 if coordinate_in_map(new_x, new_y):
                     obj = game_map_.get_obj(new_x, new_y)

                     if obj == ' ':
                         key = key_by_coordinate(new_x, new_y)
                         possible_capture[key, key_old, key_kill] = (new_x, new_y)

        new_x = disk.x + increment_x
        new_y = disk.y + 1

        if coordinate_in_map(new_x, new_y):
            obj = game_map_.get_obj(new_x, new_y)
            if obj == enemy:
                 key_kill = key_by_coordinate(new_x, new_y)

                 new_x = new_x + increment_x
                 new_y = new_y + 1
                 if coordinate_in_map(new_x, new_y):
                     obj = game_map_.get_obj(new_x, new_y)
                     if obj == ' ':
                         key = key_by_coordinate(new_x, new_y)
                         possible_capture[key, key_old, key_kill] = (new_x, new_y)

    return possible_capture


def capture_disk_rec(enemy, space, key_old, x, y, increment_x, increment_y, possible_capture):

    new_x = x + increment_x
    new_y = y + increment_y

    if coordinate_in_map(new_x, new_y):
        obj = game_map_.get_obj(new_x, new_y)

        if obj == enemy:
            key_kill = key_by_coordinate(new_x, new_y)

            new_x = new_x + increment_x
            new_y = new_y + increment_y

            if coordinate_in_map(new_x, new_y):
                obj = game_map_.get_obj(new_x, new_y)

                if obj == space:
                    key = key_by_coordinate(new_x, new_y)
                    possible_capture[key, key_old, key_kill] = (new_x, new_y)
    #  print(possible_capture)
    return possible_capture


def capture_disk2(pl_r):

    possible_capture = {}
    player_army = pl_r.get_army_dsk()

    if str(pl_r) == 'O':
        increment_x = - 1
        enemy = 'X'
    else:
        increment_x = 1
        enemy = 'O'

    for disk in player_army:

        increment_y = -1
        possible_capture = capture_disk_rec(enemy, ' ', disk.key, disk.x, disk.y,
                                            increment_x, increment_y, possible_capture)
        increment_y = 1
        possible_capture = capture_disk_rec(enemy, ' ', disk.key, disk.x, disk.y,
                                            increment_x, increment_y, possible_capture)

    return possible_capture


def validate_move(charkey, pl_r):

    is_valid = False

    if charkey in game_map.dict_all_black_cells.keys() and pl_r.disc_in_army(charkey):
        is_valid = True

    return is_valid


def coordinate_in_map(new_x, new_y):

        in_map = True
        if new_x < 0 or new_y < 0 or \
            new_x >= map_dim_x or new_y >= map_dim_y:
            in_map = False
        return in_map


def key_by_coordinate(new_x, new_y):

    for key, value in game_map.dict_all_black_cells.items():

        x, y = value
        if x == new_x and y == new_y:
            key_n = key

    return key_n


def next_step(step):

    if step == P:
        return B
    else:
        return P


def available_move(pl_r):

    possible_moves = {}
    player_army = pl_r.get_army_dsk()

    if str(pl_r) == 'O':
        increment_x = - 1
        #  enemy = 'X'
    else:
        increment_x = 1
        #  enemy = 'O'

    for disk in player_army:

        old_key = disk.key
        new_x = disk.x + increment_x
        new_y = disk.y - 1
        #  print(coordinate_in_map(new_x, new_y))
        if coordinate_in_map(new_x, new_y):
            obj = game_map_.get_obj(new_x, new_y)
            if obj == ' ':
                key = key_by_coordinate(new_x, new_y)
                possible_moves[key] = [old_key, (new_x, new_y)]

        new_x = disk.x + increment_x
        new_y = disk.y + 1
        #  print(coordinate_in_map(new_x, new_y))
        if coordinate_in_map(new_x, new_y):
            obj = game_map_.get_obj(new_x, new_y)
            if obj == ' ':
                key = key_by_coordinate(new_x, new_y)
                possible_moves[key] = [old_key, (new_x, new_y)]
    return possible_moves


def best_move(pl_r):

    possible_moves = {}
    player_army = pl_r.get_army_dsk()

    if str(pl_r) == 'O':
        increment_x = - 1
        enemy = 'X'
    else:
        increment_x = 1
        enemy = 'O'

    for disk in player_army:
        maybe = False

        old_key = disk.key
        new_x = disk.x + increment_x
        new_y = disk.y - 1

        if coordinate_in_map(new_x, new_y):
            obj = game_map_.get_obj(new_x, new_y)
            if obj == ' ':
                key = key_by_coordinate(new_x, new_y)
                x = new_x + increment_x
                y = new_y - 1

                if coordinate_in_map(x, y):
                    obj = game_map_.get_obj(x, y)
                    if obj == ' ' or obj != enemy:
                        maybe = True

                x = new_x + increment_x
                y = new_y + 1

                if coordinate_in_map(x, y):
                    obj = game_map_.get_obj(x, y)
                    if (obj == ' ' or obj != enemy) and maybe:
                        possible_moves[key] = [old_key, (new_x, new_y)]

        new_x = disk.x + increment_x
        new_y = disk.y + 1

        if coordinate_in_map(new_x, new_y):
            obj = game_map_.get_obj(new_x, new_y)
            if obj == ' ':
                key = key_by_coordinate(new_x, new_y)
                x = new_x + increment_x
                y = new_y - 1

                if coordinate_in_map(x, y):
                    obj = game_map_.get_obj(x, y)
                    if obj == ' ' or obj != enemy:
                        maybe = True

                x = new_x + increment_x
                y = new_y + 1

                if coordinate_in_map(x, y):
                    obj = game_map_.get_obj(x, y)
                    if (obj == ' ' or obj != enemy) and maybe:
                        possible_moves[key] = [old_key, (new_x, new_y)]

    return possible_moves


def move_desc(pl_r, charkey, charkey_new, new_x, new_y):

        pl_r.move_desc(charkey, charkey_new, new_x, new_y)

        return


def kill_disc(pl_r, charkey):

    pl_r.kill_disc(charkey)

    return


step = B
map_dim_x = 8
map_dim_y = 8

print('Start of a game Checkers!')
name = input('Enter your name: ')
level = input('Difficulty [Medium (M), Easy (E)]: enter M or E')
player = Player(name)
bot = Bot()
print(f'Player {name} your figure - O, bot {bot.get_name()} play - X')

while True:
    game_map_ = GameDesk()
    game_map_.put_char(bot)
    game_map_.put_char(player)
    print(game_map_)
    step = next_step(step)
    charkey_kill = ''

    if step == B:
        who_play = bot
        who_killed = player
        poss_capture = capture_disk2(who_play)
        if len(poss_capture) > 0:
            char = choice(list(poss_capture.keys()))
            new_x, new_y = poss_capture[char]
            charkey_new, charkey, charkey_kill = char
            #  old_x, old_y = game_map.dict_all_black_cells.get(charkey)
            print(f'Bot move {charkey} - {charkey_new}, and kill disk - {charkey_kill}')
        else:
            if level == 'M':
                poss_move = best_move(who_play)
                if len(poss_move) > 0:
                    charkey_new = choice(list(poss_move.keys()))
                    charkey, (new_x, new_y) = poss_move[charkey_new]
                    charkey_kill = ''
                    #  old_x, old_y = game_map.dict_all_black_cells.get(charkey)
                    print(f'Bot move {charkey} - {charkey_new}')
                else:
                    poss_move = available_move(who_play)
                    if len(poss_move) > 0:
                        charkey_new = choice(list(poss_move.keys()))
                        charkey, (new_x, new_y) = poss_move[charkey_new]
                        charkey_kill = ''
                        #  old_x, old_y = game_map.dict_all_black_cells.get(charkey)
                        print(f'Bot move {charkey} - {charkey_new}')
                    else:
                        print(f'Bot {bot.get_name()} loose!')
                        break
            else:
                poss_move = available_move(who_play)
                if len(poss_move) > 0:
                    charkey_new = choice(list(poss_move.keys()))
                    charkey, (new_x, new_y) = poss_move[charkey_new]
                    charkey_kill = ''
                    #  old_x, old_y = game_map.dict_all_black_cells.get(charkey)
                    print(f'Bot move {charkey} - {charkey_new}')
                else:
                    print(f'Bot {bot.get_name()} loose!')
                    break
    else:
        who_play = player
        who_killed = bot
        poss_capture = capture_disk2(who_play)
        poss_move = available_move(who_play)

        if len(poss_capture) == 0 and len(poss_move) == 0:
            print(f'{name} you loose!')
            break
        if len(poss_capture) == 1:

            char = choice(list(poss_capture.keys()))
            new_x, new_y = poss_capture[char]
            charkey_new, charkey, charkey_kill = char
            #  old_x, old_y = game_map.dict_all_black_cells.get(charkey)
            print(f'You have only one possible move {charkey} - {charkey_new}')
            input('Press any key ')

        else:
            while True:

                charkey = input('Input cell\'s coordinate of a checker to move : ')
                if validate_move(charkey, who_play):
                    old_x, old_y = game_map.dict_all_black_cells.get(charkey)
                    break
                else:
                    print('You take invalid disk. Try again')
            while True:

                charkey_new = input('Input (destination cell\'s coordinate): ')
                if charkey_new in game_map.dict_all_black_cells.keys():
                    new_x, new_y = game_map.dict_all_black_cells.get(charkey_new)
                    break
                else:
                    print('You input invalid move. Try again')

            if len(poss_capture) > 1:
                chars = [key for key in poss_capture.keys() if charkey in key]

                if len(chars) == 0:

                    print('You do invalid move. I\'ll take one right')
                    char = choice(list(poss_capture.keys()))
                    new_x, new_y = poss_capture[char]
                    charkey_new, charkey, charkey_kill = char
                    old_x, old_y = game_map.dict_all_black_cells.get(charkey)
                else:
                    charkey_new, charkey, charkey_kill = chars[0]
                    new_x, new_y = game_map.dict_all_black_cells.get(charkey_new)

            elif len(poss_capture) == 0 and (abs(old_x - new_x) > 1 or abs(old_y - new_y) > 1 or
                                             (old_x - new_x) < 0):

                chars = [key for key, value in poss_move.items() if charkey in value]
                charkey_new = chars[0]
                new_x, new_y = game_map.dict_all_black_cells.get(charkey_new)
                print(f'You can\'t move by 2 field or move backward. This one right - {charkey} - {charkey_new}')

    char2 = game_map_.get_obj(new_x, new_y)
    if char2 == ' ':
        #  game_map_.move_char(' ', old_x, old_y)
        #  game_map_.move_char(who_play, new_x, new_y)
        move_desc(who_play, charkey, charkey_new, new_x, new_y)

        if charkey_kill != '':
            kill_disc(who_killed, charkey_kill)
        continue

    #  else:
    #    if 'y' == input('Exit from game? (y/n): '):
    #        break
    #  continue

print('Game Over')
