import random

print('What is your name?')
name = input('> ')
print('Hello, {}!'.format(name))

print('Rolling dice...')

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

print('Die 1:', dice1)
print('Die 2:', dice2)
print('Total value: ', dice1 + dice2)

if dice1 + dice2 > 7:
    print('You won!')
else:
    print('You lost...')