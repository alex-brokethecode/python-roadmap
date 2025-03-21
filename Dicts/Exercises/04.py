# Merge two dictionaries into one.

dict1: dict[str, int] = {"a": 1, "b": 2}
dict2: dict[str, int] = {"c": 3, "d": 4}

# [ My Solution ]

output = dict1.copy()

for key, value in dict2.items():
    output[key] = value

print(output)


# [ Improved Version ]

# | operator => Merge dictionaries into a new one
print(dict1 | dict2)

# update() => Update the current dictionary by adding key-value pairs from another dictionary
output2 = dict1.copy()
output2.update(dict2)
print(output2)

# ** operator => unpack dictionaries into key=value pairs (is slower because create an intermediate dictionary)
output3 = {**dict1, **dict2}
print(output3)
