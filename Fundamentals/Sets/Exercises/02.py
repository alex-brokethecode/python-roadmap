# Add the number 6 to the set, then remove the number 2.

# [ My Solution ]

numbers = {i for i in range(1, 6)}
numbers.add(6)
numbers.discard(2)

print(numbers)
