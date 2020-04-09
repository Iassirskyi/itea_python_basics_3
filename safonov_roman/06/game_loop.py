from random import randint, choice
from characters import CHARACTERS, ENEMIES
from game_objects import GAME_OBJECTS, Chest
from game_map import GameMap


def get_trapped(character):

    print('\nYou got trapped')
    damage = randint(5, 25)
    character.get_damaged(damage)


def get_healed(character):

    print('\nYou found magic potion')
    hp = randint(5, 25)
    character.get_healed(hp)

def fight_with_enemy(character, enemy):

    is_won = True
    
    while True:
        
        character.fight(enemy)

        if character.is_dead():
            is_won = False
            break
        elif enemy.is_dead():
            break
        
    return is_won


DIRECTION = {'up', 'down', 'left', 'right'}

print('Welcome to the game!')
name = input ('Enter your name: ')
race = input ('Choose race [Human, Orc, Elf]:')
level = input('Select Difficulty [Hard, Medium, Easy]: ')

if level == 'Hard':
    objects = [choice(GAME_OBJECTS)() for i in range(4)]
    enemies = [choice(ENEMIES)() for i in range(5)]
    objects += enemies
    objects += [Chest()]
elif level == 'Medium':
    objects = [choice(GAME_OBJECTS)() for i in range(4)]
    enemies = [choice(ENEMIES)() for i in range(2)]
    objects += enemies
    objects += [Chest()]
elif level == 'Easy':
    objects = [choice(GAME_OBJECTS)() for i in range(2)]
    enemies = [choice(ENEMIES)() for i in range(1)]
    objects += enemies
    objects += [Chest()]

x, y = randint(0,4), randint(0, 4)
char = CHARACTERS[race](name, x, y)
char.show_stats()

game_map = GameMap(5, 5, objects)
game_map.put_char(char, *char.give_coords())
map_dict = {}

while True:

    print(game_map)

    while True:

        end_game = False
        
        turn = input('choose where to go [up, down, left, right]? ')
    
        while turn not in DIRECTION:
            turn = input('choose where to go [up, down, left, right]? ')

        if turn == 'up':
            move = (-1, 0)
        elif turn == 'down':
            move = (1, 0)
        elif turn == 'left':
            move = (0, -1)
        elif turn == 'right':
            move = (0, 1)

        cur_pos = char.give_coords()
        next_pos = tuple(map(lambda a, b: a + b, cur_pos, move) )
        
        if next_pos[0] >= 0 and next_pos[1] >= 0 and next_pos[0] <= game_map.show_size()[0] - 1 and next_pos[1] <= game_map.show_size()[1] - 1:
            break
        print ("\nYou can't just run away!")

    
    for element in objects:

        if element.respond()[0] == next_pos:
            step = element.respond()[1]

        else: step = ''
        
        if step == 'Chest':
            print ('\nCongratulations, you have found a Chest! \nYou won')
            end_game = 'Won'
            break

        elif step == 'Heal':
            get_healed(char)
            
        elif step == 'Trap':
            get_trapped(char)

            if char.is_dead():
                end_game = 'Lost'
                break

        elif step == 'Undead' or step == 'Murloc':
            print ('\nYou have met an ENEMY ! ! !')

            is_won = fight_with_enemy(char, element)

            if not is_won:
                end_game = 'Lost'
                break
            
        else: pass

    if not end_game:
        char.move_char(move)
        new_pos = char.give_coords()
        
        game_map.move_char(char, *cur_pos, *new_pos)

    else:
        break

if end_game == 'Lost':
    print(' ###   #  ### ')
    print(' #  #     #  #')
    print(' ###   #  ### ')
    print(' # #   #  #   ')
    print(' #  #  #  #   ')
    print('Game over')        
        
