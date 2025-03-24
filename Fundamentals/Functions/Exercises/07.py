# Use reduce() to find the longest word in a list of strings.

from functools import reduce

# [ My Solution ]

strings = ['mom', 'daughter', 'level', 'npc', 'noon', 'sun', 'rock', 'pop']
longest = reduce(lambda x, y: x if len(x) > len(y) else y, strings)

print(f'{longest=}')

# [ Tip ]
# longest = max(strings, key=len)
longest = max(strings, key=lambda x: len(x))
print(f'{longest=}')
