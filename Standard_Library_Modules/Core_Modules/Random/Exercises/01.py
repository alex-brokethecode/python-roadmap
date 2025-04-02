# Dice Roll: Write a Python program that simulates rolling a six-sided die.

from random import randint

player1 = randint(1, 6)
player2 = randint(1, 6)

print(f'Player 1 rolled: {player1}')
print(f'Player 2 rolled: {player2}\n')

result = 'Player 1 won' if player1 > player2 else 'Player 2 won' if player2 > player1 else 'Draw'
print(result)
