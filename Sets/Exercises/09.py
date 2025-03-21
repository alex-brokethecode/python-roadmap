# Find the most common element in {1, 2, 3, 2, 4, 3, 2, 5, 3, 3, 3, 4}.


numbers = [1, 2, 3, 2, 4, 3, 2, 5, 3, 3, 3, 4]

# [ My Solution ]

counter = {}

for number in numbers:
    counter[number] = counter.get(number, 0) + 1

mode = max(counter.items(), key=lambda x: x[1])[0]
print(mode)
