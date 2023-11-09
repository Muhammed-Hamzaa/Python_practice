# Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun.
# The gun beats the snake, the water beats the gun, and the snake beats the water.
# Write a python program to create a Snake Water Gun game in Python using if-else statements.
# Do not create any fancy GUI. Use proper functions to check for win.

#                      Snake  Water Gun
# computer =             0     1     2
# player   =  Snake  0  Draw  Win   Lose
#             Water  1  Lose  Draw  Win
#             Gun    2  Win   Lose  Draw

import random

def check(computer,player):
    if (computer == player):
        return 0
    elif (computer==0 and player==2):
        return 1
    elif (computer==1 and player==0):
        return 1
    elif (computer==2 and player==1):
        return 1
    else:
        return -1

computer= random.randint(0,2)
player= int(input('Press:\n 0 for Snake\n 1 for Water\n 2 for Gun\n'))

if player==0:
    print(f'You: {player} Snake')
elif player==1:
    print(f'You: {player} Water')
elif player==2:
    print(f'You: {player} Gun')
else:
    print("invalid selection")

if computer==0:
    print(f'You: {computer} Snake')
elif computer==1:
    print(f'You: {computer} Water')
else:
    print(f'You: {computer} Gun')


score=check(computer,player)
if score==1:
    print("You Won !")
elif score==0:
    print("It's a Draw !")
else:
    print('You Lose !')
