# Find the largest and smallest number in a list without using `max()` or `min()`.

from random import randint

numbers: list[int] = [randint(1, 100) for _ in range(10)]

max_number = min_number = numbers[0]

for number in numbers[1:]:
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number

print(numbers)
print(f'max = {max_number}')
print(f'min = {min_number}')
