# Write a program that merges two lists of the same length by alternating elements

list_a: list[int] = [0, 2, 4, 6, 8]
list_b: list[int] = [1, 3, 5, 7, 9]

# [ My solution ]
merged_list: list[int] = []

for i in range(len(list_a)):
    merged_list.append(list_a[i])
    merged_list.append(list_b[i])

print(merged_list)

# [ Improved version ]
print([num for pair in zip(list_a, list_b) for num in pair])

# list(zip(list_a, list_b)) => [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]
