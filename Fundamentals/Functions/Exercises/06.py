# Use filter() to keep only palindromic words from a list.

# [ My Solution ]

words = ['mom', 'daughter', 'level', 'npc', 'noon', 'sun', 'rock', 'pop']

palindromic = list(filter(lambda w: w == w[::-1], words))
print(f'{palindromic=}')

# [ Tip ]
palindromic = [word for word in words if word == word[::-1]]
print(f'{palindromic=}')
