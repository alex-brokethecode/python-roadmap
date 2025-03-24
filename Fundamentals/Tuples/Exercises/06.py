# Given tuple1 = (1, 2, 3, 2, 4, 2, 5), count how many times 2 appears without using .count()

tuple1 = (1, 2, 3, 2, 4, 2, 5)

# [ My Solution]

counter = 0

for number in tuple1:
    if number == 2:
        counter += 1

print(counter)
