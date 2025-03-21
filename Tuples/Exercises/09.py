# Write a program that finds the largest number in a tuple without using max()

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# [ My Solution ]

min_number = max_number = numbers[0]

for number in numbers[1:]:
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number

print(max_number)
print(min_number)
