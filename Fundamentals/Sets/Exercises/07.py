# Given two sets {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}, find:
# - Elements present in the first set but not in the second.
# - Elements present in either of the sets but not both.

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# [ My Solution ]

# print(a - b)
print(a.difference(b))

# print(a ^ b)
print(a.symmetric_difference(b))
