# Invert a dictionary (keys become values and values become keys).

from collections import defaultdict

original: dict[str, int] = {"a": 1, "b": 2, "c": 3}

# [ My Solution ]
output = {value: key for key, value in original.items()}
print(output)
