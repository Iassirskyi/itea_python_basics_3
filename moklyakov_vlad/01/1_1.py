"""
Task 1 - Game 21

Create a game - 21. There are 10 cards representing values 2-11.
The goal is to get max points, but less then 21. Each turn a player
should decide pick a new card o pass. Pick - value of a card should be
added to player's points. If player gets more then 21 points - he lost.
Pass - no new cards, player stays with current points. Results should
be shown only after all the players passed.

Level 1 - one player.
Level 2 - one player + one bot.
Level 3 - one player + two bots.

To generate a random card use:
# Import function randint from module random
from random import randint

# Usage example
randint(2, 11)
"""

from random import randint

print('-------------------')
print('Game 21')
print('-------------------')
print('1. Purpose of the game: to get a greater number of points on the \n'
      'cards among the players while not crossing the line of 21 points. \n'
      '2. Before starting the game you need to choose the level in which \n'
      'you will play. \n'
      '3. If you want to leave the game: press the Q or q key. If you want \n'
      'to continue: select any of the levels provided.')
print('-------------------')
print('Level 1 - one player. \n'
      'Level 2 - one player + one bot. \n'
      'Level 3 - one player + two bots.')
print('-------------------')
print('The game started! \n')

while True:
    score_player = randint(2, 11)
    score_bot1 = randint(2, 11)
    score_bot2 = randint(2, 11)
    change = 0

    key = input('Or q or level game: ')
    if key == 'q' or key == 'Q':
        break

    elif key == '1':
        score_player += randint(2, 11)

    elif key == '2':
        score_player += randint(2, 11)
        score_bot1 += randint(2, 11)

    elif key == '3':
        score_player += randint(2, 11)
        score_bot1 += randint(2, 11)
        score_bot2 += randint(2, 11)
    else:
        print('Enter correct symbol from conditional')

    while change != 'no':
        print('Card player:', score_player)
        change = input('yes or no: ')
        if change == 'yes':
            score_player += randint(2, 11)
            score_bot1 += randint(2, 11)
            score_bot2 += randint(2, 11)
        elif change == 'no':
            continue
        else:
            print('Do your choose')

    if key == '1' and score_player <= 21:
        print('win', score_player)
    elif key == '2' and score_bot1 < score_player <= 21:
        print('win', score_player, score_bot1)
    elif key == '3' and (score_bot1 and score_bot2) < score_player <= 21:
        print('win', score_player, score_bot1, score_bot2)
    else:
        if score_bot1 > score_bot2:
            print('lose', score_player, score_bot1)
        print('lose', score_player, score_bot2)

print('END GAME')
