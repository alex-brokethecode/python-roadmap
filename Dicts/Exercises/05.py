# Remove all key-value pairs where the value is None from a dictionary.

dictionary: dict[str, int | None] = {
    'a': 1,
    'b': None,
    'c': 3,
    'd': None
}

# [ My Solution ]

output = {key: value for key, value in dictionary.items() if value is not None}
print(output)

# != => Checks if values are not equal
# is not => Checks if objects are different in memory
