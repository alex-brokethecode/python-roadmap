# Use reduce() to multiply all numbers in a list.

# [ My Solution ]
from math import prod
from functools import reduce

numbers: list[int] = [i for i in range(1, 6)]

multiplied_numbers: int = reduce(lambda x, y: x * y, numbers)

print(f'{multiplied_numbers=}')

# [ Tip ]

multiplied_numbers = prod(numbers)
print(f'{multiplied_numbers=}')
