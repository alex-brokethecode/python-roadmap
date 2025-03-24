# Given a list of numbers, use map(), filter(), and reduce() together to:
# - Square each number
# - Filter out even numbers
# - Find the sum of the remaining numbers

from functools import reduce

numbers: list[int] = [i for i in range(1, 11)]

# [ My Solution ]

# squares = [(lambda x: x ** 2)(i) for i in numbers]
squares = list(map(lambda x: x ** 2, numbers))
even = list(filter(lambda x: x % 2 == 0, numbers))
total = reduce(lambda x, y: x + y, numbers)

print(f'{squares=}')
print(f'{even=}')
print(f'{total=}')

# [ Tip ]
# List comprehensions are faster and clearer

squares = [x ** 2 for x in numbers]
even = [x for x in numbers if x % 2 == 0]
total = sum(numbers)
