from random import randint, choice
from characters import CHARACTERS, ENEMIES
from game_objects import GAME_OBJECTS, Exit
from game_map import GameMap


def get_trapped(character):
    print('You got into trap. It is going to hurt!')
    damage = randint(5, 25)
    character.get_damaged(damage)


def get_healed(character):
    print('You got healed')
    hp = randint(5, 25)
    character.get_healed(hp)


def fight_with_enemy(character, enemy):
    is_won = True

    while True:
        character.fight(enemy)

        if character.is_dead():
            is_won = False
            print('Unfortunately, you have been killed')
            break
        elif enemy.is_dead():
            break

    return is_won


print('Welcome to my game!')
name = input('Enter your name: ')
race = input('Choose race [Human, Orc, Elf]: ')
level = input('Difficulty [Hard, Medium, Easy]: ')

if level == 'Hard' or level == 'hard':
    objects = [choice(GAME_OBJECTS)() for i in range(3)]
    enemies = [choice(ENEMIES)() for i in range(6)]
    objects += enemies
    objects += [Exit()]
elif level == 'Medium' or level == 'medium':
    objects = [choice(GAME_OBJECTS)() for i in range(4)]
    enemies = [choice(ENEMIES)() for i in range(4)]
    objects += enemies
    objects += [Exit()]
elif level == 'Easy' or level == 'easy':
    objects = [choice(GAME_OBJECTS)() for i in range(6)]
    enemies = [choice(ENEMIES)() for i in range(2)]
    objects += enemies
    objects += [Exit()]

x, y = randint(0, 4), randint(0, 4)
char = CHARACTERS[race](name, x, y)
char.show_stats()

game_map = GameMap(6, 6, objects)
game_map.put_char(char, *char.get_coords())
game = True

while game:

    print(game_map)
    step = input('Please specify direction [up, down, left, right?]:\t')
    if step == 'up':
        move = (-1, 0)

    elif step == 'down':
        move = (1, 0)

    elif step == 'left':
        move = (0, -1)

    elif step == 'right':
        move = (0, 1)

    char_pos = char.get_coords()
    char.move(move)
    new_pos = char.get_coords()
    game_map.moving_char(char, *char_pos, *new_pos)

    for obj in objects:

        if obj.show_coords()[0] == new_pos:
            target = obj.show_coords()[1]

            if target == 'Trap':
                get_trapped(char)
                if char.is_dead():
                    print('You have been killed by a Trap. Shame on you!')
                    game = False

            elif target == 'Heal':
                get_healed(char)

            elif target == 'Undead' or target == 'Murlock':
                print('You are under attack!')
                fight_with_enemy(char, obj)
                if char.is_dead():
                    print('Game over! Thank you for bringing your bones to our feast!')
                    game = False

            elif target == 'Exit':
                print('You successfully escaped! See you next time')
                game = False
