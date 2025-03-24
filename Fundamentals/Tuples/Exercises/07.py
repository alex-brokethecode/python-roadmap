# Merge two tuples (1, 2, 3) and (4, 5, 6) without using +.

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# [ My Solution ]

output = tuple(number for pair in zip(tuple1, tuple2) for number in pair)
print(output)
