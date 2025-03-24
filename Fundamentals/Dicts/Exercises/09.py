# Write a function that finds the most common value in a dictionary.

from collections import Counter

data = {"a": 2, "b": 3, "c": 2, "d": 4, "e": 3, "f": 3}

# [ My Solution ]

values = list(data.values())
counter = {}

for item in values:
    counter[item] = values.count(item)

common = max(counter.items(), key=lambda x: x[1])[0]
print(common)

# [ Improved Version ]

counter = Counter(data.values())  # Counter({3: 3, 2: 2, 4: 1})
common = max(counter, key=counter.get)  # type: ignore
print(common)
